#!/usr/bin/env python
import glob
import os
import re
import numpy as np
import pandas as pd
import csv


def get_event_pres(data,rootdir,num,run):
    onset_s = []
    dur_s = []
    onset_nons = []
    dur_nons =[]
    for index in data.index:
        if data["trial_type"][index] == 1.0 or data["trial_type"][index] == 2.0:
            onset_s.append(data["onset_event_presentation"][index])
            dur_s.append(data["duration_event"][index])
        if data["trial_type"][index] == 3.0 or data["trial_type"][index] == 4.0:
            onset_nons.append(data["onset_event_presentation"][index])
            dur_nons.append(data["duration_event"][index])
    soc = np.array([onset_s, dur_s],dtype = "int32")
    nonsoc = np.array([onset_nons, dur_nons],dtype = "int64")
    path1 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_event_pres_Social.txt" %(rootdir, num,num,run))
    path2 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_event_pres_Nonsocial.txt" %(rootdir, num,num,run))
    with open(path1, "w+") as f:
        np.savetxt(f, np.transpose(soc), fmt = "%1.3f")
    with open(path2, "w+") as f:
        np.savetxt(f, np.transpose(nonsoc),fmt = "%1.3f")


def get_1st_est(data,rootdir,num,run):
    onset_1st_s_p = []
    onset_1st_s_n = []
    onset_1st_nons_p = []
    onset_1st_nons_n = []
    dur_s_p =[]
    dur_s_n = []
    dur_nons_p = []
    dur_nons_n = []
    for index in data.index:
        if data["trial_type"][index] == 1.0:
            onset_1st_s_p.append(data["onset_cue_presentation"][index])
            dur_s_p.append(data["duration_cue_presentation"][index])
        if data["trial_type"][index] == 2.0:
            onset_1st_s_n.append(data["onset_cue_presentation"][index])
            dur_s_n.append(data["duration_cue_presentation"][index])
        if data["trial_type"][index] == 3.0:
            onset_1st_nons_p.append(data["onset_cue_presentation"][index])
            dur_nons_p.append(data["duration_cue_presentation"][index])
        if data["trial_type"][index] == 4.0:
            onset_1st_nons_n.append(data["onset_cue_presentation"][index])
            dur_nons_n.append(data["duration_cue_presentation"][index])
    first_s_p = np.array([onset_1st_s_p, dur_s_p],dtype = "int32")
    first_s_n = np.array([onset_1st_s_n, dur_s_n],dtype = "int32")
    first_nons_p = np.array([onset_1st_nons_p,dur_nons_p],dtype = "int32")
    first_nons_n = np.array([onset_1st_nons_n,dur_nons_n],dtype = "int32")
    path1 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_1st_soc_pos.txt" %(rootdir, num,num,run))
    path2 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_1st_soc_neg.txt" %(rootdir, num,num,run))
    path3 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_1st_nons_pos.txt" %(rootdir, num,num,run))
    path4 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_1st_nons_neg.txt" %(rootdir, num,num,run))
    with open(path1, "w+") as f:
        np.savetxt(f, np.transpose(first_s_p), fmt = "%1.3f")
    with open(path2, "w+") as f:
        np.savetxt(f, np.transpose(first_s_n), fmt = "%1.3f")
    with open(path3, "w+") as f:
        np.savetxt(f, np.transpose(first_nons_p), fmt = "%1.3f")
    with open(path4, "w+") as f:
        np.savetxt(f, np.transpose(first_nons_n), fmt = "%1.3f")


def get_BR_est(data,rootdir,num,run):
    onset_s_p = []
    onset_s_n = []
    onset_nons_p =[]
    onset_nons_n = []
    dur_s_p = []
    dur_s_n = []
    dur_nons_p = []
    dur_nons_n = []
    #up_s_p = []
    #up_s_n =[]
    #up_ns_p = []
    #up_ns_n = []
    ee_s_p =[]
    ee_s_n = []
    ee_nons_p = []
    ee_nons_n =[]
    for index in data.index:
        if data["trial_type"][index] == 1.0:
            onset_s_p.append(data["onset_BR_presentation"][index])
            dur_s_p.append(data["duration_BR_presentation"][index])
            ee_s_p.append(data["estimation_error"][index])
        if data["trial_type"][index] == 2.0:
            onset_s_n.append(data["onset_BR_presentation"][index])
            dur_s_n.append(data["duration_BR_presentation"][index])
            ee_s_n.append(data["estimation_error"][index])
        if data["trial_type"][index] == 3.0:
            onset_nons_p.append(data["onset_BR_presentation"][index])
            dur_nons_p.append(data["duration_BR_presentation"][index])
            ee_nons_p.append(data["estimation_error"][index])
        if data["trial_type"][index] == 4.0:
            onset_nons_n.append(data["onset_BR_presentation"][index])
            dur_nons_n.append(data["duration_BR_presentation"][index])
            ee_nons_n.append(data["estimation_error"][index])
    pm_ee_s_p = np.array([onset_s_p,dur_s_p,ee_s_p],dtype = "int32")
    pm_ee_s_n = np.array([onset_s_n,dur_s_n,ee_s_n],dtype = "int32")
    pm_ee_nons_p = np.array([onset_nons_p,dur_nons_p, ee_nons_p],dtype = "int32")
    pm_ee_nons_n = np.array([onset_nons_n,dur_nons_n,ee_nons_n],dtype = "int32")
    path1 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_PM_EE_Soc_pos.txt" %(rootdir, num,num,run))
    path2 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_PM_EE_soc_neg.txt" %(rootdir, num,num,run))
    path3 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_PM_EE_nons_pos.txt" %(rootdir, num,num,run))
    path4 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_PM_EE_nons_n.txt" %(rootdir, num,num,run))
    with open(path1, "w+") as f:
        np.savetxt(f, np.transpose(pm_ee_s_p), fmt = "%1.3f")
    with open(path2, "w+") as f:
        np.savetxt(f, np.transpose(pm_ee_s_n), fmt = "%1.3f")
    with open(path3, "w+") as f:
        np.savetxt(f, np.transpose(pm_ee_nons_p), fmt = "%1.3f")
    with open(path4, "w+") as f:
        np.savetxt(f, np.transpose(pm_ee_nons_n), fmt = "%1.3f")


def get_2nd_est(data,rootdir,num,run):
    onset_2nd_s_p = []
    onset_2nd_s_n = []
    onset_2nd_nons_p = []
    onset_2nd_nons_n = []
    dur_s_p =[]
    dur_s_n = []
    dur_nons_p = []
    dur_nons_n = []
    for index in data.index:
        if data["trial_type"][index] == 1.0:
            onset_2nd_s_p.append(data["onset_second_cue_presentation"][index])
            dur_s_p.append(data["duration_second_cue_presentation"][index])
        if data["trial_type"][index] == 2.0:
            onset_2nd_s_n.append(data["onset_second_cue_presentation"][index])
            dur_s_n.append(data["duration_second_cue_presentation"][index])
        if data["trial_type"][index] == 3.0:
            onset_2nd_nons_p.append(data["onset_second_cue_presentation"][index])
            dur_nons_p.append(data["duration_second_cue_presentation"][index])
        if data["trial_type"][index] == 4.0:
            onset_2nd_nons_n.append(data["onset_second_cue_presentation"][index])
            dur_nons_n.append(data["duration_second_cue_presentation"][index])
    second_s_p = np.array([onset_2nd_s_p, dur_s_p],dtype = "int32")
    second_s_n = np.array([onset_2nd_s_n, dur_s_n],dtype = "int32")
    second_nons_p = np.array([onset_2nd_nons_p,dur_nons_p],dtype = "int32")
    second_nons_n = np.array([onset_2nd_nons_n,dur_nons_n],dtype = "int32")
    path1 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_2nd_soc_pos.txt" %(rootdir, num,num,run))
    path2 = (r"%s/sub-%------s/func/sub-%s_task-beliefup_%s_2nd_soc_neg.txt" %(rootdir, num,num,run))
    path3 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_2nd_nons_pos.txt" %(rootdir, num,num,run))
    path4 = (r"%s/sub-%s/func/sub-%s_task-beliefup_%s_2nd_nons_neg.txt" %(rootdir, num,num,run))
    with open(path1, "w+") as f:
        np.savetxt(f, np.transpose(second_s_p), fmt = "%1.3f")
    with open(path2, "w+") as f:
        np.savetxt(f, np.transpose(second_s_n), fmt = "%1.3f")
    with open(path3, "w+") as f:
        np.savetxt(f, np.transpose(second_nons_p), fmt = "%1.3f")
    with open(path4, "w+") as f:
        np.savetxt(f, np.transpose(second_nons_n), fmt = "%1.3f")


rootdir = "/media/phoenix/SeagateDrive/Dataset/HS"
files_run1 = glob.glob("%s/sub-[0-2][0-9]/func/*run-1_events.csv" %(rootdir))
files_run2 = glob.glob("%s/sub-[0-2][0-9]/func/*run-2_events.csv" %(rootdir))

for file in files_run1:
    # cd into the file directory and get the file name
    n = re.findall("\d+", file)
    num = n[0]
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]
    print(file)
    print(name)
    data = pd.read_csv(file, sep = None)
    # first regressor - 1est estimate social
    get_event_pres(data,rootdir,num,"run1")
    get_1st_est(data,rootdir,num,"run1")
    get_BR_est(data,rootdir,num,"run1")
    get_2nd_est(data,rootdir,num,"run1")

for file in files_run2:
    # cd into the file directory and get the file name
    n = re.findall("\d+", file)
    num = n[0]
    path = os.path.split(file)
    os.chdir(path[0])
    name = path[1]
    print(file)
    print(name)
    data = pd.read_csv(file, sep = None)
    # first regressor - 1est estimate social
    get_event_pres(data,rootdir,num,"run2")
    get_1st_est(data,rootdir,num,"run2")
    get_BR_est(data,rootdir,num,"run2")
    get_2nd_est(data,rootdir,num,"run2")
