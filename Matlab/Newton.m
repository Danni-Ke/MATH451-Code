function [x,num_iter]=Newton(f,df,x0,Tol)
num_iter=0;
while 1
    x=x0-f(x0)/df(x0);
    num_iter=num_iter+1;
    if abs(x-x0)<Tol
        break
    end
    if abs(f(x))<Tol
        break
    end
    x0=x;
end