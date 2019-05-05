%generate sample points
a=[5 10 20 40];
for j=1:length(a)
n=a(j);
h=2/n;
xi=-1:h:1;
yi=(1./(1+xi.^2));
plot(xi,yi,'ro')
hold on
x=-1:0.01:1;
pn=Naive_poly_interpolation(xi,yi,x);
plot(x,pn,'k','linewidth',3)
norm(pn-(1./(1+x.^2)))
pn=Lagrange_poly_interpolation(xi,yi,x);
plot(x,pn,'y','linewidth',3)
norm(pn-(1./(1+x.^2)))
end