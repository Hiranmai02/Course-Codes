#include<simplecpp>
main_program{
turtleSim();

// Square with connected midpoints
repeat(4){
forward(100);
right(90);
}
penUp();
forward(50);
penDown();
right(45);  // First nested line
forward(50*sqrt(2));  //Using Pythagoras Theorem
repeat(3){
right(90);  //For other three lines
forward(50*sqrt(2));
}
wait(10);

}
