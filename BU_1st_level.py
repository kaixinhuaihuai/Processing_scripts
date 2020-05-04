# import needed python modules
import os
import glob

# the directory where all the sub## directories/all subject folders are
rootdir = "/media/phoenix/SeagateDrive/Dataset/LS"

# directory to place all the fsf files
fsfdir = "/media/phoenix/SeagateDrive/Dataset/Outputs/Belief_Updating/1st_level_design_files/LS"

# identify the fsf template file with wildcards created. Everything that needs to be changes has be
# identified as a wildcard in the template. I.e. subject number can be SUB, run/session number can be NUM
template = "/media/phoenix/SeagateDrive/Dataset/Outputs/Belief_Updating/template_1st_level.fsf"

# Get all paths for all nifti (identify all nifti files that need to go into the analysis)
subdirs = glob.glob("%s/sub-[0-9][0-9]/func/sub-[0-9][0-9]_task-beliefup_run-[0-9]_bold.nii.gz" %(rootdir))

for dir in list(subdirs):
    splitdir = dir.split("/")    # split the path to the file
    splitdir_run = splitdir[8]    # name of the nii file
    subnum = splitdir_run[4:6]   # number of the subject
    runnum = splitdir_run[-13]   # number of the run
    replacements = {"SUB":subnum,"RUN":runnum}    # replace the wildcards with the relevant info
    with open(template) as infile:
        with open("%s/design_sub-%s_run%s.fsf" %(fsfdir,subnum,runnum), "w") as outfile:
            for line in infile:
                for src,target in replacements.iteritems():
                    line=line.replace(src,target)
                outfile.write(line)
    print("%s/design_sub-%s_run%s.fsf" %(fsfdir,subnum,runnum))
    os.system("feat %s/design_sub-%s_run%s.fsf" %(fsfdir,subnum,runnum))
