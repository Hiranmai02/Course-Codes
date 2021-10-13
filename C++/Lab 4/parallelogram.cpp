#include<simplecpp>

main_program{

long double x1,x2,x3,x4;
long double y1,y2,y3,y4;

cin>>x1>>y1;
cin>>x2>>y2;
cin>>x3>>y3;
cin>>x4>>y4;

double a,b;
a = x1 - x2 + x3;
b = y1 - y2 + y3;

if((abs(x4 - a) <= 1e-5) && (abs(y4 - b) <= 1e-5))
cout<<"Yes";
else
cout<<"No";

}
