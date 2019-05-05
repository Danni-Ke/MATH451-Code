function resultHugeSDD=MakeHugeSDD(a,B,b,n)
%a,c is the number of I, eg 2I-> a=2
%B is a matrix have the same size as the final matrix
%n is the size of the block matrix
A=a*eye(n);
C=b*eye(n);
DiagMatrix=kron(eye(n),B);
D=ones(n);
LMatrix = kron((tril(D,-1)-tril(D,-2)),A);
UMatrix = kron((triu(D,1)-triu(D,2)),C);
resultHugeSDD = LMatrix + DiagMatrix + UMatrix;
