#include<simplecpp>

main_program{
initCanvas("abc",1200,1200);
Turtle t;

Rectangle r1(70,70,62,26);  //creating buttons
r1.setColor(COLOR("red"));
r1.setFill(true);
Text x(70,70,"Forward");

Rectangle r2(150,70,34,26);
r2.setColor(COLOR("blue"));
r2.setFill(true);
Text y(150,70,"Left");

Rectangle r3(230,70,42,26);
r3.setColor(COLOR("green"));
r3.setFill(true);
Text z(230,70,"Right");

Rectangle r4(310,70,72,26);
r4.setColor(COLOR("yellow"));
r4.setFill(true);
Text w(310,70,"Backward");

repeat(10){

int a = getClick();
int x1 = a/65536, y1 = a % 65536;

if(x1<=101 && x1>=39 && y1<=83 && y1>=57)  //Calculating endpoints of buttons
t.forward(50);                               //to be clicked
else if(x1<=167 && x1>=133 && y1<=83 && y1>=57)
t.left(10);
else if(x1<=251 && x1>=209 && y1<=83 && y1>=57)
t.right(10);
else if(x1<=346 && x1>=274 && y1<=83 && y1>=57)
t.right(180);  t.forward(50);
}

wait(30);
}
