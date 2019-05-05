
dt=0.8 % step size
t = 0:dt:3;
y(1) = 1; % initial condition
for n=1:(length(t)-1)
y(n+1)=y(n)-dt*y(n);
end % to disply all t values
t_y=[t' y']