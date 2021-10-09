% Assignment 3
function [strain_T,CTE_exp,CTE_fit,CTE_th] = MM220A3()
A = importdata('lattice_strain_data.txt');

a_1 = A(1,2);
a_T(:) = A(:,2);
T = A(:,1);
strain_T(:) = (a_T - a_1)./a_1;

CTE_exp(1) = 0;
for i = 2:length(a_T)
    CTE_exp(i) = (strain_T(i) - strain_T(i-1))./(T(i) - T(i-1));
end
% Instead of the above we can do strain_T./T as it is assumed as 0 for T1
plot(T, CTE_exp, '*');
hold on;

coeff = polyfit(T, CTE_exp, 2); 
CTE_fit(:) = polyval(coeff, T);
plot(T, CTE_fit, 'r'); 
hold on;

b1 = 9.472*10^-6;
b2 = 2.062*10^-8; 
b3 = 8.934*10^-12; 

CTE_th(:) = b1 + b2.*T - b3.*T.*T;
plot(T, CTE_th, 'g');
legend('CTE exp','CTE fit','CTE th');
xlabel('Temp');
ylabel('CTE');

print('MM220A3','-dpng')
end

% strain_T is strain corresponding to each temperature (ε_T)  
%CTE_exp is CTE calculated from 𝐶𝑇𝐸 = 𝑑ε/𝑑𝑇 
%CTE_fit is CTE calculated from polynomial expression using the function polyfit. 
%CTE_th is the theoretical value of instantaneous CTE
