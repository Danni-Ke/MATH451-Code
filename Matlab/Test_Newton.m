f=@(x) x^2-2*x*cos(x)+(cos(x))^2;
df=@(x) 2*x-2*cos(x)+2*x*sin(x)-sin(2*x);
x0=1;
Tol=[1e-5 1e-6 1e-8 1e-10];
for i=1:4
[x,num_iter]=Newton(f,df,x0,Tol(i));
disp(x);
disp(num_iter);
end
