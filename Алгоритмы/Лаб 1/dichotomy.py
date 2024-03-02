# Метод дихотомии

def dichotomy(a, b, eps, f):
    if f(a)*f(b) < 0:
        count = 1
        x = (a+b)/2
        xl = [x]
        while abs(f(x)) > eps:
            if abs(f(x)) == 0:
                break
            if f(a)*f(x) < 0:
                b = x
            elif f(b)*f(x) < 0:
                a = x
            count += 1
            x = (a+b)/2
            xl.append(x)
        return x, xl, count
    else:
        return "Корней нет"