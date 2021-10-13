#include<simplecpp>

main_program{
turtleSim();

int y=60,x=100;

penUp();
left(90);   forward(200);   left(180);
penDown();

repeat(3){
right(y);  forward(x);   left(y);
y = y/2;
}

right(15);

right(180); forward(x);
right(150); forward(x);

right(180); forward(x);
right(45);  forward(x);

right(120); forward(x);
right(45); forward(x);

right(180); forward(x);
right(150); forward(x);

right(180); forward(x);
left(15); forward(x);

right(90); forward(x);
right(60); forward(x);

right(90); forward(x);
left(15); forward(x);


right(180); forward(x);
right(150); forward(x);

right(180); forward(x);
right(45);  forward(x);

right(120); forward(x);
right(45); forward(x);

right(180); forward(x);
right(150); forward(x);


wait(60);
}
