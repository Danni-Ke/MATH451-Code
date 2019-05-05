function pn=Lagrange_poly_interpolation(xi,yi,x)
num=length(xi);%number of sample points
pn=0;
for i=1:num
    li=1;
    for j=1:num
        if j~=i
            li=li.*(x-xi(j))/(xi(i)-xi(j));
        end
    end
    pn=pn+yi(i)*li;
end