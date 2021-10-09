#include<simplecpp>
main_program{

//Triangle with given sides
//Logic used : Cosine Rule
float a,b,c;
float A,C,cosA,cosC;
cout<<"Ënter Sides \n";
cin>>a>>b>>c;
cosA = (b*b + c*c - a*a)/(2*b*c);
cosC = (a*a + b*b - c*c)/(2*a*b);

A = arccosine(cosA);
C = arccosine(cosC);

turtleSim();

forward(c);
right(180 - A);
forward(b);
right(180 - C);
forward(a);

wait(30);
}
