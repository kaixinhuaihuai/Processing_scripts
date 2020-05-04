#!/usr/bin/env python
import glob
import os
import re
import shutil
import json
import numpy as np

template = "/usr/local/fsl/data/standard/MNI152_T1_2mm_brain.nii.gz"
expr = "a*b"

""""
Functional preprocessing using AFNI and FSL. Processing involves reorientating into RPI and slice time correction.
Motion correction is performed using a two-stage approach - images are first coregistered to the mean fMRI and then a
new mean is calculated and used as the target for a second coregistration using AFNI.
A 6 DOF linear transform between mean fMRI and structural image using FSL boundary-based registration. Refine
transformation using non-linear.Nuisance Variable Regression performed on the motion corrrected data using a 2nd order polynomial,
a 6-regressor model of motion, and the time series of the WM and CSF masks. Tranforming fMRI to match 2mm MNI
space using inverse of linear fMRI-sMRI transform.
Process with bandpass filtering (0.001Hz < f < 0.1Hz), smoothed with 6mm FWHM kernel.

"""
def get_file_run1():
    js_name = "sub-%s_task-beliefup_run-1_bold.json" %(n[0])
    information = json.loads(open(js_name).read())
    sl_times = information["SliceTiming"]
    return (sl_times)


def create_files_run1(input):
    with open("slice_times.txt", "w") as f:
        for item in input:
            f.write("%s " % item)


def get_file_run2():
    js_name = "sub-%s_task-beliefup_run-2_bold.json" %(n[0])
    information = json.loads(open(js_name).read())
    sl_times = information["SliceTiming"]
    return (sl_times)


def create_files_run2(input):
    with open("slice_times2.txt", "w") as f:
        for item in input:
            f.write("%s " % item)



"""
RUN 1
LS Group!!!
"""

rootdir = "/media/phoenix/SeagateDrive/Dataset/LS"
files = glob.glob("%s/sub-[0-2][0-9]/func/*run-1_bold.nii.gz" %(rootdir))

for file in files:
    #check if anatomical file exists
    if os.path.isfile(file):
        print("%s exists" %(file))
    else:
        print("%s exists" %(file))
        break

    # cd into the file directory and get the file name
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]


    # Reorient data
    print ("Reorienting %s" %(file))
    os.system("3drefit -deoblique %s" %(name))
    os.system("3dresample -orient RPI -prefix BU1_RPI.nii.gz -inset %s" %(name))


    # Slice timing correction
    print("Start slice timing correction on %s" %(file))
    sl_times = get_file_run1()
    create_files_run1(sl_times)
    rpi = glob.glob("*BU1_RPI.nii.gz")[0]
    print(rpi)
    os.system("3dTshift -TR 2.0 -tpattern @slice_times.txt -prefix BU1_time_corr.nii.gz %s -verbose" %(rpi))


    # Calculate voxel wise statistics (mean intensity values over all timepoints for each voxel)
    print(" Getting voxel wise statistics for %s" %(file))
    r_ts = glob.glob("*BU1_time_corr.nii.gz")[0]
    os.system("3dTstat -mean -prefix BU1_3dT.nii.gz %s" %(r_ts))


    # motion correction - two pass
    print ("start first pass motion correction on %s" %(file))
    base = glob.glob("*BU1_3dT.nii.gz")[0]       # base image is the mean intensity RPI image obtained above
        # for each volume, the command aligns the image with the base mean image and calculates the Motion
        # displacement and movement parameters.
    os.system("3dvolreg -Fourier -twopass -base %s -zpad 4 -maxdisp1D BU1_RPI_3dvmd1D.1D\
                -1Dfile BU1_RPI_3dv1D.1D -prefix BU1_RPI_3d.nii.gz %s" %(base, rpi))

        # calculate the voxel wise statistics for the motion corrected output from above, with mean intensity values over
        # all timepoints for each voxel
    print ("Start second pass motion correction on %s" %(file))
    mo_cor = glob.glob("*BU1_RPI_3d.nii.gz")[0]
    os.system("3dTstat -mean -prefix BU1_RPI_3dv_3dT.nii.gz %s" %(mo_cor))
        # motion correction and get motion, movement and displacement parameters
    mean_mo_cor = glob.glob("*BU1_RPI_3dv_3dT.nii.gz")[0]
    os.system("3dvolreg -Fourier -twopass -base %s -zpad 4 -maxdisp1D BU1_RPI_3dvmd1D.1D\
                -1Dfile BU1_RPI_3dv1D.1D -prefix BU1_RPI_3dv.nii.gz %s" %(mean_mo_cor, rpi))


    # Create a brain only mask
    print ("Creating brain mask only...")
    motion_corrected = glob.glob("*BU1_RPI_3dv.nii.gz")[0]
    os.system("3dAutomask -prefix BU1_RPI_3dv_automask.nii.gz %s" %(motion_corrected))


    # Edge detect - remove skull
    print ("Detect edge and remove skull on %s" %(file))
    b = glob.glob("*BU1_RPI_3dv_automask.nii.gz")[0]
    os.system("3dcalc -a %s -b %s -expr %s -prefix BU1_RPI_3dv_3dc.nii.gz" %(motion_corrected,b,expr))


    # normalize image intensity values
    print("Normalizing image intensity values...")
    ins = glob.glob("*BU1_RPI_3dv_3dc.nii.gz")[0]
    os.system("fslmaths %s -ing 10000 BU1_RPI_3dv_3dc_maths.nii.gz -odt float" %(ins))


    # calculate mean of skull stripped image
    print("Calculate mean of skull stripped image...")
    os.system("3dTstat -mean -prefix BU1_RPI_3dv_3dc_3dT.nii.gz %s" %(ins))


    # create mask (generate mask from normalized intensity data)
    print ("Generating mask from normalized intensity data...")
    maths = glob.glob("*BU1_RPI_3dv_3dc_maths.nii.gz")[0]
    os.system("fslmaths %s -Tmin -bin BU1_RPI_3dv_3dc_maths_maths.nii.gz -odt char" %(maths))


    # Register functional to mni data - register a functional scan in native space to MNI standard rest_MNI_space
    print("Performing linear transformation on the functional data to anatomical...")
    ss = glob.glob("*stripped_T1.nii.gz")[0]
    func = glob.glob("*BU1_RPI_3dv_3dc.nii.gz")[0]
    os.system("flirt -in %s -ref %s -omat BU1_to_anat_linear.mat -out BU1_to_T1.nii.gz"%(func,ss))
        # do functional to mni space
    print ("Combining rest to T1 and T1 to MNI...")
    out = glob.glob("*BU1_to_anat_linear.mat")[0]
    t1_to_mni = glob.glob("*affine_transform.mat")[0]
    os.system("convert_xfm -omat BU1_mni_linear.mat -concat %s %s "%(t1_to_mni, out))
        # invert to get mni to funcional
    print("Inverting to get mni to functional data...")
    mat = glob.glob("*BU1_mni_linear.mat")[0]
    os.system("convert_xfm -omat mni_to_BU1_linear.mat -inverse %s"%(mat))
        # apply the warp to the data to get data from mni to functional native space
    print("Apply warp to get functional data in mni space")
    non_linear = glob.glob("*non_linear_t1_to_mni.nii.gz")[0]
    os.system("applywarp --in=%s --ref=%s --warp=%s --premat=%s --out=mni_to_BU1.nii.gz" %(func,template,non_linear,out))


    print("Smoothing...")
    data = glob.glob("*mni_to_BU1.nii.gz")[0]
    os.system("3dmerge -1blur_fwhm 6 -doall -prefix BU1_smoothed.nii.gz %s" %(data))

    print("De-mean motion parameters...")
    os.system("1d_tool.py -infile BU1_RPI_3dv1D.1D -set_nruns 1 -demean -write motion_demean.1D")
    print("Compute motion parameter derivaties...")
    os.system("1d_tool.py -infile BU1_RPI_3dv1D.1D -set_nruns 1 -derivative -demean -write motion_deriv.1D")
    #print("convert motion parameters for per run regression...")
    #os.system("1d_tool.py -infile motion_demean.1D -set_nruns 1 -split_into_pad_runs mot_demean")
    #os.system("1d_tool.py -infile motion_deriv.1D -set_nruns 1 -split_into_pad_runs mot_deriv")
    print("create censor file motion...")
    os.system("1d_tool.py -infile BU1_RPI_3dv1D.1D -set_nruns 1 -show_censor_count\
              -censor_prev_TR -censor_motion 0.2 motion_%s" %(n[0]))

    print ("Nuisance regression started...")
    csf_mask = glob.glob("*csf_mask.nii.gz")[0]
    wm_mask = glob.glob("*wm_mask.nii.gz")[0]
    print("resample the CSF and WM masks...")
    os.system("3dresample -master %s -inset %s -prefix csf_resampled.nii.gz" %(data, csf_mask))
    os.system("3dresample -master %s -inset %s -prefix wm_resampled.nii.gz" %(data, wm_mask))
        # extract time courses from wm and csf
        # extract time courses from wm and csf
    os.system("3dmaskave -q -mask csf_resampled.nii.gz %s > csf_tc_file.1D" %(data))
    os.system("3dmaskave -q -mask wm_resampled.nii.gz %s > wm_tc_file.1D" %(data))

    # Perform nuisance variable regression - remove motion parameters, csf and wm time courses
    data = glob.glob("*BU1_smoothed.nii.gz")[0]
    os.system("3dDeconvolve -input %s -censor motion_%s_censor.1D\
            -polort A -num_stimts 14\
            -stim_file 1 motion_demean.1D'[0]' -stim_base 1 -stim_label 1 roll_01 \
            -stim_file 2 motion_demean.1D'[1]' -stim_base 2 -stim_label 2 pitch_01 \
            -stim_file 3 motion_demean.1D'[2]' -stim_base 3 -stim_label 3 yaw_01 \
            -stim_file 4 motion_demean.1D'[3]' -stim_base 4 -stim_label 4 dS_01 \
            -stim_file 5 motion_demean.1D'[4]' -stim_base 5 -stim_label 5 dL_01 \
            -stim_file 6 motion_demean.1D'[5]' -stim_base 6 -stim_label 6 dP_01 \
            -stim_file 7 motion_deriv.1D'[0]' -stim_base 7 -stim_label 7 roll_02 \
            -stim_file 8 motion_deriv.1D'[1]' -stim_base 8 -stim_label 8 pitch_02 \
            -stim_file 9 motion_deriv.1D'[2]' -stim_base 9 -stim_label 9 yaw_02 \
            -stim_file 10 motion_deriv.1D'[3]' -stim_base 10 -stim_label 10 dS_02 \
            -stim_file 11 motion_deriv.1D'[4]' -stim_base 11 -stim_label 11 dL_02 \
            -stim_file 12 motion_deriv.1D'[5]' -stim_base 12 -stim_label 12 dP_02 \
            -stim_file 13 csf_tc_file.1D -stim_base 13 -stim_label 13 csf \
            -stim_file 14 wm_tc_file.1D -stim_base 14 -stim_label 14 wm \
            -fout -tout -x1D X.xmat.1D -xjpeg X.jpg\
            -x1D_uncensored X.nocensor.xmat.1D -fitts fitts.19 -errts errts.%s -x1D_stop -bucket stats.%s" %(data,n[0],n[0],n[0]))

    print("Start 3dTproject...")
    os.system("3dTproject -polort 0 -input %s -censor motion_%s_censor.1D -cenmode ZERO -ort X.nocensor.xmat.1D\
            -prefix BU1_FINAL.nii.gz" %(data,n[0]))

"""
RUN 2
LS Group!!!
"""

rootdir = "/media/phoenix/SeagateDrive/Dataset/LS"
files = glob.glob("%s/sub-[0-2][0-9]/func/*run-2_bold.nii.gz" %(rootdir))

for file in files:
    #check if anatomical file exists
    if os.path.isfile(file):
        print("%s exists" %(file))
    else:
        print("%s exists" %(file))
        break

    # cd into the file directory and get the file name
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]


    # Reorient data
    print ("Reorienting %s" %(file))
    os.system("3drefit -deoblique %s" %(name))
    os.system("3dresample -orient RPI -prefix BU2_RPI.nii.gz -inset %s" %(name))


    # Slice timing correction
    print("Start slice timing correction on %s" %(file))
    sl_times = get_file_run2()
    create_files_run2(sl_times)
    rpi = glob.glob("*BU2_RPI.nii.gz")[0]
    print(rpi)
    os.system("3dTshift -TR 2.0 -tpattern @slice_times2.txt -prefix BU2_time_corr.nii.gz %s -verbose" %(rpi))


    # Calculate voxel wise statistics (mean intensity values over all timepoints for each voxel)
    print(" Getting voxel wise statistics for %s" %(file))
    r_ts = glob.glob("*BU2_time_corr.nii.gz")[0]
    os.system("3dTstat -mean -prefix BU2_3dT.nii.gz %s" %(r_ts))


    # motion correction - two pass
    print ("start first pass motion correction on %s" %(file))
    base = glob.glob("*BU2_3dT.nii.gz")[0]       # base image is the mean intensity RPI image obtained above
        # for each volume, the command aligns the image with the base mean image and calculates the Motion
        # displacement and movement parameters.
    os.system("3dvolreg -Fourier -twopass -base %s -zpad 4 -maxdisp1D BU2_RPI_3dvmd1D.1D\
                -1Dfile BU2_RPI_3dv1D.1D -prefix BU2_RPI_3d.nii.gz %s" %(base, rpi))

        # calculate the voxel wise statistics for the motion corrected output from above, with mean intensity values over
        # all timepoints for each voxel
    print ("Start second pass motion correction on %s" %(file))
    mo_cor = glob.glob("*BU2_RPI_3d.nii.gz")[0]
    os.system("3dTstat -mean -prefix BU2_RPI_3dv_3dT.nii.gz %s" %(mo_cor))
        # motion correction and get motion, movement and displacement parameters
    mean_mo_cor = glob.glob("*BU2_RPI_3dv_3dT.nii.gz")[0]
    os.system("3dvolreg -Fourier -twopass -base %s -zpad 4 -maxdisp1D BU2_RPI_3dvmd1D.1D\
                -1Dfile BU2_RPI_3dv1D.1D -prefix BU2_RPI_3dv.nii.gz %s" %(mean_mo_cor, rpi))


    # Create a brain only mask
    print ("Creating brain mask only...")
    motion_corrected = glob.glob("*BU2_RPI_3dv.nii.gz")[0]
    os.system("3dAutomask -prefix BU2_RPI_3dv_automask.nii.gz %s" %(motion_corrected))


    # Edge detect - remove skull
    print ("Detect edge and remove skull on %s" %(file))
    b = glob.glob("*BU2_RPI_3dv_automask.nii.gz")[0]
    os.system("3dcalc -a %s -b %s -expr %s -prefix BU2_RPI_3dv_3dc.nii.gz" %(motion_corrected,b,expr))


    # normalize image intensity values
    print("Normalizing image intensity values...")
    ins = glob.glob("*BU2_RPI_3dv_3dc.nii.gz")[0]
    os.system("fslmaths %s -ing 10000 BU2_RPI_3dv_3dc_maths.nii.gz -odt float" %(ins))


    # calculate mean of skull stripped image
    print("Calculate mean of skull stripped image...")
    os.system("3dTstat -mean -prefix BU2_RPI_3dv_3dc_3dT.nii.gz %s" %(ins))


    # create mask (generate mask from normalized intensity data)
    print ("Generating mask from normalized intensity data...")
    maths = glob.glob("*BU2_RPI_3dv_3dc_maths.nii.gz")[0]
    os.system("fslmaths %s -Tmin -bin BU2_RPI_3dv_3dc_maths_maths.nii.gz -odt char" %(maths))


    # Register functional to mni data - register a functional scan in native space to MNI standard rest_MNI_space
    print("Performing linear transformation on the functional data to anatomical...")
    ss = glob.glob("*stripped_T1.nii.gz")[0]
    func = glob.glob("*BU2_RPI_3dv_3dc.nii.gz")[0]
    os.system("flirt -in %s -ref %s -omat BU2_to_anat_linear.mat -out BU2_to_T1.nii.gz"%(func,ss))
        # do functional to mni space
    print ("Combining rest to T1 and T1 to MNI...")
    out = glob.glob("*BU2_to_anat_linear.mat")[0]
    t1_to_mni = glob.glob("*affine_transform.mat")[0]
    os.system("convert_xfm -omat BU2_mni_linear.mat -concat %s %s "%(t1_to_mni, out))
        # invert to get mni to funcional
    print("Inverting to get mni to functional data...")
    mat = glob.glob("*BU2_mni_linear.mat")[0]
    os.system("convert_xfm -omat mni_to_BU2_linear.mat -inverse %s"%(mat))
        # apply the warp to the data to get data from mni to functional native space
    print("Apply warp to get functional data in mni space")
    non_linear = glob.glob("*non_linear_t1_to_mni.nii.gz")[0]
    os.system("applywarp --in=%s --ref=%s --warp=%s --premat=%s --out=mni_to_BU2.nii.gz" %(func,template,non_linear,out))


    print("Smoothing...")
    data = glob.glob("*mni_to_BU2.nii.gz")[0]
    os.system("3dmerge -1blur_fwhm 6 -doall -prefix BU2_smoothed.nii.gz %s" %(data))

    print("De-mean motion parameters...")
    os.system("1d_tool.py -infile BU2_RPI_3dv1D.1D -set_nruns 1 -demean -write motion_demean.1D")
    print("Compute motion parameter derivaties...")
    os.system("1d_tool.py -infile BU2_RPI_3dv1D.1D -set_nruns 1 -derivative -demean -write motion_deriv.1D")
    #print("convert motion parameters for per run regression...")
    #os.system("1d_tool.py -infile motion_demean.1D -set_nruns 1 -split_into_pad_runs mot_demean")
    #os.system("1d_tool.py -infile motion_deriv.1D -set_nruns 1 -split_into_pad_runs mot_deriv")
    print("create censor file motion...")
    os.system("1d_tool.py -infile BU2_RPI_3dv1D.1D -set_nruns 1 -show_censor_count\
              -censor_prev_TR -censor_motion 0.2 motion_%s" %(n[0]))

    print ("Nuisance regression started...")
    csf_mask = glob.glob("*csf_mask.nii.gz")[0]
    wm_mask = glob.glob("*wm_mask.nii.gz")[0]
    print("resample the CSF and WM masks...")
    os.system("3dresample -master %s -inset %s -prefix csf_resampled.nii.gz" %(data, csf_mask))
    os.system("3dresample -master %s -inset %s -prefix wm_resampled.nii.gz" %(data, wm_mask))
        # extract time courses from wm and csf
        # extract time courses from wm and csf
    os.system("3dmaskave -q -mask csf_resampled.nii.gz %s > csf_tc_file.1D" %(data))
    os.system("3dmaskave -q -mask wm_resampled.nii.gz %s > wm_tc_file.1D" %(data))

    # Perform nuisance variable regression - remove motion parameters, csf and wm time courses
    data = glob.glob("*BU2_smoothed.nii.gz")[0]
    os.system("3dDeconvolve -input %s -censor motion_%s_censor.1D\
            -polort A -num_stimts 14\
            -stim_file 1 motion_demean.1D'[0]' -stim_base 1 -stim_label 1 roll_01 \
            -stim_file 2 motion_demean.1D'[1]' -stim_base 2 -stim_label 2 pitch_01 \
            -stim_file 3 motion_demean.1D'[2]' -stim_base 3 -stim_label 3 yaw_01 \
            -stim_file 4 motion_demean.1D'[3]' -stim_base 4 -stim_label 4 dS_01 \
            -stim_file 5 motion_demean.1D'[4]' -stim_base 5 -stim_label 5 dL_01 \
            -stim_file 6 motion_demean.1D'[5]' -stim_base 6 -stim_label 6 dP_01 \
            -stim_file 7 motion_deriv.1D'[0]' -stim_base 7 -stim_label 7 roll_02 \
            -stim_file 8 motion_deriv.1D'[1]' -stim_base 8 -stim_label 8 pitch_02 \
            -stim_file 9 motion_deriv.1D'[2]' -stim_base 9 -stim_label 9 yaw_02 \
            -stim_file 10 motion_deriv.1D'[3]' -stim_base 10 -stim_label 10 dS_02 \
            -stim_file 11 motion_deriv.1D'[4]' -stim_base 11 -stim_label 11 dL_02 \
            -stim_file 12 motion_deriv.1D'[5]' -stim_base 12 -stim_label 12 dP_02 \
            -stim_file 13 csf_tc_file.1D -stim_base 13 -stim_label 13 csf \
            -stim_file 14 wm_tc_file.1D -stim_base 14 -stim_label 14 wm \
            -fout -tout -x1D X.xmat.1D -xjpeg X.jpg\
            -x1D_uncensored X.nocensor.xmat.1D -fitts fitts.19 -errts errts.%s -x1D_stop -bucket stats.%s" %(data,n[0],n[0],n[0]))

    print("Start 3dTproject...")
    os.system("3dTproject -polort 0 -input %s -censor motion_%s_censor.1D -cenmode ZERO -ort X.nocensor.xmat.1D\
            -prefix BU2_FINAL.nii.gz" %(data,n[0]))


"""
RUN 1
HS Group!!!
"""

rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/HS"
files = glob.glob("%s/sub-[0-2][0-9]/func/*run-1_bold.nii.gz" %(rootdir))

for file in files:
    #check if anatomical file exists
    if os.path.isfile(file):
        print("%s exists" %(file))
    else:
        print("%s exists" %(file))
        break

    # cd into the file directory and get the file name
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]


    # Reorient data
    print ("Reorienting %s" %(file))
    os.system("3drefit -deoblique %s" %(name))
    os.system("3dresample -orient RPI -prefix BU1_RPI.nii.gz -inset %s" %(name))


    # Slice timing correction
    print("Start slice timing correction on %s" %(file))
    sl_times = get_file_run1()
    create_files_run1(sl_times)
    rpi = glob.glob("*BU1_RPI.nii.gz")[0]
    print(rpi)
    os.system("3dTshift -TR 2.0 -tpattern @slice_times.txt -prefix BU1_time_corr.nii.gz %s -verbose" %(rpi))


    # Calculate voxel wise statistics (mean intensity values over all timepoints for each voxel)
    print(" Getting voxel wise statistics for %s" %(file))
    r_ts = glob.glob("*BU1_time_corr.nii.gz")[0]
    os.system("3dTstat -mean -prefix BU1_3dT.nii.gz %s" %(r_ts))


    # motion correction - two pass
    print ("start first pass motion correction on %s" %(file))
    base = glob.glob("*BU1_3dT.nii.gz")[0]       # base image is the mean intensity RPI image obtained above
        # for each volume, the command aligns the image with the base mean image and calculates the Motion
        # displacement and movement parameters.
    os.system("3dvolreg -Fourier -twopass -base %s -zpad 4 -maxdisp1D BU1_RPI_3dvmd1D.1D\
                -1Dfile BU1_RPI_3dv1D.1D -prefix BU1_RPI_3d.nii.gz %s" %(base, rpi))

        # calculate the voxel wise statistics for the motion corrected output from above, with mean intensity values over
        # all timepoints for each voxel
    print ("Start second pass motion correction on %s" %(file))
    mo_cor = glob.glob("*BU1_RPI_3d.nii.gz")[0]
    os.system("3dTstat -mean -prefix BU1_RPI_3dv_3dT.nii.gz %s" %(mo_cor))
        # motion correction and get motion, movement and displacement parameters
    mean_mo_cor = glob.glob("*BU1_RPI_3dv_3dT.nii.gz")[0]
    os.system("3dvolreg -Fourier -twopass -base %s -zpad 4 -maxdisp1D BU1_RPI_3dvmd1D.1D\
                -1Dfile BU1_RPI_3dv1D.1D -prefix BU1_RPI_3dv.nii.gz %s" %(mean_mo_cor, rpi))


    # Create a brain only mask
    print ("Creating brain mask only...")
    motion_corrected = glob.glob("*BU1_RPI_3dv.nii.gz")[0]
    os.system("3dAutomask -prefix BU1_RPI_3dv_automask.nii.gz %s" %(motion_corrected))


    # Edge detect - remove skull
    print ("Detect edge and remove skull on %s" %(file))
    b = glob.glob("*BU1_RPI_3dv_automask.nii.gz")[0]
    os.system("3dcalc -a %s -b %s -expr %s -prefix BU1_RPI_3dv_3dc.nii.gz" %(motion_corrected,b,expr))


    # normalize image intensity values
    print("Normalizing image intensity values...")
    ins = glob.glob("*BU1_RPI_3dv_3dc.nii.gz")[0]
    os.system("fslmaths %s -ing 10000 BU1_RPI_3dv_3dc_maths.nii.gz -odt float" %(ins))


    # calculate mean of skull stripped image
    print("Calculate mean of skull stripped image...")
    os.system("3dTstat -mean -prefix BU1_RPI_3dv_3dc_3dT.nii.gz %s" %(ins))


    # create mask (generate mask from normalized intensity data)
    print ("Generating mask from normalized intensity data...")
    maths = glob.glob("*BU1_RPI_3dv_3dc_maths.nii.gz")[0]
    os.system("fslmaths %s -Tmin -bin BU1_RPI_3dv_3dc_maths_maths.nii.gz -odt char" %(maths))


    # Register functional to mni data - register a functional scan in native space to MNI standard rest_MNI_space
    print("Performing linear transformation on the functional data to anatomical...")
    ss = glob.glob("*stripped_T1.nii.gz")[0]
    func = glob.glob("*BU1_RPI_3dv_3dc.nii.gz")[0]
    os.system("flirt -in %s -ref %s -omat BU1_to_anat_linear.mat -out BU1_to_T1.nii.gz"%(func,ss))
        # do functional to mni space
    print ("Combining rest to T1 and T1 to MNI...")
    out = glob.glob("*BU1_to_anat_linear.mat")[0]
    t1_to_mni = glob.glob("*affine_transform.mat")[0]
    os.system("convert_xfm -omat BU1_mni_linear.mat -concat %s %s "%(t1_to_mni, out))
        # invert to get mni to funcional
    print("Inverting to get mni to functional data...")
    mat = glob.glob("*BU1_mni_linear.mat")[0]
    os.system("convert_xfm -omat mni_to_BU1_linear.mat -inverse %s"%(mat))
        # apply the warp to the data to get data from mni to functional native space
    print("Apply warp to get functional data in mni space")
    non_linear = glob.glob("*non_linear_t1_to_mni.nii.gz")[0]
    os.system("applywarp --in=%s --ref=%s --warp=%s --premat=%s --out=mni_to_BU1.nii.gz" %(func,template,non_linear,out))


    print("Smoothing...")
    data = glob.glob("*mni_to_BU1.nii.gz")[0]
    os.system("3dmerge -1blur_fwhm 6 -doall -prefix BU1_smoothed.nii.gz %s" %(data))

    print("De-mean motion parameters...")
    os.system("1d_tool.py -infile BU1_RPI_3dv1D.1D -set_nruns 1 -demean -write motion_demean.1D")
    print("Compute motion parameter derivaties...")
    os.system("1d_tool.py -infile BU1_RPI_3dv1D.1D -set_nruns 1 -derivative -demean -write motion_deriv.1D")
    #print("convert motion parameters for per run regression...")
    #os.system("1d_tool.py -infile motion_demean.1D -set_nruns 1 -split_into_pad_runs mot_demean")
    #os.system("1d_tool.py -infile motion_deriv.1D -set_nruns 1 -split_into_pad_runs mot_deriv")
    print("create censor file motion...")
    os.system("1d_tool.py -infile BU1_RPI_3dv1D.1D -set_nruns 1 -show_censor_count\
              -censor_prev_TR -censor_motion 0.2 motion_%s" %(n[0]))

    print ("Nuisance regression started...")
    csf_mask = glob.glob("*csf_mask.nii.gz")[0]
    wm_mask = glob.glob("*wm_mask.nii.gz")[0]
    print("resample the CSF and WM masks...")
    os.system("3dresample -master %s -inset %s -prefix csf_resampled.nii.gz" %(data, csf_mask))
    os.system("3dresample -master %s -inset %s -prefix wm_resampled.nii.gz" %(data, wm_mask))
        # extract time courses from wm and csf
        # extract time courses from wm and csf
    os.system("3dmaskave -q -mask csf_resampled.nii.gz %s > csf_tc_file.1D" %(data))
    os.system("3dmaskave -q -mask wm_resampled.nii.gz %s > wm_tc_file.1D" %(data))

    # Perform nuisance variable regression - remove motion parameters, csf and wm time courses
    data = glob.glob("*BU1_smoothed.nii.gz")[0]
    os.system("3dDeconvolve -input %s -censor motion_%s_censor.1D\
            -polort A -num_stimts 14\
            -stim_file 1 motion_demean.1D'[0]' -stim_base 1 -stim_label 1 roll_01 \
            -stim_file 2 motion_demean.1D'[1]' -stim_base 2 -stim_label 2 pitch_01 \
            -stim_file 3 motion_demean.1D'[2]' -stim_base 3 -stim_label 3 yaw_01 \
            -stim_file 4 motion_demean.1D'[3]' -stim_base 4 -stim_label 4 dS_01 \
            -stim_file 5 motion_demean.1D'[4]' -stim_base 5 -stim_label 5 dL_01 \
            -stim_file 6 motion_demean.1D'[5]' -stim_base 6 -stim_label 6 dP_01 \
            -stim_file 7 motion_deriv.1D'[0]' -stim_base 7 -stim_label 7 roll_02 \
            -stim_file 8 motion_deriv.1D'[1]' -stim_base 8 -stim_label 8 pitch_02 \
            -stim_file 9 motion_deriv.1D'[2]' -stim_base 9 -stim_label 9 yaw_02 \
            -stim_file 10 motion_deriv.1D'[3]' -stim_base 10 -stim_label 10 dS_02 \
            -stim_file 11 motion_deriv.1D'[4]' -stim_base 11 -stim_label 11 dL_02 \
            -stim_file 12 motion_deriv.1D'[5]' -stim_base 12 -stim_label 12 dP_02 \
            -stim_file 13 csf_tc_file.1D -stim_base 13 -stim_label 13 csf \
            -stim_file 14 wm_tc_file.1D -stim_base 14 -stim_label 14 wm \
            -fout -tout -x1D X.xmat.1D -xjpeg X.jpg\
            -x1D_uncensored X.nocensor.xmat.1D -fitts fitts.19 -errts errts.%s -x1D_stop -bucket stats.%s" %(data,n[0],n[0],n[0]))

    print("Start 3dTproject...")
    os.system("3dTproject -polort 0 -input %s -censor motion_%s_censor.1D -cenmode ZERO -ort X.nocensor.xmat.1D\
            -prefix BU1_FINAL.nii.gz" %(data,n[0]))

"""
RUN 2
HS Group!!!
"""

rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/HS"
files = glob.glob("%s/sub-[0-2][0-9]/func/*run-2_bold.nii.gz" %(rootdir))

for file in files:
    #check if anatomical file exists
    if os.path.isfile(file):
        print("%s exists" %(file))
    else:
        print("%s exists" %(file))
        break

    # cd into the file directory and get the file name
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]


    # Reorient data
    print ("Reorienting %s" %(file))
    os.system("3drefit -deoblique %s" %(name))
    os.system("3dresample -orient RPI -prefix BU2_RPI.nii.gz -inset %s" %(name))


    # Slice timing correction
    print("Start slice timing correction on %s" %(file))
    sl_times = get_file_run2()
    create_files_run2(sl_times)
    rpi = glob.glob("*BU2_RPI.nii.gz")[0]
    print(rpi)
    os.system("3dTshift -TR 2.0 -tpattern @slice_times2.txt -prefix BU2_time_corr.nii.gz %s -verbose" %(rpi))


    # Calculate voxel wise statistics (mean intensity values over all timepoints for each voxel)
    print(" Getting voxel wise statistics for %s" %(file))
    r_ts = glob.glob("*BU2_time_corr.nii.gz")[0]
    os.system("3dTstat -mean -prefix BU2_3dT.nii.gz %s" %(r_ts))


    # motion correction - two pass
    print ("start first pass motion correction on %s" %(file))
    base = glob.glob("*BU2_3dT.nii.gz")[0]       # base image is the mean intensity RPI image obtained above
        # for each volume, the command aligns the image with the base mean image and calculates the Motion
        # displacement and movement parameters.
    os.system("3dvolreg -Fourier -twopass -base %s -zpad 4 -maxdisp1D BU2_RPI_3dvmd1D.1D\
                -1Dfile BU2_RPI_3dv1D.1D -prefix BU2_RPI_3d.nii.gz %s" %(base, rpi))

        # calculate the voxel wise statistics for the motion corrected output from above, with mean intensity values over
        # all timepoints for each voxel
    print ("Start second pass motion correction on %s" %(file))
    mo_cor = glob.glob("*BU2_RPI_3d.nii.gz")[0]
    os.system("3dTstat -mean -prefix BU2_RPI_3dv_3dT.nii.gz %s" %(mo_cor))
        # motion correction and get motion, movement and displacement parameters
    mean_mo_cor = glob.glob("*BU2_RPI_3dv_3dT.nii.gz")[0]
    os.system("3dvolreg -Fourier -twopass -base %s -zpad 4 -maxdisp1D BU2_RPI_3dvmd1D.1D\
                -1Dfile BU2_RPI_3dv1D.1D -prefix BU2_RPI_3dv.nii.gz %s" %(mean_mo_cor, rpi))


    # Create a brain only mask
    print ("Creating brain mask only...")
    motion_corrected = glob.glob("*BU2_RPI_3dv.nii.gz")[0]
    os.system("3dAutomask -prefix BU2_RPI_3dv_automask.nii.gz %s" %(motion_corrected))


    # Edge detect - remove skull
    print ("Detect edge and remove skull on %s" %(file))
    b = glob.glob("*BU2_RPI_3dv_automask.nii.gz")[0]
    os.system("3dcalc -a %s -b %s -expr %s -prefix BU2_RPI_3dv_3dc.nii.gz" %(motion_corrected,b,expr))


    # normalize image intensity values
    print("Normalizing image intensity values...")
    ins = glob.glob("*BU2_RPI_3dv_3dc.nii.gz")[0]
    os.system("fslmaths %s -ing 10000 BU2_RPI_3dv_3dc_maths.nii.gz -odt float" %(ins))


    # calculate mean of skull stripped image
    print("Calculate mean of skull stripped image...")
    os.system("3dTstat -mean -prefix BU2_RPI_3dv_3dc_3dT.nii.gz %s" %(ins))


    # create mask (generate mask from normalized intensity data)
    print ("Generating mask from normalized intensity data...")
    maths = glob.glob("*BU2_RPI_3dv_3dc_maths.nii.gz")[0]
    os.system("fslmaths %s -Tmin -bin BU2_RPI_3dv_3dc_maths_maths.nii.gz -odt char" %(maths))


    # Register functional to mni data - register a functional scan in native space to MNI standard rest_MNI_space
    print("Performing linear transformation on the functional data to anatomical...")
    ss = glob.glob("*stripped_T1.nii.gz")[0]
    func = glob.glob("*BU2_RPI_3dv_3dc.nii.gz")[0]
    os.system("flirt -in %s -ref %s -omat BU2_to_anat_linear.mat -out BU2_to_T1.nii.gz"%(func,ss))
        # do functional to mni space
    print ("Combining rest to T1 and T1 to MNI...")
    out = glob.glob("*BU2_to_anat_linear.mat")[0]
    t1_to_mni = glob.glob("*affine_transform.mat")[0]
    os.system("convert_xfm -omat BU2_mni_linear.mat -concat %s %s "%(t1_to_mni, out))
        # invert to get mni to funcional
    print("Inverting to get mni to functional data...")
    mat = glob.glob("*BU2_mni_linear.mat")[0]
    os.system("convert_xfm -omat mni_to_BU2_linear.mat -inverse %s"%(mat))
        # apply the warp to the data to get data from mni to functional native space
    print("Apply warp to get functional data in mni space")
    non_linear = glob.glob("*non_linear_tranf.nii.gz")[0]
    os.system("applywarp --in=%s --ref=%s --warp=%s --premat=%s --out=mni_to_BU2.nii.gz" %(func,template,non_linear,out))


    print("Smoothing...")
    data = glob.glob("*mni_to_BU2.nii.gz")[0]
    os.system("3dmerge -1blur_fwhm 6 -doall -prefix BU2_smoothed.nii.gz %s" %(data))

    print("De-mean motion parameters...")
    os.system("1d_tool.py -infile BU2_RPI_3dv1D.1D -set_nruns 1 -demean -write motion_demean.1D")
    print("Compute motion parameter derivaties...")
    os.system("1d_tool.py -infile BU2_RPI_3dv1D.1D -set_nruns 1 -derivative -demean -write motion_deriv.1D")
    #print("convert motion parameters for per run regression...")
    #os.system("1d_tool.py -infile motion_demean.1D -set_nruns 1 -split_into_pad_runs mot_demean")
    #os.system("1d_tool.py -infile motion_deriv.1D -set_nruns 1 -split_into_pad_runs mot_deriv")
    print("create censor file motion...")
    os.system("1d_tool.py -infile BU2_RPI_3dv1D.1D -set_nruns 1 -show_censor_count\
              -censor_prev_TR -censor_motion 0.2 motion_%s" %(n[0]))

    print ("Nuisance regression started...")
    csf_mask = glob.glob("*csf_mask.nii.gz")[0]
    wm_mask = glob.glob("*wm_mask.nii.gz")[0]
    print("resample the CSF and WM masks...")
    os.system("3dresample -master %s -inset %s -prefix csf_resampled.nii.gz" %(data, csf_mask))
    os.system("3dresample -master %s -inset %s -prefix wm_resampled.nii.gz" %(data, wm_mask))
        # extract time courses from wm and csf
        # extract time courses from wm and csf
    os.system("3dmaskave -q -mask csf_resampled.nii.gz %s > csf_tc_file.1D" %(data))
    os.system("3dmaskave -q -mask wm_resampled.nii.gz %s > wm_tc_file.1D" %(data))

    # Perform nuisance variable regression - remove motion parameters, csf and wm time courses
    data = glob.glob("*BU2_smoothed.nii.gz")[0]
    os.system("3dDeconvolve -input %s -censor motion_%s_censor.1D\
            -polort A -num_stimts 14\
            -stim_file 1 motion_demean.1D'[0]' -stim_base 1 -stim_label 1 roll_01 \
            -stim_file 2 motion_demean.1D'[1]' -stim_base 2 -stim_label 2 pitch_01 \
            -stim_file 3 motion_demean.1D'[2]' -stim_base 3 -stim_label 3 yaw_01 \
            -stim_file 4 motion_demean.1D'[3]' -stim_base 4 -stim_label 4 dS_01 \
            -stim_file 5 motion_demean.1D'[4]' -stim_base 5 -stim_label 5 dL_01 \
            -stim_file 6 motion_demean.1D'[5]' -stim_base 6 -stim_label 6 dP_01 \
            -stim_file 7 motion_deriv.1D'[0]' -stim_base 7 -stim_label 7 roll_02 \
            -stim_file 8 motion_deriv.1D'[1]' -stim_base 8 -stim_label 8 pitch_02 \
            -stim_file 9 motion_deriv.1D'[2]' -stim_base 9 -stim_label 9 yaw_02 \
            -stim_file 10 motion_deriv.1D'[3]' -stim_base 10 -stim_label 10 dS_02 \
            -stim_file 11 motion_deriv.1D'[4]' -stim_base 11 -stim_label 11 dL_02 \
            -stim_file 12 motion_deriv.1D'[5]' -stim_base 12 -stim_label 12 dP_02 \
            -stim_file 13 csf_tc_file.1D -stim_base 13 -stim_label 13 csf \
            -stim_file 14 wm_tc_file.1D -stim_base 14 -stim_label 14 wm \
            -fout -tout -x1D X.xmat.1D -xjpeg X.jpg\
            -x1D_uncensored X.nocensor.xmat.1D -fitts fitts.19 -errts errts.%s -x1D_stop -bucket stats.%s" %(data,n[0],n[0],n[0]))

    print("Start 3dTproject...")
    os.system("3dTproject -polort 0 -input %s -censor motion_%s_censor.1D -cenmode ZERO -ort X.nocensor.xmat.1D\
            -prefix BU2_FINAL.nii.gz" %(data,n[0]))
