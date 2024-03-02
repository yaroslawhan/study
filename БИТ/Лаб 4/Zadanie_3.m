clc
clear
x = -8:0.48:12;
subplot(2, 2, 1)
plot(x, f1(x))
subplot(2, 2, 2)
plot(x, f2(x), '-xR', 'MarkerSize', 6, 'LineWidth', 0.5)
title('F2')
xlabel('X')
ylabel('Y')
axis([-3 15 -5 4])
grid on
subplot(2, 2, 3)
plot(x, f1(x), x, f2(x))