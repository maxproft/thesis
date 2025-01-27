function polyInput = polyFeatures(inData)
%Generate all polynomial features here

m = size(inData,2); %number of initial features
n = size(inData,1);

twopoly = [];
threepoly = [];
fourpoly = [];
fivepoly = [];
sixpoly = [];
sevenpoly = [];
eightpoly = [];
ninepoly = [];
tenpoly = [];
for c=1:m
onenum = inData(1:end,c);
for d=c:m
twonum = onenum.*inData(1:end,d);
twopoly = [twopoly,twonum];
for e=d:m
threenum = twonum.*inData(1:end,e);
threepoly = [threepoly, threenum];
for f=e:m
fournum = threenum.*inData(1:end,f);
fourpoly = [fourpoly,fournum];
for g=f:m
fivenum = fournum.*inData(1:end,g);
fivepoly = [fivepoly,fivenum];
for h=g:m
sixnum = fivenum.*inData(1:end,h);
sixpoly = [sixpoly,sixnum];
for i=h:m
sevennum = sixnum.*inData(1:end,i);
sevenpoly = [sevenpoly,sevennum];

for j=i:m
eightnum = sevennum.*inData(1:end,j);
eightpoly = [eightpoly,eightnum];

for k=j:m
ninenum = eightnum.*inData(1:end,k);
ninepoly = [ninepoly,ninenum];

for l=k:m
tennum = ninenum.*inData(1:end,l);
tenpoly = [tenpoly,tennum];
endfor
endfor
endfor
endfor
endfor
endfor
endfor
endfor
endfor
endfor


polyInput = [ones(n,1),inData,twopoly,threepoly,fourpoly,fivepoly,sixpoly,sevenpoly,eightpoly,ninepoly,tenpoly];

end
#{












Copy segments as you need to and paste at the bottom

for f=e:m
fournum = threenum*f;
fourpoly = [fourpoly,fournum];
endfor



for g=f:m
fivenum = fournum*g;
fivepoly = [fivepoly,fivenum];
endfor



for h=g:m
sixnum = fivenum*h;
sixpoly = [sixpoly,sixnum];
endfor



for i=h:m
sevennum = sixnum*i;
sevenpoly = [sevenpoly,sevennum];
endfor



for j=i:m
eightnum = sevennum*j;
eightpoly = [eightpoly,eightnum];
endfor



for k=j:m
ninenum = eightnum*k;
ninepoly = [ninepoly,tennum];
endfor



for l=k:m
tennum = ninenum*l;
tenpoly = [tenpoly,tennum];
endfor
#}



