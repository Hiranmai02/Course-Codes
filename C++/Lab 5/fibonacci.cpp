#include<simplecpp>

main_program{

long int n,k,f0=0,f1=1,sum=0,t;
cin>>n>>k;
cout<<f0<<"\n"<<f1<<"\n";

repeat(n-2){
sum = f0 + f1;
f0 = f1;
sum = sum % k;
f1 = sum;
t = sum % k;
cout<<t<<"\n";
}

}
