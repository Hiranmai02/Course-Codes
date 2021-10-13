#include<simplecpp>

main_program{

double a,d;
int n;
//cout<<"Enter values of a,n,d  \n";
cin>>a>>n>>d;
double sum1 = a;
float sum2 = a;
//cout<<"\n";

repeat(n){
cout<<int(sum2)<<"  ";
sum2 += d;
}

cout<<"\n";

repeat(n){
cout<<sum1<<"  ";
sum1 += d;
}

}
