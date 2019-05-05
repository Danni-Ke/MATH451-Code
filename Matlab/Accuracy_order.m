fun=@(x) x*exp(x);
%function handle
df_analytical=@(x) x*exp(x)+exp(x);
%analytical derivative
for i=(0:10)
a=i/10;
h=0.01;
df=Numerical_derivative(fun,a,h);
%compute the derivative
err1=df-df_analytical(a)
%numerical test order
h=0.005;
df=Numerical_derivative(fun,a,h);
err2=df-df_analytical(a)
log2(err1/err2)
h=0.0025;
df=Numerical_derivative(fun,a,h);
err4=df-df_analytical(a)
log2(err2/err4)
end
