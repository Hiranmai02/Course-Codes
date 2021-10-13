#include<simplecpp>

void circle(){
repeat(180){
left(2);  forward(1);
}
}

void temp(int n, double angle){

if(n==0)  return;
circle();
left(angle);

temp(n-1,angle);
}

void loop(int n, double angle){

temp(n,360.0/n);
}

main_program{
	turtleSim();
	hide();
	int n;
	cin>>n;
	loop(n,0);
	wait(20);
}
