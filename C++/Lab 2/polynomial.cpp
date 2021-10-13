#include<simplecpp>

main_program{
int a,b,c,i=0;
int x[3],y[3];

//cout<<"Enter Coeffients of Quad Eqn  ";
cin>>a>>b>>c;
cout<<"\n";


//cout<<"Enter 3 values of x  ";
repeat(3){
cin>>x[i];
i=i+1;
}

i=0;
repeat(3){
y[i] = a*x[i]*x[i] + b*x[i] + c;
i = i+1;
}

i=0;
repeat(3){
cout<<"\n";
cout<<y[i];
i = i+1;
}
}



