%Define the interval
n = [5 10 20 40];

%Define the functions
f1 = @(x) sin(x);
f2 = @(x) (1./(1+25*x.^2));

%loop through te intervals
for j = 1:length(n)
%Create x vector representing uniform grid
x = linspace(-1, 1, n(j));
 
%Calculate natural polynomial interpolation
p = polyfit(x, f1(x), n(j));
%Calculate error
Err = (polyval(p, x))-f1(x);

disp('Natural Error f1');
disp(Err);
  
p = polyfit(x, f2(x), n(j));
%Calculate error
Err = (polyval(p, x))-f2(x);
disp('Natural Error f2');
disp(Err);
  
%Calculate Lagrange polynomial interpolation
% Make sure that X and f2 are row vectors
Y = f2(x);
if size(x,1) > 1; x = x'; end
if size(Y,1) > 1; Y = Y'; end
if size(x,1) > 1 || size(Y,1) > 1 || size(x,2) ~= size(Y,2)
error('both inputs must be equal-length vectors')
end
N = length(x);
pvals = zeros(N,N);
% Calculate the polynomial weights for each order
for j = 1:N
% the polynomial whose roots are all the values of X except this one
pp = poly(x( (1:N) ~= j));
% scale so its value is exactly 1 at this X point (and zero
% at others, of course)
pvals(j,:) = pp ./ polyval(pp, x(j));
end
% Each row gives the polynomial that is 1 at the corresponding X
% point and zero everywhere else, so weighting each row by the
% desired row and summing (in this case the polycoeffs) gives
% the final polynomial
P = Y*pvals;
Err = P - f2(x);
disp('Lagrange Interpolation Error f2:');
disp(Err);
% Make sure that X and f1 are row vectors
Y = f1(x);
if size(x,1) > 1; x = x'; end
if size(Y,1) > 1; Y = Y'; end
if size(x,1) > 1 || size(Y,1) > 1 || size(x,2) ~= size(Y,2)
error('both inputs must be equal-length vectors')
end
N = length(x);
pvals = zeros(N,N);
% Calculate the polynomial weights for each order
for j = 1:N
% the polynomial whose roots are all the values of X except this one
pp = poly(x( (1:N) ~= j));
% scale so its value is exactly 1 at this X point (and zero
% at others, of course)
pvals(j,:) = pp ./ polyval(pp, x(j));
end
% Each row gives the polynomial that is 1 at the corresponding X
% point and zero everywhere else, so weighting each row by the
% desired row and summing (in this case the polycoeffs) gives
% the final polynomial
P = Y*pvals;
Err = P - f1(x);
disp('Lagrange Interpolation Error f1:');
disp(Err);
end
