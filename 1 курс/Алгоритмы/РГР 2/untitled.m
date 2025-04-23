clc;
clear;

disp('1 задание')
a=input('Введите начальную границу= ');
b=input('Введите конечную границу = ');
x1=linspace(-5,5,20);
plot(x1,F1(x1),'-g')
grid on
d=[a b];
z=fzero(@F1,d);
disp(z)

disp('2 задание')
a=1.4;
b=2.84;
n=12;
h=(b-a)/n;
x2=a:h:b;
s1 = trapz(x2,F2(x2));
disp(s1)

disp('3 задание')
x3=0.2:0.1:1.2;
y0=0.25;
[x3,y] = ode45(@(x3,y) (0.273.*(x3.^2+cos((1.3).*x3))+(0.687)*y), x3, y0)