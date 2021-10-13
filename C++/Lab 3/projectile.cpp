#include<simplecpp>

main_program{
initCanvas("Projectile",600,600);

getClick();

//Line l(20,250,600,250);
float e=0.85,vx=1,vy=-1,g=0.01,x=20,y=250,r=5,X;
Circle c(x,y,r);
c.penDown();

y += 0.1;

repeat(200){
c.move(vx,vy);
vy += g;
y -= vy;
wait(0.01);
}

X=c.getX();
c.penUp();
c.moveTo(X,250);
c.penDown();


vx = 1; vy = -1*e; y=250.1;

repeat(170){

c.move(vx,vy);
vy += g;
y -= vy;
wait(0.01);
}

X=c.getX();
c.penUp();
c.moveTo(X,250);
c.penDown();

vx = 1; vy = -1*e*e; y=250.1;

repeat(140){

c.move(vx,vy);
vy += g;
y -= vy;
wait(0.01);
}

getClick();
}
