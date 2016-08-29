%Make the new input values here
NewData = rand(50,6);

%load the values computed from machine learning
machLearnData = load("trainingInfo.csv")

theta   = machLearnData(1,1:end)
regMean = machLearnData(2,1:end)
regSD   = machLearnData(3,1:end)

%Convert data to polynomial terms
polyData = NewData

%regularise the data with previously used values
[n,m] = size(polyData);

averageArray = ones(n,1)*average;
SDArray = ones(n,1)*SD;

regData = (polyData-averageArray)./SDArray;


%Making the prediction
pred = predict(regData,theta,regMean,regSD);


%Plotting the data

