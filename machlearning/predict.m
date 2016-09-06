function pred = predict(inData,theta,regMean,regSD)
%input the raw, unregularised data, theta and parameters so I can regularise the data


%generate the polynomial features


polyData = polyFeatures(inData);



[n,m] = size(polyData);
meanArray = ones(n,1)*regMean;
SDArray = ones(n,1)*regSD;


regPoly = (polyData-meanArray)./SDArray;
regPoly(1:end,1)=1; %this forces the first column, the fixed values, to be one after regularisation

pred = regPoly*theta';

end

