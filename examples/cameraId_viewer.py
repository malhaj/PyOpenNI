#!/usr/bin/python
"""
Usage: python cameraId_viewer.py -camera <cameraId>
e.g. python cameraId_viewer.py -camera 0
If no -camera option is provided, the default cameraId 0 is used
"""

from openni import *
import numpy
import cv
import sys
import time

ctx = Context()
ctx.init()

cameraId = 0

for i in range(1,len(sys.argv)):
	if sys.argv[i] == '-camera':
		cameraId = int(sys.argv[i+1])

# get all the available devices
devicesList = NodeInfoList()
ctx.enumerate_production_trees(devicesList,NODE_TYPE_DEVICE)

# set the iterator at the first device
it = devicesList.begin()

# count the number of connected devices
devicesCount = 0;
while 1:
	if it.compare(devicesList.end()):
		break		
	else:
		devicesCount = devicesCount+1
		it.next()
print "Number of connected devices: " + str(devicesCount)

# if no device has the requested Id, exit
if cameraId > devicesCount - 1:
	print "No device with id: " + str(cameraId) + "!"
	raise SystemExit
# else set the iterator at the requested device
else:
	it = devicesList.begin()
	for x in range(0,cameraId):
		it.next()

# create a depth generator on the requested device
depth = DepthGenerator()
ctx.create_depth_generator_on_node(it, depth)
depth.set_resolution_preset(RES_VGA)
depth.fps = 30

# create an image generator on the requested device
color = ImageGenerator()
ctx.create_image_generator_on_node(it,color)
color.set_resolution_preset(RES_VGA)
color.fps = 30

depth.alternative_view_point_cap.set_view_point(color)

ctx.start_generating_all()

while True:
    
    ctx.wait_any_update_all()
 
    depthMap = depth.get_raw_depth_map()
    depthImage = numpy.fromstring(depthMap, dtype=numpy.uint16).reshape(depth.map.height, depth.map.width)
    
    colorMap = color.get_raw_image_map_bgr()
    colorImage = numpy.fromstring(colorMap, dtype=numpy.uint8).reshape(color.metadata.res[1],color.metadata.res[0],3)


    depthCV = cv.CreateImageHeader((depthImage.shape[1], depthImage.shape[0]), cv.IPL_DEPTH_16U, 1)
    scaleFactor = 20
    cv.SetData(depthCV, (depthImage*scaleFactor).tostring(), depthImage.dtype.itemsize * depthImage.shape[1])

    colorCV = cv.CreateImageHeader((colorImage.shape[1], colorImage.shape[0]), cv.IPL_DEPTH_8U, 3)
    cv.SetData(colorCV, colorImage.tostring())
    
    cv.ShowImage("Depth Window", depthCV)
    
    cv.ShowImage("Color Window", colorCV)

    keyEntered = cv.WaitKey(1)&0xff

    if keyEntered == 0x1b:
		cv.DestroyWindow("Depth Window")
		cv.DestroyWindow("Color Window")
		break

ctx.shutdown()
