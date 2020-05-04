function questionnaires(options)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
S = uiimport(options.questionnaires);
[SOSTY_par]      = SOSTY_load_parameters(options);
[SOSTY_zeta]     = SOSTY_load_zeta(options);

%% Kappa_reward_models
% ideas of reference predicted by kappa_reward
[~,BINT,R,RINT,stats] = regress(S.data(:,2),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)])
disp(['GLM with ideas of reference as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,2),100,'r');
title('Predicting ideas of reference from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% paranoid ideation predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,3),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with paranoid ideation as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,3),100,'r');
title('Predicting paranoid ideation from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% unusual p experiences predicted by kappa_r
[B,BINT,R,RINT,stats] = regress(S.data(:,4),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with unusual p experiences as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,4),100,'r');
title('Predicting unusual p experiences from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% magical thinking predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,5),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with magical thinking as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,5),100,'r');
title('Predicting magical thinking from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%social anxiety predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,6),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with social anxiety as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,6),100,'r');
title('Predicting social anxiety from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%no close friends predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,7),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with no close friends as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,7),100,'r');
title('Predicting no close friends from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%consricted affect predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,8),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with consricted affect as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,8),100,'r');
title('Predicting consricted affect from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close


%odd behavior predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,9),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with odd behavior as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,9),100,'r');
title('Predicting odd behavior from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%odd speech predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,10),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with odd speech as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,10),100,'r');
title('Predicting odd speech from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%c-p factor predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,11),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with c-p factor as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,11),100,'r');
title('Predicting c-p factor from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%interpersonal factor predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,12),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with interpersonal factor as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,12),100,'r');
title('Predicting interpersonal factor from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%disorganised factor predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,13),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with disorganised factor as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,13),100,'r');
title('Predicting disorganised factor from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%total SPQ predicted by kappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,14),[SOSTY_par(:,1) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with total SPQ as the dependent variable predicted by kappa_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,1), S.data(:,14),100,'r');
title('Predicting total SPQ from Kappa_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')

%% Theta_reward models 

% ideas of reference predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,2),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with ideas of reference as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,2),100,'r');
title('Predicting ideas of reference from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% paranoid ideation predicted by thetakappa_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,3),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with paranoid ideation as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,3),100,'r');
title('Predicting paranoid ideation from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% unusual p experiences predicted by theta_r
[B,BINT,R,RINT,stats] = regress(S.data(:,4),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with unusual p experiences as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,4),100,'r');
title('Predicting unusual p experiences from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% magical thinking predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,5),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with magical thinking as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,5),100,'r');
title('Predicting magical thinking from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%social anxiety predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,6),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)])
disp(['GLM with social anxiety as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,6),100,'r');
title('Predicting social anxiety from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%no close friends predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,7),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with no close friends as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,7),100,'r');
title('Predicting no close friends from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%consricted affect predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,8),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with consricted affect as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,8),100,'r');
title('Predicting consricted affect from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%odd behavior predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,9),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with odd behavior as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,9),100,'r');
title('Predicting odd behavior from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%odd speech predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,10),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with odd speech as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,10),100,'r');
title('Predicting odd speech from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%c-p factor predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,11),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with c-p factor as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,11),100,'r');
title('Predicting c-p factor from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%interpersonal factor predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,12),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with interpersonal factor as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,12),100,'r');
title('Predicting interpersonal factor from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%disorganised factor predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,13),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with disorganised factor as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,13),100,'r');
title('Predicting disorganised factor from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%total SPQ predicted by theta_reward
[B,BINT,R,RINT,stats] = regress(S.data(:,14),[SOSTY_par(:,2) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with total SPQ as the dependent variable predicted by theta_reward:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,2), S.data(:,14),100,'r');
title('Predicting total SPQ from theta_reward');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%% Kappa_advice models
% ideas of reference predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,2),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with ideas of reference as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,2),100,'r');
title('Predicting ideas of reference from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% paranoid ideation predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,3),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with paranoid ideation as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,3),100,'r');
title('Predicting paranoid ideation from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% unusual p experiences predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,4),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with unusual p experiences as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,4),100,'r');
title('Predicting unusual p experiences from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% magical thinking predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,5),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with magical thinking as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,5),100,'r');
title('Predicting magical thinking from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%social anxiety predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,6),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with social anxiety as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,6),100,'r');
title('Predicting social anxiety from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%no close friends predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,7),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with no close friends as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,7),100,'r');
title('Predicting no close friends from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%consricted affect predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,8),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with consricted affect as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,8),100,'r');
title('Predicting consricted affect from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close


%odd behavior predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,9),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with odd behavior as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,9),100,'r');
title('Predicting odd behavior from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%odd speech predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,10),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with odd speech as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,10),100,'r');
title('Predicting odd speech from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%c-p factor predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,11),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with c-p factor as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,11),100,'r');
title('Predicting c-p factor from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%interpersonal factor predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,12),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with interpersonal factor as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,12),100,'r');
title('Predicting interpersonal factor from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%disorganised factor predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,13),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with disorganised factor as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,13),100,'r');
title('Predicting disorganised factor from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%total SPQ predicted by kappa_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,14),[SOSTY_par(:,3) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with total SPQ as the dependent variable predicted by kappa_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,3), S.data(:,14),100,'r');
title('Predicting total SPQ from kappa_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%% Theta_advice models

% ideas of reference predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,2),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with ideas of reference as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,2),100,'r');
title('Predicting ideas of reference from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% paranoid ideation predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,3),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with paranoid ideation as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,3),100,'r');
title('Predicting paranoid ideation from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% unusual p experiences predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,4),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with unusual p experiences as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,4),100,'r');
title('Predicting unusual p experiences from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

% magical thinking predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,5),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with magical thinking as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,5),100,'r');
title('Predicting magical thinking from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%social anxiety predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,6),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with social anxiety as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,6),100,'r');
title('Predicting social anxiety from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%no close friends predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,7),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with no close friends as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,7),100,'r');
title('Predicting no close friends from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%consricted affect predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,8),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with consricted affect as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,8),100,'r');
title('Predicting consricted affect from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close


%odd behavior predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,9),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with odd behavior as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,9),100,'r');
title('Predicting odd behavior from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%odd speech predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,10),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with odd speech as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,10),100,'r');
title('Predicting odd speech from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%c-p factor predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,11),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with c-p factor as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,11),100,'r');
title('Predicting c-p factor from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%interpersonal factor predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,12),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with interpersonal factor as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,12),100,'r');
title('Predicting interpersonal factor from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%disorganised factor predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,13),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)])
disp(['GLM with disorganised factor as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,13),100,'r');
title('Predicting disorganised factor from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

%total SPQ predicted by theta_advice
[B,BINT,R,RINT,stats] = regress(S.data(:,14),[SOSTY_par(:,4) ones(size(SOSTY_zeta,1),1)]);
disp(['GLM with total SPQ as the dependent variable predicted by theta_advice:'...
' p value  ' ...
num2str(stats(3))]);

s = scatter(SOSTY_par(:,4), S.data(:,14),100,'r');
title('Predicting total SPQ from theta_advice');
s.LineWidth = 0.6;
s.MarkerFaceColor = [0 0.5 0.5];
lsline;
input ('enter')
close

end

