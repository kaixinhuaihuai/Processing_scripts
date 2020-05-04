#!/usr/bin/env python
import glob
import os
import re
import shutil


# Set up the required pathways and files

skull_template = "/usr/local/fsl/data/standard/MNI152_T1_2mm_brain.nii.gz"
template = "/usr/local/fsl/data/standard/MNI152_T1_2mm_brain.nii.gz"
ref_mask = "/usr/local/fsl/data/standard/MNI152_T1_2mm_brain_mask_dil.nii.gz"
cnf = "/usr/local/fsl/etc/flirtsch/T1_2_MNI152_2mm.cnf"
expr = "step(a-.99)"
Prior_CSF = "/usr/local/fsl/data/standard/tissuepriors/avg152T1_csf.hdr"
Prior_WM = "/usr/local/fsl/data/standard/tissuepriors/avg152T1_white.hdr"
Prior_GM = "/usr/local/fsl/data/standard/tissuepriors/avg152T1_gray.hdr"


"""
Preprocess T1 scans using AFNI and FSL.
The script runs the following: deoblique, reorient into RPI, skull strip, normlise to 2mm MNI space using first linear,
then nonlinear. Segment and create GM, WM and CSF masks.
"""

"""
LS GROUP!!!!
"""

rootdir = "/media/phoenix/SeagateDrive/Dataset/LS"
files = glob.glob("%s/sub-[0-2][0-9]/anat/*T1w.nii.gz" %(rootdir))

for file in files:
    print(file)
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
    print(os.getcwd())
    name = path[1]
    print(name)
    #  deoblique and reorient using AFNI
    os.system("3drefit -deoblique %s" %(name))
    print ("reorientating %s" %(file))
    os.system("3dresample -orient RPI -prefix reoriented_T1.nii.gz -inset %s" %(name))

    # skull strip the reorientated file uding AFNI
    t1_rpi = glob.glob("*reoriented_T1.nii.gz")[0]         # reorientated image is input for skillstripping
    print("Start skullstripping %s" %(file))
    os.system("3dSkullStrip -orig_vol -input %s -prefix skull_stripped_T1.nii.gz" %(t1_rpi))



    # Register to MNI space
        # use flirt to perform an affine transformation from T1 to MNI as a starting point
    print("Starting linear transformation on %s" %(file))
    ss = glob.glob("*stripped_T1.nii.gz")[0]                # ss is the skull stripped T1
    os.system("flirt -in %s -ref %s -out linear_t1_2_mni.nii.gz -omat affine_transform.mat" %(ss, template))

        # invert the affine transformation (we had t1 to mni affine, now we will get affine transformation from mni to t1)
    print ("Invert affine transformation...")
    affine = glob.glob("*affine_transform.mat")[0]
    os.system("convert_xfm -omat mni_to_t1.mat -inverse %s" %(affine))

        # refine registration by applying non-linear transformation
    print ("Starting non-linear transformation on %s" %(file))
    os.system("fnirt --in=%s --ref=%s --refmask=%s --config=%s\
                --aff=%s --cout=non_linear_t1_to_mni.nii.gz" %(t1_rpi, skull_template, ref_mask, cnf, affine))

        # apply non-linear transformation to the skull stripped image to normalise it into skull stripped MNI space
    print("Apply non-linear warp on the data on %s" %(file))
    nonlinear_xfm = glob.glob("*non_linear_t1_to_mni.nii.gz")[0]
    os.system("applywarp --in=%s --warp=%s --ref=%s --out=norm_T1.nii.gz" %(ss,nonlinear_xfm,template))



    # segment using FSL
    ss = glob.glob("*stripped_T1.nii.gz")[0]                # ss is the skull stripped T1
    print("Segmenting %s" %(file))
    out = "segmented_T1w.nii.gz"
    os.system("fast -S 1 -t 1 -g -p -n 3 -o segmented_T1w.nii.gz %s" %(ss))



    # create CSF mask
        # register csf template in template space to t1 space
    print("Creating csf mask for %s" %(file))
    invert = glob.glob("*mni_to_t1.mat")[0]
    os.system("flirt -in %s -ref %s -applyxfm -init %s -out csf_mni_2_t1.nii.gz" %(Prior_CSF, ss, invert))

        # find overlap between csf probability map and csf mni to t1
    in_csf_file = glob.glob("*pve_0.nii.gz")[0]
    csf_mni_t1 = glob.glob("*csf_mni_2_t1.nii.gz")[0]
    os.system("fslmaths %s -mas %s csf_combo.nii.gz" %(in_csf_file, csf_mni_t1))

        # threshold and binarize CSF probability map
    combo = glob.glob("*csf_combo.nii.gz")[0]
    os.system("fslmaths %s -thr 0.4 -bin csf_bin.nii.gz" %(combo))

        # generate csf mask by applying csf prior in t1 space to binarized csf probability map
    bin = glob.glob("*csf_bin.nii.gz")[0]
    os.system("fslmaths %s -mas %s csf_mask.nii.gz" %(bin, csf_mni_t1))



    # create WM mask
        # register wm template in template space to t1 space
    print("Creating wm mask for %s" %(file))
    os.system("flirt -in %s -ref %s -applyxfm -init %s -out wm_mni_2_t1.nii.gz" %(Prior_WM, ss, invert))

        # find overlap between wm probability map and wm mni to t1
    in_wm_file = glob.glob("*pve_2.nii.gz")[0]
    wm_mni_t1 = glob.glob("*wm_mni_2_t1.nii.gz")[0]
    os.system("fslmaths %s -mas %s wm_combo.nii.gz" %(in_wm_file, wm_mni_t1))

        # threshold and binarize WM probability map
    combo_wm = glob.glob("*wm_combo.nii.gz")[0]
    os.system("fslmaths %s -thr 0.4 -bin wm_bin.nii.gz" %(combo_wm))

        # generate wm mask by applying wm prior in t1 space to binarized wm probability map
    bin_wm = glob.glob("*wm_bin.nii.gz")[0]
    os.system("fslmaths %s -mas %s wm_mask.nii.gz" %(bin_wm, wm_mni_t1))



    # create GM mask
        # register GM template in template space to t1 space
    print("Creating GM mask for %s" %(file))
    os.system("flirt -in %s -ref %s -applyxfm -init %s -out gm_mni_2_t1.nii.gz" %(Prior_GM, ss, invert))

        # find overlap between gm probability map and gm mni to t1
    in_gm_file = glob.glob("*pve_1.nii.gz")[0]
    gm_mni_t1 = glob.glob("*gm_mni_2_t1.nii.gz")[0]
    os.system("fslmaths %s -mas %s gm_combo.nii.gz" %(in_gm_file, gm_mni_t1))

        # threshold and binarize CSF probability map
    combo_gm = glob.glob("*gm_combo.nii.gz")[0]
    os.system("fslmaths %s -thr 0.4 -bin gm_bin.nii.gz" %(combo_gm))

        # generate gm mask by applying gm prior in t1 space to binarized gm probability map
    bin_gm = glob.glob("*gm_bin.nii.gz")[0]
    os.system("fslmaths %s -mas %s gm_mask.nii.gz" %(bin_gm, gm_mni_t1))


"""
HS GROUP
"""
rootdir = "/media/phoenix/Seagate Backup Plus Drive/Dataset/HS/"
files = glob.glob("%s/sub-[0-2][0-9]/anat/*T1w.nii.gz" %(rootdir))

for file in files:
    print(file)
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

    #  deoblique and reorient using AFNI
    os.system("3drefit -deoblique %s" %(name))
    print ("reorientating %s" %(file))
    os.system("3dresample -orient RPI -prefix reoriented_T1.nii.gz -inset %s" %(name))

    # skull strip the reorientated file uding AFNI
    t1_rpi = glob.glob("*reoriented_T1.nii.gz")[0]         # reorientated image is input for skillstripping
    print("Start skullstripping %s" %(file))
    os.system("3dSkullStrip -orig_vol -input %s -prefix skull_stripped_T1.nii.gz" %(t1_rpi))



    # Register to MNI space
        # use flirt to perform an affine transformation from T1 to MNI as a starting point
    print("Starting linear transformation on %s" %(file))
    ss = glob.glob("*stripped_T1.nii.gz")[0]                # ss is the skull stripped T1
    os.system("flirt -in %s -ref %s -out linear_t1_2_mni.nii.gz -omat affine_transform.mat" %(ss, template))

        # invert the affine transformation (we had t1 to mni affine, now we will get affine transformation from mni to t1)
    print ("Invert affine transformation...")
    affine = glob.glob("*affine_transform.mat")[0]
    os.system("convert_xfm -omat mni_to_t1.mat -inverse %s" %(affine))

        # refine registration by applying non-linear transformation
    print ("Starting non-linear transformation on %s" %(file))
    os.system("fnirt --in=%s --ref=%s --refmask=%s --config=%s\
                --aff=%s --cout=non_linear_t1_to_mni.nii.gz" %(t1_rpi, skull_template, ref_mask, cnf, affine))

        # apply non-linear transformation to the skull stripped image to normalise it into skull stripped MNI space
    print("Apply non-linear warp on the data on %s" %(file))
    nonlinear_xfm = glob.glob("*non_linear_t1_to_mni.nii.gz")[0]
    os.system("applywarp --in=%s --warp=%s --ref=%s --out=norm_T1.nii.gz" %(ss,nonlinear_xfm,template))



    # segment using FSL
    ss = glob.glob("*stripped_T1.nii.gz")[0]                # ss is the skull stripped T1
    print("Segmenting %s" %(file))
    out = "segmented_T1w.nii.gz"
    os.system("fast -S 1 -t 1 -g -p -n 3 -o segmented_T1w.nii.gz %s" %(ss))



    # create CSF mask
        # register csf template in template space to t1 space
    print("Creating csf mask for %s" %(file))
    invert = glob.glob("*mni_to_t1.mat")[0]
    os.system("flirt -in %s -ref %s -applyxfm -init %s -out csf_mni_2_t1.nii.gz" %(Prior_CSF, ss, invert))

        # find overlap between csf probability map and csf mni to t1
    in_csf_file = glob.glob("*pve_0.nii.gz")[0]
    csf_mni_t1 = glob.glob("*csf_mni_2_t1.nii.gz")[0]
    os.system("fslmaths %s -mas %s csf_combo.nii.gz" %(in_csf_file, csf_mni_t1))

        # threshold and binarize CSF probability map
    combo = glob.glob("*csf_combo.nii.gz")[0]
    os.system("fslmaths %s -thr 0.4 -bin csf_bin.nii.gz" %(combo))

        # generate csf mask by applying csf prior in t1 space to binarized csf probability map
    bin = glob.glob("*csf_bin.nii.gz")[0]
    os.system("fslmaths %s -mas %s csf_mask.nii.gz" %(bin, csf_mni_t1))



    # create WM mask
        # register wm template in template space to t1 space
    print("Creating wm mask for %s" %(file))
    os.system("flirt -in %s -ref %s -applyxfm -init %s -out wm_mni_2_t1.nii.gz" %(Prior_WM, ss, invert))

        # find overlap between wm probability map and wm mni to t1
    in_wm_file = glob.glob("*pve_2.nii.gz")[0]
    wm_mni_t1 = glob.glob("*wm_mni_2_t1.nii.gz")[0]
    os.system("fslmaths %s -mas %s wm_combo.nii.gz" %(in_wm_file, wm_mni_t1))

        # threshold and binarize WM probability map
    combo_wm = glob.glob("*wm_combo.nii.gz")[0]
    os.system("fslmaths %s -thr 0.4 -bin wm_bin.nii.gz" %(combo_wm))

        # generate wm mask by applying wm prior in t1 space to binarized wm probability map
    bin_wm = glob.glob("*wm_bin.nii.gz")[0]
    os.system("fslmaths %s -mas %s wm_mask.nii.gz" %(bin_wm, wm_mni_t1))



    # create GM mask
        # register GM template in template space to t1 space
    print("Creating GM mask for %s" %(file))
    os.system("flirt -in %s -ref %s -applyxfm -init %s -out gm_mni_2_t1.nii.gz" %(Prior_GM, ss, invert))

        # find overlap between gm probability map and gm mni to t1
    in_gm_file = glob.glob("*pve_1.nii.gz")[0]
    gm_mni_t1 = glob.glob("*gm_mni_2_t1.nii.gz")[0]
    os.system("fslmaths %s -mas %s gm_combo.nii.gz" %(in_gm_file, gm_mni_t1))

        # threshold and binarize CSF probability map
    combo_gm = glob.glob("*gm_combo.nii.gz")[0]
    os.system("fslmaths %s -thr 0.4 -bin gm_bin.nii.gz" %(combo_gm))

        # generate gm mask by applying gm prior in t1 space to binarized gm probability map
    bin_gm = glob.glob("*gm_bin.nii.gz")[0]
    os.system("fslmaths %s -mas %s gm_mask.nii.gz" %(bin_gm, gm_mni_t1))
