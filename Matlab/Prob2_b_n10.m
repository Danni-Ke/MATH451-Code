options.MaxIter=1500;
options.Tol=1e-10;

a1 = ones(100,1);
x_10 = zeros(100,1);
SDD10 = MakeSDD(1,4,1,10);
HugeSDD10 = MakeHugeSDD(2,SDD10,2,10);

%n=10 counting time for Jacobi
tic
J1_n10 = Jacobi(HugeSDD10,a1,x_10,options);
toc
%error calculation for Jacobi
real_b1_n10 = mldivide(HugeSDD10,a1);
err_b1_n10_J = abs(real_b1_n10 - J1_n10);
disp(mean(err_b1_n10_J.^2));

%couting time for Gauss seidel
tic
GS1_n10 = Gauss_seidel(HugeSDD10,a1,x_10,options);
toc
%error calculation for Gauss seidel
err_b1_n10_GS = abs(real_b1_n10 - GS1_n10);
disp(mean(err_b1_n10_GS.^2));


%Find the optimal omega for SOR
omega_vec = 0.01:0.01:1.99;

iter_min = 999999999;
n = size(omega_vec);
for i = 1:n(2)
    [SOR1_n10, iter_cur] = SOR(HugeSDD10,a1,omega_vec(i),x_10,options);
    if iter_cur < iter_min
        iter_min = iter_cur;
        SOR_min = SOR1_n10;
        omega_min = omega_vec(i);
    end
end
disp(omega_min);  %optimal omega
disp(iter_min);   %iteration for SOR

%counting time for SOR
tic
SOR1_n10 = SOR(HugeSDD10,a1,omega_min,x_10,options);
toc
%error calculation for SOR
err_b1_n10_SOR = abs(real_b1_n10 - SOR1_n10);
disp(mean(err_b1_n10_SOR.^2));