%Load the data and separate it into the input and output.
rawdata = load("data.csv");
indata = rawdata(1:end,1:end-1);
yReal = rawdata(1:end,end);



%Make all polynomial terms here
polyInput = indata;
%I also need to add in a constant term here.


%Regularising input:
[regPoly,regMean,regSD] = regularization(polyInput);




%Train to get theta

theta = ones(1,size(regPoly,2));




%export theta, regMean and regSD so I can make new predictions
trainingInfo = [theta;regMean;regSD]
csvwrite("trainingInfo.csv",trainingInfo);




