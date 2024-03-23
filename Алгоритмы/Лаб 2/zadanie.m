clc;
clear;

syms x1 y1;
f1 = x1^2*y1^2 - 3*x1^3 - 6*y1^3 + 2*7;
f2 = x1^4 - 9*y1 + 2*(7/(7+1));

% F(1) = x^2*y^2 - 3*x^3 - 6*y^3 + 2*7;
% F(2) = x^4 - 9*y + 2*(7/(7+1));

x1 = fsolve(@fun, [-2, 2])

f1p = ezplot(f1);
set(f1p, "Color", "black", "LineWidth", 2);
grid on;
hold on;
f2p = ezplot(f2);
set(f2p, "Color", "green", "LineWidth", 2);
xses = plot(x1, fun());
hold off;

function F = fun(x)

F(1) = x(1)^2*x(2)^2 - 3*x(1)^3 - 6*x(1)^3 + 2*7;
F(2) = x(1)^4 - 9*x(1) + 2*(7/(7+1));
end