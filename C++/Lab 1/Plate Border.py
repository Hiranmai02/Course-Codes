#include<simplecpp>

main_program{
turtleSim();

repeat(36){
left(45);
forward(50);

repeat(180){
forward(0.1);
right(1);
}

right(45);
forward(50);

repeat(180){
forward(0.1);
left(1);
}
left(10);
}


wait(60);
}
