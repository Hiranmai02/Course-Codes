#include<simplecpp>

main_program{

float x[3],y[3],area;
int i=1;
//cout<<"Enter coordinates in ordered pairs\n";
repeat(3){
cin>>x[i];   cin>>y[i];
i += 1;
}

area = x[1]*(y[2]-y[3]) - x[2]*(y[1]-y[3]) + x[3]*(y[1]-y[2]);
cout<<abs(area)/2;
}
