clc
clear

x = -1:0.01:1;

ans1 = vpa(fsolve(@f, 0), 3);
disp("Fsolve method: ")
ans1
disp("Fzero method: ")
ans2 = vpa(fzero(@f, 0), 3)

plot(x, f(x), 'k', ans1, f(ans1), 'r*', 'Markersize', 10);
grid on;

a = input("Enter number a: ");
b = input("Enter number b: ");
eps = input("Enter number eps: ");

syms y x1;
y = x1^5 + x1 - 1;
diff_y = diff(y);
diff2_y = diff(diff_y);

if f(a)*f(b) < 0
    x = a - ((b-a)*(f(a)))/(f(b)-f(a));
    
    while (abs(f(x)) >= eps) %& (abs(subs(diff_y, x)) < 1)
        % if f(b)*(subs(diff2_y, x)) > 0
        %     x = x - ((b-x)*(f(x)))/(f(b)-f(x));
        % elseif f(a)*(subs(diff2_y, x)) > 0
        %     x = x - ((x-a)*(f(x)))/(f(x)-f(a));
        % end

        if f(a)*f(x) < 0
            b = x;
        elseif f(b)*f(x) < 0
            a = x;
        end

        x = a - ((b-a)*(f(a)))/(f(b)-f(a));
    end
end

disp("Chords method: ")
x