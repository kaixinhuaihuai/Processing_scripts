import os
import glob
from nipype.interfaces.fsl import Merge

def getonefile(files, name):
    merger = Merge()
    merger.inputs.in_files = files
    merger.inputs.dimension = "t"
    merger.inputs.tr = 2.00
    merger.inputs.output_type = "NIFTI_GZ"
    merger.inputs.merged_file = "/media/phoenix/SeagateDrive/Dataset/Outputs/Belief_Updating/Higher_level_inputs/%s.nii.gz" %(name)
    merger.run()


# # get the directories
# rootdirHS = "/media/phoenix/SeagateDrive/Dataset/Outputs/Belief_Updating/HS/Second_level/1st_step/HS/"
# rootdirLS = "/media/phoenix/SeagateDrive/Dataset/Outputs/Belief_Updating/LS/Second_level/1st_step/LS/"
#
#
# for i in range (1,21):
#     contrast_hs = glob.glob("%s/[0-2][0-9].gfeat/cope%s.feat/stats/cope1.nii.gz" %(rootdirHS,i))
#     contrast_ls = glob.glob("%s/[0-2][0-9].gfeat/cope%s.feat/stats/cope1.nii.gz" %(rootdirLS,i))
#     files = contrast_hs + contrast_ls
#     print(files)
#     assert len(files) == 47
#     getonefile(files, i)


os.chdir("/media/phoenix/SeagateDrive/Dataset/Outputs/Belief_Updating/Higher_level_inputs/")
files = glob.glob("*.nii.gz")

for file in files:
    name = file.strip(".nii.gz")
    print(name)
    print("Running randomise on %s with name %s" %(file,name))
    os.system("randomise -i %s -o %s -d Template.mat -t Template.con\
         -m /usr/local/fsl/data/standard/MNI152_T1_2mm_brain -n 10000 -T" %(file,name))
