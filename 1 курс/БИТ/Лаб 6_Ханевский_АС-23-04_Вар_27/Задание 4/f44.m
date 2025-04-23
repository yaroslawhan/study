function y=f44(x)
n=length(x);
for i=1:n
    if (x(i)>=-8) & (x(i)<=-7) 
        y(i)=f11(x(i));
    else if (x(i)>-7) & (x(i)<=1)
        y(i)=f22(x(i));
    else y(i)=f33(x(i));
    end
 end
end
end
