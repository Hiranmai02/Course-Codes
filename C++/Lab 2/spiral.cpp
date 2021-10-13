#include<simplecpp>

main_program{
int i=20,n;
cout<<"Enter n ";
cin>>n;
turtleSim();

repeat(2){
left(90);  forward(10);
}

repeat(n){
repeat(2){
left(90);  forward(i);
}
i=i+10;
}

wait(20);
}
