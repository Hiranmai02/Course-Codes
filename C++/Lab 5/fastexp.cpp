#include<simplecpp>

main_program{

long long int x,n,k,i,ans=1,t,j;
cin>>x>>n>>k;

while(n != 0){
i = 0;

if(n != 2){
while(pow(2,i) < n){
i += 1;
}
}

if(n == 2){
i = 1;
while(pow(2,i) <= n){
i += 1;
}
}
//cout<<"  "<<i;
j = i; t = 1;
while(j>0){
t *= x;
j -= 1;
}

ans = (ans*(t%k))%k;


n = n/2;

}

if((n%2)==0)
cout<<ans;
else
cout<<(ans*(x%k))%k;


}
