function browse()
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
Files=dir(fullfile('*.mat'));
files = struct2cell(Files)';
b = {'variables'};

for i = 1:length(files)
    names(i,1) = files(i,1);
end

x = false(size(names)); % <-- Indexes to delete, start out nobody deleted
    for k=1:numel(b)
        x = x | ~cellfun(@isempty,strfind(names,b{k})); % <-- Flag the ones that b{k} matches
    end
names(x) = []; % <-- Delete all the flagged lines at once
plots = string(names);
    for i = 1:length(plots)
        a = plots(i);
        if exist('a', 'var') == 1
            load(a)
            fprintf(a)
            hgf_plotTraj_reward_social(est_sosty)
            input('enter')            
        end
        close
    end
end

