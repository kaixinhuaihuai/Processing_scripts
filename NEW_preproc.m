%% Loop for going through separate folders
% add active current working directory and initiate spm
dbstop if error
clear all

addpath D:\PhD\MATLAB\spm12;
spm('Defaults','fMRI');
spm_jobman('initcfg');
spm fmri

% get the separate folders added as names
files = dir;
directoryNames = {files([files.isdir]).name};

%remove unnecesssary bits and pieces and prepare matlabbatch to run
directoryNames = directoryNames(~ismember(directoryNames,{'.','..'}));
matlabbatch{1}.cfg_basicio.file_dir.dir_ops.cfg_cd.dir = cellstr(cd);
spm_jobman('run',matlabbatch);
clear matlabbatch;

% if you want to loop only from 23 to 26 for example
% directoryNames = (3:end)

%get the number of folders/subjects you have to go through 
numberofFolders = numel(directoryNames);

% Start the loop
% for 1 to the number of folders you have
% this directory is the number of folder/subject you are on
% print which folder of how many you are working in currently
% EPIDir is the files in the current folder following nifti and convert
% subfolders
% display said image in there
% run the script

%%

for k = 2:numberofFolders
    thisDir = fullfile(directoryNames(k));
    fprintf('Processing folder %d of %d',k, numberofFolders)
    number = thisDir{1,1};
    cd (number);
    cd MBEPI_25iso_Belief_0005;
    EPIDir = pwd;
    
    
    % if you need to do bad slice repair activate these comments
    %repairedslices = dir('g*.*');
    %if ~isempty(repairedslices) == 1
    %    f = spm_select('FPList', fullfile(EPIDir), '^gf.*\.nii$');
    %else
    %    f = spm_select('FPList', fullfile(EPIDir), '^f.*\.nii$');
    %end
    f = spm_select('FPList', fullfile(EPIDir), '^f.*\.nii$'); % functional images
    s = spm_select('FPList', fullfile(EPIDir), '^s.*\.nii');  % structural images
    
    spm_figure('GetWin','Graphics')
    spm_image('Display', s)
    
   % First step - Realign and resclice
   % We are not using slice timing correction as per Poldrack's textbook -
   % practically not very helpful for TR smaller or equal to 2s, and
   % interleaved sequencing followed by spatial smoothing. The use of temporal derivatives
   % allows for some degree of timing misspecification and can reduce the impact of slice 
   % timing differences. Furthermore, motion correction is linked to
   % slice timing (the two affect each other and bias results depending on
   % processing order).
   
   % Step is performed without changing any defaults in SPM
    matlabbatch{1}.spm.spatial.realign.estwrite.data = cellstr(f);
   % matlabbatch{1}.spm.spatial.realign.estwrite.data{1} = cellstr(f);
    spm_jobman('run',matlabbatch);
    clear matlabbatch;
    
    % Motion adjustment using Art Repair
    ReslicedDir = EPIDir;
    ReslicedImages = spm_select('FPList', fullfile(EPIDir),'^r.*\.nii');
    RealignDir = EPIDir;
    RealignImages  = spm_select('FPList', fullfile(EPIDir), '^f.*\.nii$');
    art_motionregress( ReslicedDir, ReslicedImages, RealignDir, RealignImages);
        
    % Artifact repair using Art Repair and the motion corrected images 
    HeadMaskT = 4;
    RepairType = 2;
    Images = spm_select('FPList', fullfile(EPIDir),'^m.*\.nii');
    RFile = spm_select('FPList', fullfile(EPIDir), '^rp.*\.txt');
    art_global(Images, RFile, HeadMaskT, RepairType);
    
    % According to the textbook, the images need to be segmented and co-registered
    % prior to spatial normalization. We need to segment using bias field
    % correction (variations in the intesity of the image due to field
    % inhomogeneities, can affect the T1). SPM combines bias field
    % correction with tissue segmentation. 
    
    % Segmentation - using CAT12 defaults
    matlabbatch{1}.spm.tools.cat.estwrite.data = cellstr(s);
    matlabbatch{1}.spm.tools.cat.estwrite.output.warps = [1 0];  %forward deformantion field
    spm_jobman('run',matlabbatch);
    clear matlabbatch;
end
    
    
    
    
    