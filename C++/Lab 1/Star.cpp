#include<simplecpp>
main_program{

cout<<"Ënter Number of sides (Odd)";
int n;
cin>>n;

turtleSim();

right(((n-2)*180)/n); forward(200);

repeat(n-1){
right(180 - (180/n));   forward(200);
}

wait(30);
}
