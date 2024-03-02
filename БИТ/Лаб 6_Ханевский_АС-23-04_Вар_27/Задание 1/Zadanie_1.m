clc
clear
a = [0.85 1.27 -2.37 0.57; 1.47 -0.28 0.56 -1.21; 0.66 1.31 -0.63 0.43; 0.57 -0.78 -0.56 -0.83]
b = [2.23; 1.71; -0.54; 3.65]

%Inverse matrix method
a1 = inv(a)
x1 = a1*b

%Cramer's method
a1 = a();
a1(:, 1) = b
a2 = a();
a2(:, 2) = b
a3 = a();
a3(:, 3) = b
a4 = a();
a4(:, 4) = b

d = det(a)
d1 = det(a1)
d2 = det(a2)
d3 = det(a3)
d4 = det(a4)

x2 = [d1/d; d2/d; d3/d; d4/d]

%Gausses method
c = rref([a b]);
x3 = c(:, 5)

%Solve method
syms x1 x2 x3 x4
xx = [x1; x2; x3; x4];
eqn = a*xx == b;
x5 = solve(eqn);
x5 = [double(x5.x1); double(x5.x2); double(x5.x3); double(x5.x4)]

%Fsolve method
x6 = [0;0;0;0];
fsolve(@f, x6)