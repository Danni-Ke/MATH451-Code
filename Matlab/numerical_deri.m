function df=numerical_deri(fun,x,h)
df=(fun(x-2*h)-8*fun(x-h)+8*fun(x+h)-fun(x+2*h))/(12*h);