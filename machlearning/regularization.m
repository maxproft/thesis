function [regData,average,SD] = regularization(Data)

average = mean(Data);
SD = std(Data);

%n is number of samples
%m is the number of data dimensions
[n,m] = size(Data);

averageArray = ones(n,1)*average;
SDArray = ones(n,1)*SD;


regData = (Data-averageArray)./SDArray;

regData(1:end,1)=1; %this forces the first column, the fixed values, to be one after regularisation

end
