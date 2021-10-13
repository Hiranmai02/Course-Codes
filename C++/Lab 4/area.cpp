#include<simplecpp>
#include <iomanip>

main_program{

double x1,y1,x2,y2,x3,y3,x4,y4,area;
int n,i=0;
cin>>n;
cin>>x1>>y1;
cin>>x2>>y2;
cin>>x3>>y3;

double sum = (x1*y2 - x2*y1) + (x2*y3 - x3*y2);

if(n==3)
{sum += (x3*y1 - x1*y3);
cout<<abs(sum/2);}

else{

repeat(n-2){
i += 1;

if(i != (n-2)){

cin>>x4>>y4;
x2 = x3;    y2 = y3;
x3 = x4;    y3 = y4;

sum += (x2*y3 - x3*y2);
}

else{
sum += (x3*y1 - x1*y3);
}

}


}
area = abs(sum/2);
cout << fixed << setprecision(2) << area;


}
