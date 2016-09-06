%Make the new input values here
NewData = rand(5,6);

NewData(1,3)=1.5;#0.5*(3)+(4)**3
NewData(1,4)=1.5;#pred: 4.1

NewData(2,3)=1.5;
NewData(2,4)=7.5;#pred: 420

NewData(3,3)=1.5;
NewData(3,4)=10;#pred: 1000

NewData(4,3)=1.5;
NewData(4,4)=3.5;#pred: 44

NewData(5,3)=1.5;
NewData(5,4)=30;#pred: 27000

%load the values computed from machine learning
machLearnData = load("trainingInfo.csv");

theta   = machLearnData(1,1:end);
regMean = machLearnData(2,1:end);
regSD   = machLearnData(3,1:end);

%Making the prediction
pred = predict(NewData,theta,regMean,regSD);
pred

%Plotting the data



