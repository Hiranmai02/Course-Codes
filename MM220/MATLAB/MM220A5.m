% Assignment 5
function [f_explicit,f_numerical] = MM220A5()
syms t;
n = 4.2;
tau = 1236;
eqn1 = 'Df = n*((t^(n-1))/(tau)^n)*exp(-((t/tau)^n))';
ic = 'f(0) = 0';
f1 = dsolve(eqn1, ic);
t = [0:1:1800];
f_explicit = subs(f1);
plot(t,f_explicit,'g');
hold on;

dfdt = @(t,f) n.*((t.^(n-1))./(tau).^n).*exp(-((t./tau).^n));
tspan = [0,1800];
f0 = 0;
[t,f_numerical] = ode45(dfdt, tspan, f0);
plot(t, f_numerical, 'r');
hold on;

time = [300 540 660 780 960 1080 1260 1440 1620 1800];
fraction = [0.039 0.050 0.065 0.108 0.285 0.458 0.661 0.857 0.935 0.967];
plot(time, fraction, '*');
xlabel('Time');
ylabel('Fraction');
legend('dsolve','ode45','exp');
hold on;
print('MM220A5','-dpng');
%f_explicit is fraction of phase transformed calculated using the dsolve function(case a) for time 0 s to 1800 s, using a time step of 1 second.
%f_numerical is fraction of phase transformed calculated using the ode45 function(case b) for time 0 s to 1800 s.
end
