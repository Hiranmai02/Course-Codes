#include<simplecpp>

void semi1(){
repeat(90){
right(2);   forward(0.5);
}
repeat(90){
left(2);   forward(0.5);
}
}

void semi2(){
repeat(90){
left(2);   forward(0.5);
}
repeat(90){
right(2);   forward(0.5);
}
}

void temp(int n){

if(n==0) return;

semi1();
temp(n-1);

}

void pattern(int n){

temp(n);
forward(90/3.14);
repeat(n){
semi2();
}

}

main_program{
	turtleSim();
	//hide();
	//Initialising position of turtle
	left(180);
	penUp();
	forward(200);
	penDown();
	right(90);
	//Taking input
	int n;
	cin>>n;
	pattern(n);

	wait(20);
}
