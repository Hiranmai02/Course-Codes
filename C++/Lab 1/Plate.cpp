#include<simplecpp>

main_program{

turtleSim();


repeat(18){
repeat(25){
forward(1);
right(10);
}

forward(30);

repeat(25){
forward(1);
left(10);
}

forward(30);
right(20);
}

wait(30);
}
