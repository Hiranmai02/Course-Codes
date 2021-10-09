#include<simplecpp>
main_program{

//Polygon
int n;
cout<<"Sides";
cin>>n;
cout<<n;
turtleSim();
repeat(n){
forward(50);
right(360/n);  //Total Sum of External angles is 360
}
wait(10);

}

