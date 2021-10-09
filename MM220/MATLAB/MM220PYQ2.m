% Arrhenius Rate Equation
function [Ea,A] = MM220T2()
A = importdata("rate.txt");
T = A(:,1);
k = A(:,2);
plot(1./T, log(k), '*'); 
hold on;
coeff = polyfit(1./T, log(k),1);
y = polyval(coeff, 1./T);
plot(1./T,y);
Ea = -8.314*coeff(1);
A = exp(coeff(2));
end
