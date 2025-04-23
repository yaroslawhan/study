clc
clear

x = -40:0.1:40;
f = 0.5*x-4*sin(0.8*x);
plot(x, f)
x1 = [fzero(@f1, [-4 -2]); fzero(@f1, [-2 2]); fzero(@f1, [2 4])]
x2 = [fsolve(@f1, -5); fsolve(@f1, -1); fsolve(@f1, 5)]