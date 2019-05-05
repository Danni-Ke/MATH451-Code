fun=@(x) exp(exp(sin(x^2)))
%function handle
df_analytical=@(x) exp(exp(sin(x^2)))*exp(sin(x^2))*cos(x^2)*(2*x)
%analytical derivative
a=1;
h=0.1;
df=Numerical_derivative(fun,a,h);
%compute the derivative
err1=df-df_analytical(a)

%numerical test order
h=0.05;
df=Numerical_derivative(fun,a,h);
err2=df-df_analytical(a)
log2(err1/err2)
h=0.025;
df=Numerical_derivative(fun,a,h);
err4=df-df_analytical(a)
log2(err2/err4)
