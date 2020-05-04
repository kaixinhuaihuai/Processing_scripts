#!/usr/bin/env python
import glob
import os
import re
import numpy as np

rootdir = "/media/phoenix/SeagateDrive/Dataset/LS"
files_run1 = glob.glob("%s/sub-[0-2][0-9]/func/*BU1_RPI_3dv1D.1D" %(rootdir))
files_run2 = glob.glob("%s/sub-[0-2][0-9]/func/*BU2_RPI_3dv1D.1D" %(rootdir))

for file in files_run1:
    # cd into the file directory and get the file name
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]
    print(file)

    motion_params = np.genfromtxt(file).T
    np.savetxt ("run_1m1.txt", motion_params[0,:])
    np.savetxt ("run_1m2.txt", motion_params[1,:])
    np.savetxt ("run_1m3.txt", motion_params[2,:])
    np.savetxt ("run_1m4.txt", motion_params[3,:])
    np.savetxt ("run_1m5.txt", motion_params[4,:])
    np.savetxt ("run_1m6.txt", motion_params[5,:])

for file in files_run2:
    # cd into the file directory and get the file name
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]
    print(file)

    motion_params = np.genfromtxt(file).T
    np.savetxt ("run_2m1.txt", motion_params[0,:])
    np.savetxt ("run_2m2.txt", motion_params[1,:])
    np.savetxt ("run_2m3.txt", motion_params[2,:])
    np.savetxt ("run_2m4.txt", motion_params[3,:])
    np.savetxt ("run_2m5.txt", motion_params[4,:])
    np.savetxt ("run_2m6.txt", motion_params[5,:])


rootdir = "/media/phoenix/SeagateDrive/Dataset/HS"
files_run1 = glob.glob("%s/sub-[0-2][0-9]/func/*BU1_RPI_3dv1D.1D" %(rootdir))
files_run2 = glob.glob("%s/sub-[0-2][0-9]/func/*BU2_RPI_3dv1D.1D" %(rootdir))

for file in files_run1:
    # cd into the file directory and get the file name
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]
    print(file)

    motion_params = np.genfromtxt(file).T
    np.savetxt ("run_1m1.txt", motion_params[0,:])
    np.savetxt ("run_1m2.txt", motion_params[1,:])
    np.savetxt ("run_1m3.txt", motion_params[2,:])
    np.savetxt ("run_1m4.txt", motion_params[3,:])
    np.savetxt ("run_1m5.txt", motion_params[4,:])
    np.savetxt ("run_1m6.txt", motion_params[5,:])

for file in files_run2:
    # cd into the file directory and get the file name
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]
    print(file)

    motion_params = np.genfromtxt(file).T
    np.savetxt ("run_2m1.txt", motion_params[0,:])
    np.savetxt ("run_2m2.txt", motion_params[1,:])
    np.savetxt ("run_2m3.txt", motion_params[2,:])
    np.savetxt ("run_2m4.txt", motion_params[3,:])
    np.savetxt ("run_2m5.txt", motion_params[4,:])
    np.savetxt ("run_2m6.txt", motion_params[5,:])
