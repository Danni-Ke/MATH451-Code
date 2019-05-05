fun=@(x) x*exp(x);
%function handle
df_analytical=@(x) x*exp(x)+exp(x);
%analytical derivative
for i=0:10
a=i/10;
h=0.01;
df=numerical_deri(fun,a,h);
disp(df);
%compute the derivative
err1=df-df_analytical(a);
disp(err1);
%numerical test order
h=0.005;
df=numerical_deri(fun,a,h);
err2=df-df_analytical(a)
%display the order
disp(log2(err1/err2))
h=0.0025;
df=numerical_deri(fun,a,h);
err4=df-df_analytical(a)
%display the order 
disp(log2(err2/err4));

end
