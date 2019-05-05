function pn=Naive_poly_interpolation(xi,yi,x)
n=length(xi)-1;
A=vander(xi);
b=yi';
a=A\b;
pn=0;
for i=1:n+1
    pn=pn+a(i)*x.^(n-i+1);
end