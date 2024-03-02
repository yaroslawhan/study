clc
clear

a = [];
for i = 1:8
    for j = 1:8
        if i+j > 2
            a(i, j) = 2.7*(i^2)+3*i+j;
        else
            a(i, j) = (16.12*j+0.8*(i^2))^(1/2);
        end
    end
end
a
k = input('Enter number: ');
s = input('Enter string number: ');
n = 0;
for j = 1:8
    if a(s, j) < k
        n = n+1;
    end
end
disp('Number of elements: ')
n
b = [];
for j = 1:8
    mn = a(1, j);
    for i = 1:8
        if a(i, j) < mn
            mn = a(i, j);
        end
    end
    b(j) = mn;
end
disp('Minimums of columns: ')
b = b'
a = a([1 2 3 4 7 6 5 8], :)
d1 = [];
for i = 1:8
    d1(i) = a(i, i);
end
d1 = d1'

d2 = [];
l = 8;
for i = 1:8
    d2(i) = a(l, i);
    l = l-1;
end
d2 = d2'
disp('Vector X: ')
x = cat(1, d2, d1)
