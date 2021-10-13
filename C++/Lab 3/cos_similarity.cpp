#include<simplecpp>
#include<iomanip>
main_program{
long int n;
long double sum=0,cosx,mag_a=0,mag_b=0,a,b;
//cout<<"Enter n (Dimension of Vector)\n";
cin>>n;
cout<<"\n";
//cout<<"Enter the components of the two vectors pair wise (ai and bi)\n";
repeat(n){
cin>>a>>b;
sum += a*b;
mag_a += a*a;
mag_b += b*b;
}
cosx = sum/sqrt(mag_a*mag_b);
cout.setf(ios::fixed);
cout.setf(ios::showpoint);
cout<<setprecision(2);
cout<<cosx;
}
