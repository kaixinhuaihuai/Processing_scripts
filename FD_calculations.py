#!/usr/bin/env python
"""
Calculate framewise displacement as done by Power et al., 2012
"""
import glob
import numpy as np
import os
"""
LS Group
"""

rootdir = "/media/phoenix/SeagateDrive/Dataset/LS"  #change as necessary
files = glob.glob("%s/sub-[0-2][0-9]/func/rest_RPI_3dv1D.1D" %(rootdir))

for file in files:
    path = os.path.split(file)
    motion_params = np.genfromtxt(file).T
    rotations = np.transpose(np.abs(np.diff(motion_params[0:3,:])))
    translations = np.transpose(np.abs(np.diff(motion_params[3:6,:])))

    fd =np.sum(translations,axis=1) + (50 * np.pi / 180) * np.sum(rotations,axis=1)

    fd = np.insert(fd, 0, 0)

    out_file = os.path.join(path[0], "rest_FD.1D")
    np.savetxt(out_file, fd)


rootdir = "/media/phoenix/SeagateDrive/Dataset/HS"  #change as necessary
files = glob.glob("%s/sub-[0-2][0-9]/func/rest_RPI_3dv1D.1D" %(rootdir))

for file in files:
    path = os.path.split(file)
    motion_params = np.genfromtxt(file).T
    rotations = np.transpose(np.abs(np.diff(motion_params[0:3,:])))
    translations = np.transpose(np.abs(np.diff(motion_params[3:6,:])))

    fd =np.sum(translations,axis=1) + (50 * np.pi / 180) * np.sum(rotations,axis=1)

    fd = np.insert(fd, 0, 0)

    out_file = os.path.join(path[0], "rest_FD.1D")
    np.savetxt(out_file, fd)
