function [y1, y2] = f11(x,y)
    y1 = 4*y(1) + y(2) - exp(2*x);
    y2 = -2*y(1) + y(2);
end