#include<simplecpp>
long long int i = 0,sum = 0;

long long int diff(long int n){

repeat(n+1){
sum += i*i - i;
i += 1;
}

return sum;
}

main_program{
long long int n;
cin>>n;
cout<<diff(n);

}
