#include<simplecpp>
main_program{
turtleSim();

repeat(6){  // to print 6 circles at 60 degree intervals

right(180); // To revert back to centre circle

repeat(360){
forward(0.5);  // other circles
right(1);
}

right(180);

repeat(60){  //to retrace centre circle for 60 degrees
forward(0.5);
right(1);
}

}
wait(30);
}
