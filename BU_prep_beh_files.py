#!/usr/bin/env python
import glob
import pandas as pd
import numpy as np
import re
import os

"""
Get the necessary numbers for the behavioral analysis of the BU Dataset
"""

rootdir = "/media/phoenix/SeagateDrive/Dataset/HS"
files = glob.glob("%s/sub-[0-2][0-9]/func/*run-1_events.csv" %(rootdir))


for file in files:
    print(file)
    n = re.findall("\d+", file)
    path = os.path.split(file)
    os.chdir(path[0])
    num = n[0]
    run2 = glob.glob("*run-2_events.csv")[0]
    data_run1 = pd.read_csv(file, usecols = ["trial_type","resp1","resp2","estimation_error"],sep = None)
    data_run2 = pd.read_csv(run2, usecols = ["trial_type","resp1","resp2","estimation_error"],sep = None)
    data = pd.concat([data_run1,data_run2],ignore_index = True)
    data["soc_pos"] = pd.Series([0]*62)
    data["soc_neg"] = pd.Series([0]*62)
    data["nonsoc_pos"] = pd.Series([0]*62)
    data["nonsoc_neg"] = pd.Series([0]*62)
    data["est_e_soc_pos"] = pd.Series([0]*62)
    data["est_e_soc_neg"] = pd.Series([0]*62)
    data["est_e_nons_pos"] = pd.Series([0]*62)
    data["est_e_nons_neg"] = pd.Series([0]*62)
    for index in data.index:
        if data["trial_type"][index] == 1.0:
            data["soc_pos"][index] = data["resp1"][index] - data["resp2"][index]
            data["est_e_soc_pos"][index] = data["estimation_error"][index]
        elif data["trial_type"][index] == 2.0:
            data["soc_neg"][index] = data["resp2"][index] - data["resp1"][index]
            data["est_e_soc_neg"][index] = data["estimation_error"][index]
        elif data["trial_type"][index] == 3.0:
            data["nonsoc_pos"][index] = data["resp1"][index] - data["resp2"][index]
            data["est_e_nons_pos"][index] = data["estimation_error"][index]
        elif data["trial_type"][index] == 4.0:
            data["nonsoc_neg"][index] = data["resp1"][index] - data["resp2"][index]
            data["est_e_nons_neg"][index] = data["estimation_error"][index]
    data["mean_soc_pos"] = data["soc_pos"].mean()
    data["mean_soc_neg"] = data["soc_neg"].mean()
    data["mean_nonsoc_pos"] = data["nonsoc_pos"].mean()
    data["mean_nonsoc_neg"] = data["nonsoc_neg"].mean()
    data["social_bias"] = data["mean_soc_pos"] - data["mean_soc_neg"]
    data["nonsocial_bias"] = data["mean_nonsoc_pos"] - data["mean_nonsoc_neg"]
    data["differential_soc_vs_nonsoc"] = data["social_bias"] - data["nonsocial_bias"]
    data["mean_ee_soc_pos"] = data["est_e_soc_pos"].mean()
    data["mean_ee_soc_neg"] = data["est_e_soc_neg"].mean()
    data["mean_ee_nons_pos"] = data["est_e_nons_pos"].mean()
    data["mean_ee_nons_neg"] = data["est_e_nons_neg"].mean()
    path = (r"%s/sub-%s/func/sub-%s_task-beliefup_Beh_data.csv" %(rootdir, num,num))
    data.to_csv(path, index = False, columns = ["trial_type","mean_soc_pos","mean_soc_neg","mean_nonsoc_pos",\
    "mean_nonsoc_neg","mean_ee_soc_pos","mean_ee_soc_neg","mean_ee_nons_pos","mean_ee_nons_neg"])
