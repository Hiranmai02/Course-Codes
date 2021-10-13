#include<simplecpp>

main_program{

long int max1=0,max2=0,x,n,temp=0;
cin>>n;

repeat(n){
cin>>x;
if(x >= max1){
temp = max1;
max1 = x;
max2 = temp;
}
else if(x < max1 && x > max2)
max2 = x;
}

cout<<max2;

}
