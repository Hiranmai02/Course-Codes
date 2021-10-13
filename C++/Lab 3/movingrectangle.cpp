#include<simplecpp>

main_program{
initCanvas("abc",1500,1500);

int a=getClick();   int b=getClick();
int x1,x2,y1,y2;
x1=a/65536;  y1=a % 65536;
x2=b/65536;  y2=b % 65536;

float c1,c2;
c1=(x1+x2)/2;    c2=(y1+y2)/2;
Rectangle r1(c1,c2,abs(x2-x1),abs(y2-y1));

int c=getClick(),x3,y3;
x3=c/65536;   y3=c % 65536;

float vx,vy,t=1;
vx=abs(x3-c1)/100;
vy=abs(y3-c2)/100;
float x=atan((y3-c2)/(x3-c1));
r1.rotate(x);

repeat(100){
r1.move(vx*t,vy*t);
wait(0.1);
}
getClick();
}
