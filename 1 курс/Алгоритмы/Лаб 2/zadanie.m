clc;
clear;

syms x1 y1 x y;
f1 = x1^2*y1^2 - 3*x1^3 - 6*y1^3 + 2*7;
f2 = x1^4 - 9*y1 + 2*(7/(7+1));

% F(1) = x^2*y^2 - 3*x^3 - 6*y^3 + 2*7;
% F(2) = x^4 - 9*y + 2*(7/(7+1));
dots = [fsolve(@fun, [-10, 10]); fsolve(@fun, [2, 2])];
xses = [dots(1, 1); dots(2, 1)];
ys = [dots(1, 2); dots(2, 2)];

dots1=solve([x^2*y^2 - 3*x^3 - 6*y^3 + 2*7 == 0, x^4 - 9*y + 2*(7/(7+1)) == 0]);
x_values = double(dots1.x);
y_values = double(dots1.y);
% dots1(2)=double(eval(char(dots1(2))));


disp('Roots: ')
disp(dots)

disp('All roots: ')
disp(x_values)
disp(y_values)

f1p = ezplot(f1);
set(f1p, 'Color', 'black', 'LineWidth', 2);
grid on;
hold on;
f2p = ezplot(f2);
set(f2p, 'Color', 'green', 'LineWidth', 2);
dotsp = scatter(xses, ys, 100, '*r');
hold off;