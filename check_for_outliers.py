#!/usr/bin/env python
"""
Check the motion parameters and the motion outliers for each task and each participant
"""
import os
import glob
import re


"""
LS GROUP!!!!!
"""

folders = ["Belief_Updating", "Resting", "Soc_Prob"]
print (folders)
for i in folders:
    if "Belief" in i:
        rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/%s/LS" %(i)  #change as necessary
        files = glob.glob("%s/sub-[0-2][0-9]/*parameters.nii.gz" %(rootdir))
        for file in files:
            path = os.path.split(file)
            out = path[0]
            name = path[1]
            os.chdir(out)
            n = re.findall("\d+", file)
            if "beliefup_run-1" in name:
                outliers_file = ("sub-%s_belief_up_run1_motion_outliers_FD.txt" %(n[0]))
                plot = ("sub-%s_belief_up_run1_motion_outliers_FD.png" %(n[0]))
                os.system ("fsl_motion_outliers -i \"%s\" -o \"%s\" -p \"%s\" --nomoco --fd -v" %(name, outliers_file, plot))
            if "beliefup_run-2" in name:
                outliers_file = ("sub-%s_belief_up_run2_motion_outliers_FD.txt" %(n[0]))
                plot = ("sub-%s_belief_up_run2_motion_outliers_FD.png" %(n[0]))
                os.system ("fsl_motion_outliers -i \"%s\" -o %s -p \"%s\" --nomoco --fd -v" %(name, outliers_file, plot))
    if "Resting" in i:
        rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/%s/LS" %(i)   #change as necessary
        files = glob.glob("%s/sub-[0-2][0-9]/*parameters.nii.gz" %(rootdir))
        for file in files:
            path = os.path.split(file)
            out = path[0]
            name = path[1]
            os.chdir(out)
            n = re.findall("\d+", file)
            outliers_file = ("sub-%s_rest_motion_outliers_FD.txt" %(n[0]))
            plot = ("sub-%s_rest_motion_outliers_FD.png" %(n[0]))
            os.system ("fsl_motion_outliers -i \"%s\" -o %s -p \"%s\" --nomoco --fd -v" %(name, outliers_file, plot))
    if "Soc_Prob" in i:
        rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/%s/LS" %(i)  #change as necessary
        files = glob.glob("%s/sub-[0-2][0-9]/*parameters.nii.gz" %(rootdir))
        for file in files:
            path = os.path.split(file)
            out = path[0]
            name = path[1]
            os.chdir(out)
            n = re.findall("\d+", file)
            outliers_file = ("sub-%s_soc_prob_motion_outliers_FD.txt" %(n[0]))
            plot = ("sub-%s_soc_prob_motion_outliers_FD.png" %(n[0]))
            os.system ("fsl_motion_outliers -i \"%s\" -o %s -p \"%s\" --nomoco --fd -v" %(name, outliers_file, plot))

"""
HS GROUP!!!!!
"""
for fol in folders:
    if "Belief" in fol:
        rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/%s/LS" %(fol)   #change as necessary
        files = glob.glob("%s/sub-[0-2][0-9]/func/*parameters.nii.gz" %(rootdir))
        for file in files:
            path = os.path.split(file)
            out = path[0]
            name = path[1]
            os.chdir(out)
            n = re.findall("\d+", file)
            if "beliefup_run-1" in name:
                outliers_file = ("sub-%s_belief_up_run1_motion_outliers_FD.txt" %(n[0]))
                plot = ("sub-%s_belief_up_run1_motion_outliers_FD.png" %(n[0]))
                os.system ("fsl_motion_outliers -i \"%s\" -o \"%s\" -p \"%s\" --nomoco --fd -v" %(name, outliers_file, plot))
            if "beliefup_run-2" in name:
                outliers_file = ("sub-%s_belief_up_run2_motion_outliers_FD.txt" %(n[0]))
                plot = ("sub-%s_belief_up_run2_motion_outliers_FD.png" %(n[0]))
                os.system ("fsl_motion_outliers -i \"%s\" -o %s -p \"%s\" --nomoco --fd -v" %(name, outliers_file, plot))
    if "Resting" in fol:
        rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/%s/LS" %(fol)  #change as necessary
        files = glob.glob("%s/sub-[0-2][0-9]/func/*parameters.nii.gz" %(rootdir))
        for file in files:
            path = os.path.split(file)
            out = path[0]
            name = path[1]
            os.chdir(out)
            n = re.findall("\d+", file)
            outliers_file = ("sub-%s_rest_motion_outliers_FD.txt" %(n[0]))
            plot = ("sub-%s_rest_motion_outliers_FD.png" %(n[0]))
            os.system ("fsl_motion_outliers -i \"%s\" -o %s -p \"%s\" --nomoco --fd -v" %(name, outliers_file, plot))
    if "Soc_Prob" in fol:
        rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/%s/LS" %(fol)  #change as necessary
        files = glob.glob("%s/sub-[0-2][0-9]/func/*parameters.nii.gz" %(rootdir))
        for file in files:
            path = os.path.split(file)
            out = path[0]
            name = path[1]
            os.chdir(out)
            n = re.findall("\d+", file)
            outliers_file = ("sub-%s_soc_prob_motion_outliers_FD.txt" %(n[0]))
            plot = ("sub-%s_soc_prob_motion_outliers_FD.png" %(n[0]))
            os.system ("fsl_motion_outliers -i \"%s\" -o %s -p \"%s\" --nomoco --fd -v" %(name, outliers_file, plot))
