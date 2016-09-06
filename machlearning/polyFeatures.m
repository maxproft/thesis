function polyInput = polyFeatures(inData)
%Generate all polynomial features here



m = size(inData,2); %number of initial features
n = size(inData,1);
twopoly = [];
for i=1:m
for j=i:m
twopoly = [twopoly,(inData(1:end,i).*inData(1:end,j))];
endfor
endfor



threepoly = [];
for i=1:m
for j=i:m
for k=j:m
threepoly = [threepoly, (inData(1:end,i).*inData(1:end,j).*inData(1:end,k))];
endfor
endfor
endfor


polyInput = [ones(n,1),inData,twopoly,threepoly];

%polyInput = [ones(n,1),inData];


end
