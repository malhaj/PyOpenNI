/* ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This file is part of PyOpenNI.
 *
 * PyOpenNI is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * PyOpenNI is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with PyOpenNI.  If not, see <http://www.gnu.org/licenses/>.
 *
 * PyOpenNI is Copyright (C) 2011, Xavier Mendez (jmendeth).
 * OpenNI Python Wrapper (ONIPY) is Copyright (C) 2011, Gabriele Nataneli (gamix).
 *
 * ***** END GPL LICENSE BLOCK ***** */


#ifndef OUTPUT_META_DATA_WRAPPER_H
#define	OUTPUT_META_DATA_WRAPPER_H

#include "wrapperTypes.h"

XnUInt64 OutputMetaData_Timestamp_wrapped(xn::OutputMetaData& self);
XnUInt32 OutputMetaData_FrameID_wrapped(xn::OutputMetaData& self);
XnBool OutputMetaData_IsDataNew_wrapped(xn::OutputMetaData& self);

#endif	/* OUTPUT_META_DATA_WRAPPER_H */
