function f = b(x, y)
    if abs(x)-y^2 > 0
        f = log(abs(x)-y^2);
    else
        f = 'ERROR b';
    end
end