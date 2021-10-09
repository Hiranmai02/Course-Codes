function MM220Q2()
n = [1:1:10];
T1 = n;
T2 = exp(n)./n;
T3 = n.*n.*log(n);
plot(n,T1,n,T2,n,T3);
xlabel('n');
ylabel('T1,T2,T3');
legend('T1','T2','T3');
print('MM220Q2','-dpng')
end
