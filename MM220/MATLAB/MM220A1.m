% Assignment 1
% [z] = MM220A1(-5*pi,pi/10,5*pi,-5*pi,pi/10,5*pi)

function [z] = MM220A1(xmin,deltax,xmax,ymin,deltay,ymax)

%xlim([-5*pi 5*pi])
%ylim([-5*pi 5*pi])
xmin = -5*pi;
ymin = -5*pi;
xmax = 5*pi;
ymax = 5*pi;
deltax = pi/10;
deltay = pi/10;

x1 = [xmin:deltax:xmax];
y1 = [ymin:deltay:ymax];

[x,y] = meshgrid(x1,y1);

k = sin(x).*cos(y);
z = k./x;
surf(x,y,z);

xlabel('x');
ylabel('y');
zlabel('sin(x)cos(y)/x');

print('MM220A1','-dpng');
end

% Output variable(s) are on the LHS of the above code
% z: output variable
