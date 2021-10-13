#include<simplecpp>

main_program{
initCanvas();
float x=200, y=200, r=50;

Circle c1(x,y,r);
c1.imprint();
int a=getClick();     int b=getClick();
int x1,y1,x2,y2;
x1=a/65536;      y1=a%65536;
x2=b/65536;      y2=b%65536;
//cout<<x1<<"   "<<x2<<"   "<<y1<<"  "<<y2<<"\n";
Line l1(x1,y1,x2,y2);
float m= (float(y2-y1)/float(x2-x1));
//cout<<m<<"  ";
float t;

if(m>0)
t=arctangent((m));
else if(m<0)
t=arctangent((m)) + 180;
//cout<<t<<"  ";
float d = abs((y-m*x+m*x2-y2)/sqrt(1+m*m));
float c=2*d;
//cout<<c<<"  "<<d<<"  ";
//cout<<(c*sine(t))<<"   "<<(c*cosine(t));
if(t<90)
c1.move((c*sine(t)),(-c*cosine(t)));
else if(t>90)
c1.move(abs(c*sine(t)),abs(c*cosine(t)));
c1.imprint();
getClick();
}
