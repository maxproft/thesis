function [regData,average,SD] = regularization(Data)

average = mean(Data);
SD = std(Data);

%n is number of samples
%m is the number of data dimensions
[n,m] = size(Data);

averageArray = ones(n,1)*average;
SDArray = ones(n,1)*SD;


regData = (Data-averageArray)./SDArray;


end
