#include<simplecpp>
using namespace std;

void binary(long long n){

if(n/2 == 0){
cout<<n;
return;
}
binary(n/2);
cout<<n%2;
}

main_program{
	long long n;
	cin>>n;
	binary(n);
}
