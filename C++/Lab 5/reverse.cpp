#include<simplecpp>

main_program{

long int n, rev = 0, rem;

    cin >> n;

    while(n != 0) {
        rem = n%10;
        rev = rev*10 + rem;
        n /= 10;
    }

    cout << rev;
}
