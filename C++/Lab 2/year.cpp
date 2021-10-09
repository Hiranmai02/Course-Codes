#include<simplecpp>

main_program{
turtleSim();

repeat(2){

forward(30);   right(90);
forward(30);   right(90);
forward(30);   left(90);
forward(30);   left(90);
forward(30);

penUp();   forward(30);  penDown();

repeat(2){
forward(30);   left(90);
forward(60);  left(90);
}

penUp();   forward(60); left(90);
forward(60); right(90); penDown();

}

wait(10);
}
