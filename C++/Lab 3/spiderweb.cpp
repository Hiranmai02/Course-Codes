#include<simplecpp>

main_program{
initCanvas();
Turtle t1,t2,t3,t4,t5,t6;
float x=200, y=20;

repeat(3){
t1.forward(x);   t1.right(180);   t1.forward(2*x);
t1.right(180);   t1.forward(x);   t1.right(60);
}

t2.right(60);  t2.forward(y);  t2.right(120);

repeat(6){
t2.forward(y);
t2.right(60);
}
t2.right(60);   t2.forward(y);   t2.right(120);
y=y+20;

t3.right(60);  t3.forward(y);  t3.right(120);

repeat(6){
t3.forward(y);
t3.right(60);
}
t3.right(60);   t3.forward(y);   t3.right(120);
y=y+40;

t4.right(60);  t4.forward(y);  t4.right(120);

repeat(6){
t4.forward(y);
t4.right(60);
}
t4.right(60);   t4.forward(y);   t4.right(120);
y=y+40;

t5.right(60);  t5.forward(y);  t5.right(120);

repeat(6){
t5.forward(y);
t5.right(60);
}
t5.right(60);   t5.forward(y);   t5.right(120);
y=y+40;

t6.right(60);  t6.forward(y);  t6.right(120);

repeat(6){
t6.forward(y);
t6.right(60);
}
t6.right(60);   t6.forward(y);   t6.right(120);

wait(30);
}
