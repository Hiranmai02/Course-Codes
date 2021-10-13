#include<simplecpp>

main_program{

unsigned long int m,n,mod=1;
//cout<<"Enter n and m (n<=10^5) and (m<=10^9)\n";
cin>>n>>m;

repeat(n){
mod = (mod*(n%m))%m;
n -= 1;
}
cout<<mod;
//cout<<"Mod is  "<<mod;

}
