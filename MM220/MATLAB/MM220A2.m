% Assignment 2
% [x1,x2,PE1,PE2,KE1,KE2,TE1,TE2] = MM220A2([0:0.1:30],1,1,1,0.1,0)

function [x1,x2,PE1,PE2,KE1,KE2,TE1,TE2] = MM220A2(t,k,m,A,b1,b2)
m = 1;
k = 1;
A = 1;
b1 = 0.1;
b2 = 0;

w1 = sqrt((k./m) - ((b1.^2)./(4.*m.^2)));
w2 = sqrt((k./m) - ((b2.^2)./(4.*m.^2)));

x1 = A.*exp((-b1.*t)./(2.*m)).*cos(w1.*t);
x2 = A.*exp((-b2.*t)./(2.*m)).*cos(w2.*t);

t = [0:0.1:30];

v1 = -A.*exp((-b1.*t)./(2.*m)).*(w1.*sin(w1.*t) + (b1./(2.*m)).*cos(w1.*t));
v2 = -A.*exp((-b2.*t)./(2.*m)).*(w2.*sin(w2.*t) + (b2./(2.*m)).*cos(w2.*t));

PE1 = 0.5.*k.*x1.*x1;
PE2 = 0.5.*k.*x2.*x2;

KE1 = 0.5.*m.*v1.*v1;
KE2 = 0.5.*m.*v2.*v2;

TE1 = PE1 + KE1;
TE2 = PE2 + KE2;

plot(t,x1,'r',t,x2,'g');
xlabel('t');
ylabel('x');

print('MM220A21','-dpng');

plot(t,PE1,'r',t,KE1,'g',t,TE1,'b');
xlabel('t');
ylabel('E');

print('MM220A22','-dpng');

plot(t,PE2,'r',t,KE2,'g',t,TE2,'b');
xlabel('t');
ylabel('E');

print('MM220A23','-dpng');

end

% Note output variables are on the LHS of the above code enclosed within [] brackets

% Description of output variables:
% x1: position array for damped motion (b1 = 0.1 kg/s)
% x2: position array for undamped motion (b2 = 0)
% PE1,KE1,TE1: arrays of potential energy, kinetic energy and total energy for damped motion
% PE2,KE2,TE2: arrays of potential energy, kinetic energy and total energy for undamped motion
