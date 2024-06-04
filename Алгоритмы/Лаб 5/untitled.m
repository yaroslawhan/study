clc;
clear;

table = xlsread('Лист Microsoft Excel.xlsx')
poly = polyfit(table(:, 1), table(:, 2), 3)
x = -1:0.1:3;
subplot(2,2,1)
plot(x, polyval(polyfit(table(:, 1), table(:, 2), 2), x))
title('Полином 2-й степени')
xlabel('X')
ylabel('F(X)')
hold on
scatter(table(:, 1), table(:, 2))
subplot(2,2,2)
plot(x, polyval(polyfit(table(:, 1), table(:, 2), 3), x))
title('Полином 3-й степени')
xlabel('X')
ylabel('F(X)')
hold on
scatter(table(:, 1), table(:, 2))
subplot(2,2,3)
plot(x, polyval(polyfit(table(:, 1), table(:, 2), 4), x))
title('Полином 4-й степени')
xlabel('X')
ylabel('F(X)')
hold on
scatter(table(:, 1), table(:, 2))
subplot(2,2,4)
plot(x, polyval(polyfit(table(:, 1), table(:, 2), 5), x))
title('Полином 5-й степени')
xlabel('X')
ylabel('F(X)')
hold on
scatter(table(:, 1), table(:, 2))
hold off