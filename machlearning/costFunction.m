function [J, grad] = costFunction(theta, X, y, lambda)


m = length(y);


newtheta=theta;
newtheta(1)=0;


J=sum((X*theta'-y).^2)/(2*m)    ;#    + sum(newtheta.^2)*lambda/(2*m);


grad = sum(  ((X*theta'-y)*ones(1,size(theta,2))  )  .*X)/m     ; #  + newtheta*lambda/m;




end
