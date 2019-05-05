function ans = MatSum(A)
[m, n] = size(A);
ans = 0;
for i = 1: m;
    for j = 1: n;
        ans = ans + A(i, j);
    end
end
disp(ans);
end