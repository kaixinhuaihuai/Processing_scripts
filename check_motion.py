#!/usr/bin/env python
"""
Check the motion parameters and the motion outliers for each task and each participant
"""
import os
import glob
import re

"""
Run the analyses for all files
LS GROUP!!!!!
"""
rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/LS"  #change as necessary
files = glob.glob("%s/sub-[0-2][0-9]/func/*bold.nii.gz" %(rootdir))
out_dir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs"

for file in list(files):
    if "beliefup_run-1" in file:
        n = re.findall("\d+", file)
        folder = "Belief_Updating"
        out_file = ("%s/%s/LS/sub-%s/sub-%s_belief_up_run1_motion_parameters" %(out_dir, folder, n[0], n[0]))
        os.system ("mcflirt -in \"%s\" -o \"%s\" -cost normcorr -plots -stages 3 -sinc_final -report" %(file, out_file))
    if "beliefup_run-2" in file:
         n = re.findall("\d+", file)
         folder = "Belief_Updating"
         out_file = ("%s/%s/LS/sub-%s/sub-%s_belief_up_run2_motion_parameters" %(out_dir, folder, n[0], n[0]))
         os.system ("mcflirt -in \"%s\" -o \"%s\" -cost normcorr -plots -stages 3 -sinc_final -report" %(file, out_file))
    if "rest" in file:
        n = re.findall("\d+", file)
        folder = "Resting"
        out_file = ("%s/%s/LS/sub-%s/sub-%s_rest_motion_parameters" %(out_dir, folder, n[0], n[0]))
        os.system ("mcflirt -in \"%s\" -o \"%s\" -cost normcorr -plots -stages 3 -sinc_final -report" %(file, out_file))
    if "soc_prob" in file:
         n = re.findall("\d+", file)
         folder = "Soc_Prob"
         out_file = ("%s/%s/LS/sub-%s/sub-%s_soc_prob_motion_parameters" %(out_dir, folder, n[0], n[0]))
         os.system ("mcflirt -in \"%s\" -o \"%s\" -cost normcorr -plots -stages 3 -sinc_final -report" %(file, out_file))

"""
Run the analyses for all files
HS GROUP!!!!
"""

rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/HS"  #change as necessary
files = glob.glob("%s/sub-[0-2][0-9]/func/*bold.nii.gz" %(rootdir))
out_dir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs"

for file in list(files):
    if "beliefup_run-1" in file:
        n = re.findall("\d+", file)
        folder = "Belief_Updating"
        out_file = ("%s/%s/HS/sub-%s/sub-%s_belief_up_run1_motion_parameters" %(out_dir, folder, n[0], n[0]))
        os.system ("mcflirt -in \"%s\" -o \"%s\" -cost normcorr -plots -stages 3 -sinc_final -report" %(file, out_file))
    if "beliefup_run-2" in file:
         n = re.findall("\d+", file)
         folder = "Belief_Updating"
         out_file = ("%s/%s/HS/sub-%s/sub-%s_belief_up_run2_motion_parameters" %(out_dir, folder, n[0], n[0]))
         os.system ("mcflirt -in \"%s\" -o \"%s\" -cost normcorr -plots -stages 3 -sinc_final -report" %(file, out_file))
    if "rest" in file:
        n = re.findall("\d+", file)
        folder = "Resting"
        out_file = ("%s/%s/HS/sub-%s/sub-%s_rest_motion_parameters" %(out_dir, folder, n[0], n[0]))
        os.system ("mcflirt -in \"%s\" -o \"%s\" -cost normcorr -plots -stages 3 -sinc_final -report" %(file, out_file))
    if "soc_prob" in file:
         n = re.findall("\d+", file)
         folder = "Soc_Prob"
         out_file = ("%s/%s/HS/sub-%s/sub-%s_soc_prob_motion_parameters" %(out_dir, folder, n[0], n[0]))
         os.system ("mcflirt -in \"%s\" -o \"%s\" -cost normcorr -plots -stages 3 -sinc_final -report" %(file, out_file))
