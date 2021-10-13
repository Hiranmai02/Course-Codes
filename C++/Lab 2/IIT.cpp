#include<simplecpp>

main_program{
int n;
cout<<"Enter n (Top dimension of the letters) (Odd number>1)";
cin>>n;

repeat(2){  // Top part (Horizontal) has 2 lines

repeat(3){  // for I I T

repeat(n){
cout<<"*";   // Top part of letters
}
cout<<"   "; //3 spaces
}
cout<<"\n";
}

repeat(n){  // Vertical part of I has n stars
                    // T has n+2 stars
repeat((n-1)/2){
cout<<" ";          //Initial Number of spaces before first
}                   //star of vertical lines
cout<<"*";

repeat(2){

repeat(n+2){        //Number of spaces between stars of VL
cout<<" ";          //of two letters
}
cout<<"*";
}

cout<<"\n";
}

repeat(2){

repeat(2){
repeat(n){        //Bottom horizontal block of 2 I
cout<<"*";
}
cout<<"   ";
}

repeat((n-1)/2){  //Extra vertical stars for T
cout<<" ";        //instead of horizontal block
}
cout<<"*";
cout<<"\n";
}

}

