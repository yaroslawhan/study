clc;
clear;

n = 5;
A = zeros(n, n);
for i = 1:n
    for j = 1:n
        if (i == j)
            A(i, j) = 1/i;
        else
            A(i, j) = ((-1)^j)*j;
        end
    end
end
A

B = ones(n, 1);
B(1, 1) = 8;
B

X = linsolve(A, B)

noiseA = normrnd(0, 0.05/3, n, n);
noiseB = normrnd(0, 0.05/3, n, 1);

An = A + noiseA
Bn = B + noiseB

Xn1 = linsolve(A, Bn)
Xn2 = linsolve(An, B)
Xn3 = linsolve(An, Bn)

err1 = norm((X - Xn1), 1)/norm(X, 1)
err2 = norm((X - Xn2), 1)/norm(X, 1)
err3 = norm((X - Xn3), 1)/norm(X, 1)

errInp1 = norm((B - Bn), 1)/norm(B, 1);
errInp2 = norm((A - An), 1)/norm(A, 1);
errInp3 = max(norm((A - An), 1)/norm(A, 1), norm((B - Bn), 1)/norm(B, 1));
dd1 = err1/errInp1
dd2 = err2/errInp2
dd3 = err3/errInp3

condA = cond(A, 1)
condAn = cond(An, 1)

echoA = norm(inv(A), 1)*norm(B, 1)/norm(X, 1)
echoAn1 = norm(inv(A), 1)*norm(Bn, 1)/norm(Xn1, 1)
echoAn2 = norm(inv(An), 1)*norm(B, 1)/norm(Xn2, 1)
echoAn3 = norm(inv(An), 1)*norm(Bn, 1)/norm(Xn3, 1)

fprintf(1, '%g <= %g \n', err1, condAn*errInp1)
fprintf(1, '%g <= %g \n', err2, condAn*errInp2)
fprintf(1, '%g <= %g \n', err3, condAn*errInp3)


n2 = 2*8;
A2 = zeros(n2, n2);
for i = 1:n2
    for j = 1:n2
        if (i == j)
            A2(i, j) = 1/i;
        else
            A2(i, j) = ((-1)^j)*j;
        end
    end
end
A2

B2 = ones(n*2, 1);
B2(1, 1) = 2*8;
B2

X2 = linsolve(A2, B2)

noiseA2 = normrnd(0, 0.05/3, n2, n2);
noiseB2 = normrnd(0, 0.05/3, n2, 1);

An2 = A2 + noiseA2
Bn2 = B2 + noiseB2

Xn12 = linsolve(A2, Bn2)
Xn22 = linsolve(An2, B2)
Xn32 = linsolve(An2, Bn2)

err12 = norm((X2 - Xn12), 1)/norm(X2, 1)
err22 = norm((X2 - Xn22), 1)/norm(X2, 1)
err32 = norm((X2 - Xn32), 1)/norm(X2, 1)

errInp12 = norm((B2 - Bn2), 1)/norm(B2, 1)
errInp22 = norm((A2 - An2), 1)/norm(A2, 1)
errInp32 = max(norm((A2 - An2), 1)/norm(A2, 1), norm((B2 - Bn2), 1)/norm(B2, 1))
dd12 = err12/errInp12
dd22 = err22/errInp22
dd32 = err32/errInp32

condA2 = cond(A2, 1)
condAn2 = cond(An2, 1)

echoA2 = norm(inv(A2), 1)*norm(B2, 1)/norm(X2, 1)
echoAn12 = norm(inv(A2), 1)*norm(Bn2, 1)/norm(Xn12, 1)
echoAn22 = norm(inv(An2), 1)*norm(B2, 1)/norm(Xn22, 1)
echoAn32 = norm(inv(An2), 1)*norm(Bn2, 1)/norm(Xn32, 1)

fprintf(1, '%g <= %g \n', err12, condAn2*errInp12)
fprintf(1, '%g <= %g \n', err22, condAn2*errInp22)
fprintf(1, '%g <= %g \n', err32, condAn2*errInp32)