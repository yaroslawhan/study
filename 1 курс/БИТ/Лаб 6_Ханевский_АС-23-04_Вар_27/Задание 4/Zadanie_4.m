clc
clear

x=-8:0.75:15;
subplot(2,2,1)
plot(x,f11(x))
subplot(2,2,2)
plot(x,f22(x))
subplot(2,2,3)
plot(x,f33(x))
subplot(2,2,4)
plot(x,f44(x))