#include<simplecpp>

main_program{
long int i, n;
    double x, sum=1, t=1;

    cin>>n>>x;

    x=x*3.14159/180;

    for(i=1;i<=n;i++)
    {
        t=t*(-1)*x*x/(2*i*(2*i-1));
        sum=sum+t;
    }

    cout<<sum;
}
