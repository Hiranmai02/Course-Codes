#include<simplecpp>

main_program{

int n;
//cout<<"Enter value of n ";
cout<<"\n";
cin>>n;

repeat(n){
cout<<"\n";

repeat(3*n){
cout<<"*";
}
}

repeat(2*n){
cout<<"\n";

repeat(n){
cout<<" ";
}
repeat(n){
cout<<"*";
}
repeat(n){
cout<<" ";
}
}
}
