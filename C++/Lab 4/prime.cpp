#include<simplecpp>

main_program{

long int n,i=1,s,j=1,t=0;
cin>>n;
s = floor(sqrt(n));

repeat(n){

i += 1;   t = 0;  j = 1;

if((n % i) == 0){

repeat(i){
if((i % j)==0){
j += 1;
t += 1;
}
else
j += 1;
}
if(t==2)
cout<<i<<"\n";

}

}

}
