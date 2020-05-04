%% FIRST LEVEL SOCIAL LEARNING TASK

dbstop if error
clear all

%% Specify paths
%initialise spm
addpath C:\Work\spm12
addpath C:\Work\spm12;
spm('Defaults','fMRI');
spm_jobman('initcfg');
%spm fmri

% get the separate folders added as names
files = dir;
directoryNames = {files([files.isdir]).name};

%remove unnecesssary bits and pieces and prepare matlabbatch to run
directoryNames = directoryNames(~ismember(directoryNames,{'.','..'}));
matlabbatch{1}.cfg_basicio.file_dir.dir_ops.cfg_cd.dir = cellstr(cd);
spm_jobman('run',matlabbatch);
clear matlabbatch;

%get the number of folders/subjects you have to go through 
numberofFolders = numel(directoryNames);

%% Loop through subjects
for k = 1:numberofFolders
    thisDir = fullfile(directoryNames(k));
    fprintf('Processing folder %d of %d',k, numberofFolders)
    number = thisDir{1,1};
    cd (number);
    cd MBEPI_25iso_Social_0009
    EPIDir = pwd;
    f = spm_select('FPList', fullfile(EPIDir), '^sw.*\.nii$');    % fully pre-processed functional images
    matlabbatch{1}.spm.stats.fmri_spec.dir = {};
    matlabbatch{1}.spm.stats.fmri_spec.timing.units = 'secs';
    matlabbatch{1}.spm.stats.fmri_spec.timing.RT = 2;
    matlabbatch{1}.spm.stats.fmri_spec.timing.fmri_t = 52;
    matlabbatch{1}.spm.stats.fmri_spec.timing.fmri_t0 = 26;
    matlabbatch{1}.spm.stats.fmri_spec.sess(1).scans = cellstr(f);
    
    cd ..
    cd Social_prob_1stlevel
    matlabbatch{1}.spm.stats.fmri_spec.dir = {pwd};
    rp = dir('*.txt');
    cond = dir('*conditions.mat');
    
    matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {}, 'orth', {});
    matlabbatch{1}.spm.stats.fmri_spec.sess(1).multi = {cond.name};
    matlabbatch{1}.spm.stats.fmri_spec.sess(1).regress = struct('name', {}, 'val', {});
    matlabbatch{1}.spm.stats.fmri_spec.sess(1).multi_reg = {rp.name};
    matlabbatch{1}.spm.stats.fmri_spec.sess(1).hpf = 128;
    matlabbatch{1}.spm.stats.fmri_spec.bases.hrf.derivs = [1 0];
    spm_jobman('run',matlabbatch);
    
    % Model estimation
    clear matlabbatch;

    matlabbatch{1}.spm.stats.fmri_est.spmmat = {'SPM.mat'};

    save(fullfile('Soc_prob'),'matlabbatch');
    spm_jobman('run',matlabbatch);
    
    % Results
    clear matlabbatch;

    matlabbatch{1}.spm.stats.con.spmmat = {'SPM.mat'};

    matlabbatch{1}.spm.stats.con.consess{1}.tcon.name = 'Outcome > Baseline';
    matlabbatch{1}.spm.stats.con.consess{1}.tcon.convec =[0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
    matlabbatch{1}.spm.stats.con.consess{1}.tcon.sessrep = 'none';
    matlabbatch{1}.spm.stats.con.consess{2}.tcon.name = 'CuexBelief_Precision_Advice> Baseline';
    matlabbatch{1}.spm.stats.con.consess{2}.tcon.convec =[0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
    matlabbatch{1}.spm.stats.con.consess{2}.tcon.sessrep = 'none';
    matlabbatch{1}.spm.stats.con.consess{3}.tcon.name = 'CuexBelief_Precision_Card> Baseline';
    matlabbatch{1}.spm.stats.con.consess{3}.tcon.convec =[0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
    matlabbatch{1}.spm.stats.con.consess{3}.tcon.sessrep = 'none';
    matlabbatch{1}.spm.stats.con.consess{4}.tcon.name = 'CuexVolatility> Baseline';
    matlabbatch{1}.spm.stats.con.consess{4}.tcon.convec =[0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
    matlabbatch{1}.spm.stats.con.consess{4}.tcon.sessrep = 'none';
    matlabbatch{1}.spm.stats.con.consess{5}.tcon.name = 'CuexVolatility_Card> Baseline';
    matlabbatch{1}.spm.stats.con.consess{5}.tcon.convec =[0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
    matlabbatch{1}.spm.stats.con.consess{5}.tcon.sessrep = 'none';
    matlabbatch{1}.spm.stats.con.consess{6}.tcon.name = 'OutcomexEpsilon2_Advice> Baseline';
    matlabbatch{1}.spm.stats.con.consess{6}.tcon.convec =[0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
    matlabbatch{1}.spm.stats.con.consess{6}.tcon.sessrep = 'none';
    matlabbatch{1}.spm.stats.con.consess{7}.tcon.name = 'OutcomexEpsilon2_Cue> Baseline';
    matlabbatch{1}.spm.stats.con.consess{7}.tcon.convec =[0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0];
    matlabbatch{1}.spm.stats.con.consess{7}.tcon.sessrep = 'none';
    matlabbatch{1}.spm.stats.con.consess{8}.tcon.name = 'OutcomexEpsilon3_Advice> Baseline';
    matlabbatch{1}.spm.stats.con.consess{8}.tcon.convec =[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0];
    matlabbatch{1}.spm.stats.con.consess{8}.tcon.sessrep = 'none';
    matlabbatch{1}.spm.stats.con.consess{9}.tcon.name = 'OutcomexEpsilon3_Cue> Baseline';
    matlabbatch{1}.spm.stats.con.consess{9}.tcon.convec =[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0];
    matlabbatch{1}.spm.stats.con.consess{9}.tcon.sessrep = 'none';
    
    spm_jobman('run',matlabbatch);
    clear matlabbatch;
    cd ..
    clear number;
    cd ..
end
