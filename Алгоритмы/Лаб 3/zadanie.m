clc;
clear;

a = [4.5 -3.5 7.4; 
    3.1 -0.6 -2.3; 
    0.8 7.4 -0.5]
b = [2.5; -1.5; 6.4]

%Cramer method
a1 = a;
a1(:, 1) = b;
a2 = a;
a2(:, 2) = b;
a3 = a;
a3(:, 3) = b;


da = det(a)
da1 = det(a1);
da2 = det(a2);
da3 = det(a3);

if da ~= 0
    disp('Roots of system: ')
    x = [da1/da; da2/da; da3/da];
    disp(vpa(x, 3))
else
    disp('Determinant is equal 0')
end

%inverse matrix method

ai = inv(a)
x1 = ai*b;
disp('Roots of system: ')
disp(vpa(x1, 3))