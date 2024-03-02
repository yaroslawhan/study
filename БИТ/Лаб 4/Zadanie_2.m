clc
clear
x=input('¬ведите x: ');
y=input('¬ведите y: ');
  
if a(x, y) < b(x, y)
    mn1 = a(x, y);
else
    mn1 = b(x, y);
end

if b(x, y) < c(x, y)
    mn2 = b(x, y);
else
    mn2 = c(x, y);
end


if mn1 < mn2
    mx = mn2;
else
    mx = mn1;
end

u = mx;

if a(x, y) == 'ERROR a' | b(x, y) == 'ERROR b'
    if a(x, y) == 'ERROR a'
        disp('ERROR a')
    end

    if b(x, y) == 'ERROR b'
        disp('ERROR b')
    end
else
    u
end

%u = max(min(a(x, y),b(x, y)), min(b(x, y),c(x, y)))
