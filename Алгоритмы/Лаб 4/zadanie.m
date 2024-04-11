clc;
clear;

plt = fplot(@f, [1.1, 10], 'LineWidth', 2, 'Color', 'magenta');
hold on;

plot([exp(1), exp(1)], [0.1, f(exp(1))], '--', 'LineWidth', 1.5, 'Color', 'black');
plot([5, 5], [0.1, f(5)], '--', 'LineWidth', 1.5, 'Color', 'black');

title('Lab. 2, Khanewskiy Y., var. №26');
grid on;
hold off;

x = [0 0.26 0.52 0.79 1.05 1.31 1.57 1.83 2.09 2.36 2.62 2.88 3.14];
y = [0 0.13 0.43 0.78 1.1 1.38 1.61 1.8 1.95 2.06 2.14 2.18 2.2];
tr = trapz(x, y);
q = quad(@f, exp(1), 5);

disp('Root trapz: ')
disp(tr)

disp('Root quad: ')
disp(q)

n = 47
a = exp(1);
b = 5;
integral = (2/3)*((log(5)^(3/2))-1);
h = (b-a)/n;
result = f(a) + f(b);
for i = 1:n-1
	if mod(i, 2) == 0
		result = result + 2*f(a+i*h);
    else
		result = result + 4*f(a+i*h);
    end
end
result = result*h/3;
abs_err = abs(integral-result);
rel_err = 100*(abs_err/integral);

disp('Simpson method: ')
disp(result)
disp('Absolute error: ')
disp(abs_err)
disp('Relative error: ')
disp(rel_err)