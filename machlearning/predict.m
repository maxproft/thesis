function pred = predict(inData,theta,regMean,regSD)
%input the raw, unregularised data, theta and parameters so I can regularise the data


%generate the polynomial features
polyData = regdata



[n,m] = size(polyData);
meanArray = ones(n,1)*average;
SDArray = ones(n,1)*SD;


regData = (polyData-averageArray)./SDArray;

pred = regData*theta';

end

