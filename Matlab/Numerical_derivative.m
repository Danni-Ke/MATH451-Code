function df=Numerical_derivative(fun,x,h)
df=(fun(x+h)-fun(x))/h;%forward scheme
df=(fun(x+h)-fun(x))/h;%backward scheme
df=(fun(x+h)-fun(x-h))/2/h;%central finite difference 
