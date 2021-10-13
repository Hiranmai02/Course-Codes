#include<simplecpp>

long long fact(int t){
long long int fact = 1;
while(t > 0){
fact *= t;
t -= 1;
}

return fact;
}

long long int combination(int n,int r){
long long int c=1;

c = fact(n)/(fact(r)*fact(n-r));
return c;
}

long long binomial(int n, int r){
long long int d=1,i=r,j=0;

return d;
}

void pascal_triangle(int k){
for(int i=0; i<k+1; i++)
cout<<binomial(k,i)<<" ";

}

main_program{
int k;
cin>>k;
pascal_triangle(k);
}
