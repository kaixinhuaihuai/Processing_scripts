#!/usr/bin/env python
"""
Calculate framewise displacement as done by Power et al., 2012
"""
import glob
import os
import re

rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/HS"
files = glob.glob("%s/sub-[0-2][0-9]/func/*func.nii.gz" %(rootdir))

for file in files:
    # cd into the file directory and get the file name
    print(file)
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]
    na = os.path.splitext(name)
    print(na)
    n = os.path.splitext(na[0])
    print(n)
    print(n[0])
    # ensure image is binary
    os.system("fslmaths %s -bin %s" %(name,name))
    # extract time series
    input = glob.glob("*rest_finalised_preproc.nii.gz")[0]
    out = "time_series_" + n[0] + ".txt"
    print(out)
    os.system("fslmeants -i %s -o %s -m %s" %(input,out,name))

rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/HSfdf"
files = glob.glob("%s/sub-[0-2][0-9]/func/*func.nii.gz" %(rootdir))

for file in files:
    # cd into the file directory and get the file name
    print(file)
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]
    # ensure image is binary
    os.system("fslmaths %s -bin %s" %(name,name))
    # extract time series
    input = glob.glob("*rest_finalised_preproc.nii.gz")[0]
    out = "time_series_" + name
    print(out)
    os.system("fslmeants -i %s -o %s -m %s" %(input,out,name))
