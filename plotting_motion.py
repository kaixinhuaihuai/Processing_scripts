#!/usr/bin/env python
"""
Check the motion parameters and the motion outliers for each task and each participant
"""
import glob
import numpy as np
import matplotlib.pyplot as plt
import cv2
import keyboard

"""
BELIEF UPDATING
"""
rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/Belief_Updating/HS"  #change as necessary
images = glob.glob("%s/sub-[0-2][0-9]//*.png" %(rootdir))
files = glob.glob("%s/sub-[0-2][0-9]//*.par" %(rootdir))
BU_MS_HS = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/Beliefup_updating_motion_spikes_HS.txt"
BU_M_HS = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/Beliefup_updating_motion_HS.txt"

"""
Plot the outliers
"""
with open(BU_MS_HS, "a") as text:
    for im in images:
        print(im)
        img = cv2.imread(im)
        img = cv2.resize(img,(1028,373))
        cv2.imshow("image",img)
        cv2.waitKey(0)
        if keyboard.is_pressed("o"):
            text.write(im)
        cv2.destroyAllWindows()

with open(BU_M_HS, "a") as text:
    for file in files:
        par = np.loadtxt(file)
        fig, axes = plt.subplots(2,1,figsize=(15,5))
        axes[0].set_ylabel("rotation (radians)")
        axes[0].plot(par[0:,:3])
        axes[1].plot(par[0:,3:])
        axes[1].set_xlabel("time (TR)")
        axes[1].set_ylabel("translation (mm)")
        print(file)
        plt.plot()
        plt.waitforbuttonpress(0)
        if keyboard.is_pressed("o"):
            text.write(file)
        plt.close()


"""
RESTING
"""
rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/Resting/HS"  #change as necessary
images = glob.glob("%s/sub-[0-2][0-9]//*.png" %(rootdir))
files = glob.glob("%s/sub-[0-2][0-9]//*.par" %(rootdir))
Resting_MS_HS = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/Resting_motion_spikes_HS.txt"
Resting_M_HS = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/Resting_motion_HS.txt"


"""
Plot the outliers
"""
with open (Resting_MS_HS, "a") as text:
    for im in images:
        print(im)
        img = cv2.imread(im)
        img = cv2.resize(img,(1028,373))
        cv2.imshow("image",img)
        cv2.waitKey(0)
        if keyboard.is_pressed("o"):
            text.write(im)
        cv2.destroyAllWindows()


with open (Resting_M_HS, "a") as text:
    for file in files:
        par = np.loadtxt(file)
        fig, axes = plt.subplots(2,1,figsize=(15,5))
        axes[0].set_ylabel("rotation (radians)")
        axes[0].plot(par[0:,:3])
        axes[1].plot(par[0:,3:])
        axes[1].set_xlabel("time (TR)")
        axes[1].set_ylabel("translation (mm)")
        print(file)
        plt.plot()
        plt.waitforbuttonpress(0)
        if keyboard.is_pressed("o"):
            text.write(file)
        plt.close()


"""
SOC_PROB
"""
rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/Soc_Prob/HS"  #change as necessary
images = glob.glob("%s/sub-[0-2][0-9]//*.png" %(rootdir))
files = glob.glob("%s/sub-[0-2][0-9]//*.par" %(rootdir))
Soc_prob_MS_HS = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/Soc_Prob_motion_spikes_HS.txt"
Soc_prob_M_HS = "/media/phoenix/Seagate Backup Plus Drive/Dataset/Outputs/Soc_Prob_motion_HS.txt"


"""
Plot the outliers
"""
with open (Soc_prob_MS_HS, "a") as text:
    for im in images:
        print(im)
        img = cv2.imread(im)
        img = cv2.resize(img,(1028,373))
        cv2.imshow("image",img)
        cv2.waitKey(0)
        if keyboard.is_pressed("o"):
            text.write(im)
        cv2.destroyAllWindows()

with open (Soc_prob_M_HS, "a") as text:
    for file in files:
        par = np.loadtxt(file)
        fig, axes = plt.subplots(2,1,figsize=(15,5))
        axes[0].set_ylabel("rotation (radians)")
        axes[0].plot(par[0:,:3])
        axes[1].plot(par[0:,3:])
        axes[1].set_xlabel("time (TR)")
        axes[1].set_ylabel("translation (mm)")
        print(file)
        plt.plot()
        plt.waitforbuttonpress(0)
        if keyboard.is_pressed("o"):
            text.write(file)
        plt.close()
