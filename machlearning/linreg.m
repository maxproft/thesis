%% Initialization
#clear ; close all; clc

%Load the data and separate it into the input and output.
fprintf('Program Starting Now\n');
rawdata = load("maxSD machLearnData.csv");
inData = rawdata(1:end,1:end-1);#The first 6 columns
yReal = rawdata(1:end,end);#This is the last column

clear rawdata

fprintf('Making Poly Features\n');

%Make all polynomial terms here
polyInput = polyFeatures(inData);
clear in Data

#polyFeatures(ones(10,1)*[2,3,5]) %This is to test whether or not the polyFeatures function works

fprintf('Normalising the data\n');
%Regularising input:
[regPoly,regMean,regSD] = regularization(polyInput);

clear polyInput

fprintf('Training the algorithm\n');

%Train to get theta
options = optimset('GradObj', 'on', 'MaxIter', 400);
#options = optimset('MaxIter', 500);
initial_theta = zeros(1,size(regPoly,2));

if (exist("trainingInfo.csv")==2)
      machLearnData = load("trainingInfo.csv");
      previousTheta   = machLearnData(1,1:end);
      if (size(previousTheta) == size(initial_theta))
            printf("Loading the previous theta as the initial theta.\n\n")
            initial_theta = previousTheta;
      endif
endif



lambda = 0;



[initCost,initGrad] = costFunction(initial_theta, regPoly, yReal,lambda);
fprintf('Cost at initial theta: %f\n', initCost);

[theta, cost] = fminunc(@(t)(costFunction(t, regPoly, yReal,lambda)), initial_theta, options);
fprintf('Cost at final theta with fminunc: %f\n', cost);



%[theta, cost] = fmincg(@(t)(costFunction(t, regPoly, yReal,lambda)), initial_theta, options);
%fprintf('Cost at final theta with fmincg: %f\n', cost);
%theta;




%export theta, regMean and regSD so I can make new predictions
trainingInfo = [theta;regMean;regSD];
csvwrite("trainingInfo.csv",trainingInfo);




