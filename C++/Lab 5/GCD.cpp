#include<simplecpp>
main_program{
long int m, n;
cin >> m >> n;

while(m % n != 0){
long int nextm = n;
long int nextn = m % n;
m = nextm;
n = nextn;
}

cout << n << endl;
}
