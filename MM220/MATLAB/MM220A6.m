% Assignment 6
function y=MM220A6()
dydt = @(t,y) y.*(1-y);
y0 = 0.01; 
tspan = [0 15];
[t,y] = ode45(dydt, tspan, y0);

plot(t,y);
xlabel('Time');
ylabel('Fraction of infected people');
print('MM220A6', '-dpng');
%y is the proportion of infected people
end
