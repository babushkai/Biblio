# get mtcars data
A<-data.matrix(mtcars) 

# Make square-matrix 
B<-t(A)%*%A

# Get eigenvalues and vectors
L <- eigen(B)$values
P <- eigen(B)$vectors 

# Diagonalization of B matrix(square). The result is matrix whose diagonal elements are eigenvalues
diagonal <- t(P)%*%B%*%(P)

# Inverse of Eigendecomposotion, create the original matrix
B<-(P)%*%diagonal%*%t(P)