% Newton - Raphson Method
function [t,count] = MM220T1()
x(1) = 2;
tol = 0.001;
n = 10;
count = 0;
for i = 1:n
    k = x(i);
    x(i+1) = x(i) - ((k.^3 - k - 1)./(3*k.^2 - 1));
    count = count + 1;
    if (abs(x(i+1) - x(i)) < tol)
        t = x(i);
        break;
    end
end
n1 = [0:1:count];
plot(n1,x, '*')
xlabel('n');
ylabel('x')
end
