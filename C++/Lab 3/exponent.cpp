#include<simplecpp>

main_program{
initCanvas();

Line l1(250,0,250,250);
Line l2(0,250,500,250);

Line l3(150,250,150,252);
float x=150;
float a=-5;

Text t1(250,265,"0");
Text t2(150,265,"-5");
Text t3(350,265,"5");
Text t4(225,102,"exp(5)");
Text t5(10,265,"-X");
Text t6(490,265,"X");
Text t7(265,10,"Y");

repeat(2000){
float y = -exp(a);
l3.moveTo(x,y+250); //center is at (250,250)
l3.imprint();
x += 0.1;
a = (x-250)/20;    //Scaling factor for x axis is 20
}
getClick();
}
