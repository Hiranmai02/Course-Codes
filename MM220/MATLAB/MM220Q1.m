function MM220Q1()
% initial conditions
y1(1) = exp(-2);
y2(1) = exp(-2);
% h1 = 0.1;
% h2 = 0.5;

% Range of x for h1 and h2
x1 = [1:0.1:10];
x2 = [1:0.5:10];

% Analytical Function
y = exp(-2*x1);

% using h = 0.1
for i = 1:90
    y1(i+1) = y1(i) - 0.2*y1(i);  
end

% using h = 0.5 gives us hy' as 0.5*(-2)*y = -y
% all values in y2 are 0 (except the initial condition taken)
for i = 1:18
    y2(i+1) = y2(i) - y2(i);  
end

% plot with h = 0.1
plot(x1,y1,'*');
hold on;
% plot of actual function
plot(x1,y);
hold on;
% plot with h = 0.5
plot(x2,y2,'o');
hold on;

xlabel('x');
ylabel('exp(-2x)');
legend('h = 0.1','Analytical Function','h = 0.5')
print('MM220Q1','-dpng')
end
