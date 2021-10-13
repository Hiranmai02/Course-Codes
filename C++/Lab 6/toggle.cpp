#include<simplecpp>
int i=0,j=0,t=0;

void toggle(unsigned int &n, int k){
int a[32];      long int sum =0;

for(i=0; i<32; i++){
a[31-i] = n%2;
n = n/2;
}

if(a[31-k] == 0)
a[31-k] = 1;
else
a[31-k] = 0;

for(j=0 ; j<32; j++){
sum += a[j]*pow(2,(31-j));
}

cout<<sum;
}

main_program{
unsigned int n;  int k;
cin>>n>>k;
toggle(n,k);
}
