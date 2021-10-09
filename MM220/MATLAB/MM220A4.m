% Assignment 4

function [estrn,pstrn,coeffs20,pfit20,error20] = MM220A4()

B = importdata('exp_stress_strain.txt');

sn = B(:,1);
ss = B(:,2);
E = 330000;

estrn = ss./E;
pstrn = sn - estrn;

coeffs20 = polyfit(pstrn, ss, 20);
pfit20 = polyval(coeffs20,pstrn);
plot(sn, ss, 'o');
hold on;
plot(sn, pfit20, 'r');
ylabel('Stress')
xlabel('Strain')

print('MM220A4','-dpng')

e_sum = sum(((pfit20 - ss)./ss).^2);
error20 = sqrt(e_sum./length(ss));

end

%estrn and pstrn is values of elastic strain and plastic strain respectively.
%coeffs20 is coefficients obtained for the polynomial fit
%pfit20 is stress values obtained using polynomial fit
%error20 is root mean squared (RMS) error associated with your fit
