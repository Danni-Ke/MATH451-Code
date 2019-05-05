function resultSDD=MakeSDD(a,b,c,n)
%a,b,c is the number we going to put into the matrix
%n is the size of matrix
DiagMatrix = b*eye(n);
A= ones(n);
LMatrix = a*(tril(A,-1)-tril(A,-2));
UMatrix = c*(triu(A,1)-triu(A,2));
resultSDD = LMatrix + DiagMatrix + UMatrix;