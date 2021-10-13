#include<simplecpp>

main_program{
turtleSim();

float x=220;

repeat(11){

penUp();
right(45);   forward(x/sqrt(2));   //moving to centre of square
right(5);       //Turning the square
forward(x/sqrt(2));  //moving to corner
penDown();

right(135);  //To maintain same center of square (Same Direction)
x = x-5;     //Decreasing Length of Square

repeat(4){
forward(x);   right(90);  //Drawing a Square
}

penUp();    //Same commands in penup mode to come back to the same
right(45);   forward(x/sqrt(2));   right(1); //point after each
forward(x/sqrt(2));                          //square

right(135);
x = x-5;

repeat(4){
forward(x);   right(90);
}
penDown();

}
wait(30);
}
