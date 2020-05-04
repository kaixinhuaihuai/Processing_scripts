%% This script analyses data for the Social_probabilistic task
% Does first-level analysis for indicated subjects
% NB READ THROGUGH THE COMMENTS!! THEY ARE HERE FOR A REASON!

% If unclear about any options in the script refer to the SPM GUI and it
% will give an indication of what/where/how needs to be changed.

% If any of the default SPM pre-processing settings need to be changed
% go to the SPM GUI and change from there then click View -> show .m code
% this will show you which part of the code changes respective of what you
% have changed, then change in the script as needed.

dbstop if error
clear all

%% Specify paths
%initialise spm
%addpath D:\PhD\MATLAB\spm12
%spm fmri;
spm('Defaults','fMRI');
spm_jobman('initcfg');

cd MBEPI_25iso_Social_0009;
EPIDir = pwd;
f = spm_select('FPList', fullfile(EPIDir), '^swvra.*\.nii$');    % fully pre-processed functional images

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Classical statistical analysis (CATEGORICAL)
% Remember to copy and paste the realignment regressors into the 
% BeliefUpdating_Run1 folder!!!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear matlabbatch; 
% Model specification
% CHANGE THE NUMBER OF THE FOLDER OF THE OUTPUT DIRECTORY!
% CHANGE THE NAMES OF THE MULTIPLE REGRESSOR MOVEMENT FILES!

matlabbatch{1}.spm.stats.fmri_spec.dir = {'G:\PhD\Trying Out Analysis\LS\08\BeliefUpdating_1stLevel\ByUpdate'};
matlabbatch{1}.spm.stats.fmri_spec.timing.units = 'secs';
matlabbatch{1}.spm.stats.fmri_spec.timing.RT = 2;
matlabbatch{1}.spm.stats.fmri_spec.timing.fmri_t = 52;
matlabbatch{1}.spm.stats.fmri_spec.timing.fmri_t0 = ceil(52/2);
matlabbatch{1}.spm.stats.fmri_spec.sess(1).scans = cellstr(f);

cd ..
cd BeliefUpdating_Run1


matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {}, 'orth', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(1).multi = {'conditionsFOR_PARAMETRICUPDATE_BY_UPDATE_session1.mat'};
matlabbatch{1}.spm.stats.fmri_spec.sess(1).regress = struct('name', {}, 'val', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(1).multi_reg = {'rp_af2019-02-27_09-18-093431-00001-00001-1.txt'};
matlabbatch{1}.spm.stats.fmri_spec.sess(1).hpf = 128;

cd ..
cd MBEPI_25iso_Belief_0006
f_sess2 = spm_select('FPList', fullfile(EPIDir), '^swvra.*\.nii$');    % fully pre-processed functional images
matlabbatch{1}.spm.stats.fmri_spec.sess(2).scans = cellstr(f_sess2);

cd ..
cd BeliefUpdating_run1

matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {}, 'orth', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(2).multi = {'conditionsFOR_PARAMETRICUPDATE_BY_UPDATE_session2.mat'};
matlabbatch{1}.spm.stats.fmri_spec.sess(2).regress = struct('name', {}, 'val', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(2).multi_reg = {'rp_af2019-02-27_09-18-094742-00001-00001-1.txt'};
matlabbatch{1}.spm.stats.fmri_spec.sess(2).hpf = 128;

matlabbatch{1}.spm.stats.fmri_spec.bases.hrf.derivs = [1 0];
spm_jobman('run',matlabbatch);
%% Model estimation
cd ..
cd beliefUpdating_1stLevel
cd ByUpdate
clear matlabbatch;

matlabbatch{1}.spm.stats.fmri_est.spmmat = {'SPM.mat'};

save(fullfile('spm_2nd_Update'),'matlabbatch');
spm_jobman('run',matlabbatch);

%% Results
clear matlabbatch;

matlabbatch{1}.spm.stats.con.spmmat = {'SPM.mat'};

matlabbatch{1}.spm.stats.con.consess{1}.tcon.name = '1stEstimate_Social>Baseline';
matlabbatch{1}.spm.stats.con.consess{1}.tcon.convec = [1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{1}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{2}.tcon.name = '1stEstimate_NonSocial>Baseline';
matlabbatch{1}.spm.stats.con.consess{2}.tcon.convec = [0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{2}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{3}.tcon.name = '1stEstimate_Social>NonSocial';
matlabbatch{1}.spm.stats.con.consess{3}.tcon.convec = [1	0	-1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	-1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{3}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{4}.tcon.name = '1stEstimate_NonSocial>Social';
matlabbatch{1}.spm.stats.con.consess{4}.tcon.convec = [-1	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	-1	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{4}.tcon.sessrep = 'none';


matlabbatch{1}.spm.stats.con.consess{5}.tcon.name = 'BR_Soc_Des>Baseline';
matlabbatch{1}.spm.stats.con.consess{5}.tcon.convec = [0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{5}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{6}.tcon.name = 'BR_Soc_Undes>Baseline';
matlabbatch{1}.spm.stats.con.consess{6}.tcon.convec = [0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{6}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{7}.tcon.name = 'BR_NonSoc_Des>Baseline';
matlabbatch{1}.spm.stats.con.consess{7}.tcon.convec = [0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{7}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{8}.tcon.name = 'BR_NonSoc_Undes>Baseline';
matlabbatch{1}.spm.stats.con.consess{8}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{8}.tcon.sessrep = 'none';


matlabbatch{1}.spm.stats.con.consess{9}.tcon.name = 'Update_Soc_Des>Baseline';
matlabbatch{1}.spm.stats.con.consess{9}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{9}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{10}.tcon.name = 'Update_Soc_Des_X_UpdateSizePM>Baseline';
matlabbatch{1}.spm.stats.con.consess{10}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{10}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{11}.tcon.name = 'Update_Soc_Undes>Baseline';
matlabbatch{1}.spm.stats.con.consess{11}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{11}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{12}.tcon.name = 'Update_Soc_Undes_X_UpdateSizePM>Baseline';
matlabbatch{1}.spm.stats.con.consess{12}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{12}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{13}.tcon.name = 'Update_NonSoc_Des>Baseline';
matlabbatch{1}.spm.stats.con.consess{13}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{13}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{14}.tcon.name = 'Update_NonSoc_Des_X_UpdateSizePM>Baseline';
matlabbatch{1}.spm.stats.con.consess{14}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{14}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{15}.tcon.name = 'Update_NonSoc_Undes>Baseline';
matlabbatch{1}.spm.stats.con.consess{15}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{15}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{16}.tcon.name = 'Update_NonSoc_Undes_X_UpdateSizePM>Baseline';
matlabbatch{1}.spm.stats.con.consess{16}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{16}.tcon.sessrep = 'none';


matlabbatch{1}.spm.stats.con.consess{17}.fcon.name = 'Social_vs_Nonsocial_Conditions';
matlabbatch{1}.spm.stats.con.consess{17}.fcon.convec = [0.2	0	-0.2	0	0.2	0	0.2	0	-0.2	0	-0.2	0	0.2	0	0	0	0.2	0	0	0	-0.2	0	0	0	-0.2	0	0	0	0	0	0	0	0	0	0.2	0	-0.2	0	0.2	0	0.2	0	-0.2	0	-0.2	0	0.2	0	0	0	0.2	0	0	0	-0.2	0	0	0	-0.2	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{17}.fcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{18}.fcon.name = 'Des_vs_Undes_BR';
matlabbatch{1}.spm.stats.con.consess{18}.fcon.convec = [0	0	0	0	0.5	 0	-0.5	0	0.5	 0	-0.5	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0.5	 0	-0.5	0	0.5  0	-0.5	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{18}.fcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{19}.fcon.name = 'Des_vs_Undes_Update';
matlabbatch{1}.spm.stats.con.consess{19}.fcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0.5	 0	0	0	-0.5	0	0	0	0.5  0	0	0	-0.5	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0.5  0	0	0	-0.5	0	0	0	0.5  0	0	0	-0.5	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{19}.fcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.delete = 0;

matlabbatch{2}.spm.stats.results.spmmat = {'SPM.mat'};  %invokes the contrast manager
matlabbatch{2}.spm.stats.results.conspec.titlestr = '';
matlabbatch{2}.spm.stats.results.conspec.contrasts = 1;
matlabbatch{2}.spm.stats.results.conspec.threshdesc = 'FWE';
matlabbatch{2}.spm.stats.results.conspec.thresh = 0.05;
matlabbatch{2}.spm.stats.results.conspec.extent = 0;
matlabbatch{2}.spm.stats.results.conspec.conjunction = 1;
matlabbatch{2}.spm.stats.results.conspec.mask.none = 1;
matlabbatch{2}.spm.stats.results.units = 1;
matlabbatch{2}.spm.stats.results.export{1}.ps = true;

spm_jobman('run',matlabbatch);

%% By BR
%Specify paths
%initialise spm

% Model Specification
clear matlabbatch
clear hReg, clear SPM, clear TabDat, clear xSPM

matlabbatch{1}.spm.stats.fmri_spec.dir = {'G:\PhD\Trying Out Analysis\LS\08\BeliefUpdating_1stLevel\ByBR'};
matlabbatch{1}.spm.stats.fmri_spec.timing.units = 'secs';
matlabbatch{1}.spm.stats.fmri_spec.timing.RT = 2;
matlabbatch{1}.spm.stats.fmri_spec.timing.fmri_t = 52;
matlabbatch{1}.spm.stats.fmri_spec.timing.fmri_t0 = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).scans = cellstr(f);

cd ..
cd ..
cd BeliefUpdating_Run1


matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {}, 'orth', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(1).multi = {'conditionsFOR_PARAMETRICUPDATE_BY_BASERATE_session1.mat'};
matlabbatch{1}.spm.stats.fmri_spec.sess(1).regress = struct('name', {}, 'val', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(1).multi_reg = {'rp_af2019-02-27_09-18-093431-00001-00001-1.txt'};
matlabbatch{1}.spm.stats.fmri_spec.sess(1).hpf = 128;

matlabbatch{1}.spm.stats.fmri_spec.sess(2).scans = cellstr(f_sess2);

cd ..
cd BeliefUpdating_run1

matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {}, 'orth', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(2).multi = {'conditionsFOR_PARAMETRICUPDATE_BY_BASERATE_session2.mat'};
matlabbatch{1}.spm.stats.fmri_spec.sess(2).regress = struct('name', {}, 'val', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(2).multi_reg = {'rp_af2019-02-27_09-18-094742-00001-00001-1.txt'};
matlabbatch{1}.spm.stats.fmri_spec.sess(2).hpf = 128;

matlabbatch{1}.spm.stats.fmri_spec.bases.hrf.derivs = [1 0];
spm_jobman('run',matlabbatch);
%% Model estimation
cd ..
cd BeliefUpdating_1stLevel
cd ByBR
clear matlabbatch;

matlabbatch{1}.spm.stats.fmri_est.spmmat = {'SPM.mat'};

save(fullfile('spm_BR'),'matlabbatch');
spm_jobman('run',matlabbatch);

%% Results
clear matlabbatch;

matlabbatch{1}.spm.stats.con.spmmat = {'SPM.mat'};

matlabbatch{1}.spm.stats.con.consess{1}.tcon.name = '1stEstimate_Social>Baseline';
matlabbatch{1}.spm.stats.con.consess{1}.tcon.convec = [1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{1}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{2}.tcon.name = '1stEstimate_NonSocial>Baseline';
matlabbatch{1}.spm.stats.con.consess{2}.tcon.convec = [0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{2}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{3}.tcon.name = '1stEstimate_Social>NonSocial';
matlabbatch{1}.spm.stats.con.consess{3}.tcon.convec = [1	0	-1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	-1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{3}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{4}.tcon.name = '1stEstimate_NonSocial>Social';
matlabbatch{1}.spm.stats.con.consess{4}.tcon.convec = [-1	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	-1	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{4}.tcon.sessrep = 'none';


matlabbatch{1}.spm.stats.con.consess{5}.tcon.name = 'BR_Soc_Des>Baseline';
matlabbatch{1}.spm.stats.con.consess{5}.tcon.convec = [0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{5}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{6}.tcon.name = 'BR_Soc_Des_X_UpdateSizePM>Baseline';
matlabbatch{1}.spm.stats.con.consess{6}.tcon.convec = [0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{6}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{7}.tcon.name = 'BR_Soc_Undes>Baseline';
matlabbatch{1}.spm.stats.con.consess{7}.tcon.convec = [0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{7}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{8}.tcon.name = 'BR_Soc_Undes_X_UpdateSizePM>Baseline';
matlabbatch{1}.spm.stats.con.consess{8}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{8}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{9}.tcon.name = 'BR_NonSoc_Des>Baseline';
matlabbatch{1}.spm.stats.con.consess{9}.tcon.convec = [0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{9}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{10}.tcon.name = 'BR_NonSoc_Des_X_UpdateSizePM>Baseline';
matlabbatch{1}.spm.stats.con.consess{10}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{10}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{11}.tcon.name = 'BR_NonSoc_Undes>Baseline';
matlabbatch{1}.spm.stats.con.consess{11}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{11}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{12}.tcon.name = 'BR_NonSoc_Undes_X_UpdateSizePM>Baseline';
matlabbatch{1}.spm.stats.con.consess{12}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{12}.tcon.sessrep = 'none';


matlabbatch{1}.spm.stats.con.consess{13}.tcon.name = 'Update_Soc_Des>Baseline';
matlabbatch{1}.spm.stats.con.consess{13}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{13}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{14}.tcon.name = 'Update_Soc_Undes>Baseline';
matlabbatch{1}.spm.stats.con.consess{14}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{14}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{15}.tcon.name = 'Update_NonSoc_Des>Baseline';
matlabbatch{1}.spm.stats.con.consess{15}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{15}.tcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{16}.tcon.name = 'Update_NonSoc_Undes>Baseline';
matlabbatch{1}.spm.stats.con.consess{16}.tcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{16}.tcon.sessrep = 'none';

matlabbatch{1}.spm.stats.con.consess{17}.fcon.name = 'Social_vs_Nonsocial_Conditions';
matlabbatch{1}.spm.stats.con.consess{17}.fcon.convec = [0.2	0	-0.2	0	0.2	0	0.2	0	-0.2	0	-0.2	0	0.2	0	0	0	0.2	0	0	0	-0.2	0	0	0	-0.2	0	0	0	0	0	0	0	0	0	0.2	0	-0.2	0	0.2	0	0.2	0	-0.2	0	-0.2	0	0.2	0	0	0	0.2	0	0	0	-0.2	0	0	0	-0.2	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{17}.fcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{18}.fcon.name = 'Des_vs_Undes_BR';
matlabbatch{1}.spm.stats.con.consess{18}.fcon.convec = [0	0	0	0	0.5	 0	-0.5	0	0.5	 0	-0.5	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0.5	 0	-0.5	0	0.5  0	-0.5	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{18}.fcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.consess{19}.fcon.name = 'Des_vs_Undes_Update';
matlabbatch{1}.spm.stats.con.consess{19}.fcon.convec = [0	0	0	0	0	0	0	0	0	0	0	0	0.5	 0	0	0	-0.5	0	0	0	0.5  0	0	0	-0.5	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0.5  0	0	0	-0.5	0	0	0	0.5  0	0	0	-0.5	0	0	0	0	0	0	0	0	0];
matlabbatch{1}.spm.stats.con.consess{19}.fcon.sessrep = 'none';
matlabbatch{1}.spm.stats.con.delete = 0;

matlabbatch{2}.spm.stats.results.spmmat = {'SPM.mat'};  %invokes the contrast manager
matlabbatch{2}.spm.stats.results.conspec.titlestr = '';
matlabbatch{2}.spm.stats.results.conspec.contrasts = 1;
matlabbatch{2}.spm.stats.results.conspec.threshdesc = 'FWE';
matlabbatch{2}.spm.stats.results.conspec.thresh = 0.05;
matlabbatch{2}.spm.stats.results.conspec.extent = 0;
matlabbatch{2}.spm.stats.results.conspec.conjunction = 1;
matlabbatch{2}.spm.stats.results.conspec.mask.none = 1;
matlabbatch{2}.spm.stats.results.units = 1;
matlabbatch{2}.spm.stats.results.export{1}.ps = true;

spm_jobman('run',matlabbatch);
