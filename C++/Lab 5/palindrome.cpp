#include<simplecpp>

main_program{

long int x,y,rev=0,rem,t,n,a;
cin>>x>>y;
if(x<y)
t = x;
else
t = y;

n = abs(x-y)+1;

repeat(n){
rev = 0;   a = t;

while(a != 0){
rem = a%10;
rev = rev*10 + rem;
a /= 10;
}

if(t == rev)
cout<<t<<"\n";

t += 1;

}

}
