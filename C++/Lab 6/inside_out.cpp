#include<simplecpp>

double area(double x1,double y1, double x2, double y2, double x3, double y3){

double b = 0.5*abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2));
return b;

}

main_program{
double x1,y1,x2,y2,x3,y3,x4,y4,x5,y5;
cin>>x1>>y1>>x2>>y2>>x3>>y3>>x4>>y4>>x5>>y5;
double a,a1,a2,a3,b1;
a =  area(x1,y1,x2,y2,x3,y3);
a1 = area(x4,y4,x2,y2,x3,y3);
a2 = area(x1,y1,x4,y4,x3,y3);
a3 = area(x1,y1,x2,y2,x4,y4);
b1 = a1 + a2 + a3;

if(abs(a - b1)<= 1e-5)
cout<<"Yes";
else cout<<"No";

a1 = area(x5,y5,x2,y2,x3,y3);
a2 = area(x1,y1,x5,y5,x3,y3);
a3 = area(x1,y1,x2,y2,x5,y5);
b1 = a1 + a2 + a3;

if(abs(a - b1)<= 1e-5)
cout<<" Yes";
else cout<<" No";

}
