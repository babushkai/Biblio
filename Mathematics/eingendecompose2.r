> A <- matrix(c(1,0,0,0,1,0,0,0,1),nrow=3)
> A
     [,1] [,2] [,3]
[1,]    1    0    0
[2,]    0    1    0
[3,]    0    0    1
> B <- matrix(c(-1,1,0,2,-1,0,0,1,-1),nrow=3)
> B
     [,1] [,2] [,3]
[1,]   -1    2    0
[2,]    1   -1    1
[3,]    0    0   -1
> C <- matrix(c(2,2,0,-1),ncol=2)
> C
     [,1] [,2]
[1,]    2    0
[2,]    2   -1
> D <- matrix(c(1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,1),nrow=4)
> D
     [,1] [,2] [,3] [,4]
[1,]    1   -1    1   -1
[2,]   -1    1   -1    1
[3,]    1   -1    1   -1
[4,]   -1    1   -1    1
> A-B
     [,1] [,2] [,3]
[1,]    2   -2    0
[2,]   -1    2   -1
[3,]    0    0    2
> A+C
Error in A + C : non-conformable arrays
> dim(A)
[1] 3 3
> dim(C)
[1] 2 2
> A-D
Error in A - D : non-conformable arrays
> C+D
Error in C + D : non-conformable arrays
> A*C
Error in A * C : non-conformable arrays
> A*B
     [,1] [,2] [,3]
[1,]   -1    0    0
[2,]    0   -1    0
[3,]    0    0   -1
> A%*%B
     [,1] [,2] [,3]
[1,]   -1    2    0
[2,]    1   -1    1
[3,]    0    0   -1
> B%*%A
     [,1] [,2] [,3]
[1,]   -1    2    0
[2,]    1   -1    1
[3,]    0    0   -1
> A <- matrix(c(2,1,0,1,4,1),nrow=3)
> A
     [,1] [,2]
[1,]    2    1
[2,]    1    4
[3,]    0    1
> B <- matrix(c(0,1,-1,1,0,1,-1,0),nrow=2)
> B
     [,1] [,2] [,3] [,4]
[1,]    0   -1    0   -1
[2,]    1    1    1    0
> A*B
Error in A * B : non-conformable arrays
> A%*%B
     [,1] [,2] [,3] [,4]
[1,]    1   -1    1   -2
[2,]    4    3    4   -1
[3,]    1    1    1    0
> A
     [,1] [,2]
[1,]    2    1
[2,]    1    4
[3,]    0    1
> A <- matrix(c(1,0,0,0,1,0,0,0,1),nrow=3)
> A
     [,1] [,2] [,3]
[1,]    1    0    0
[2,]    0    1    0
[3,]    0    0    1
> rank(A)
[1] 8.0 3.5 3.5 3.5 8.0 3.5 3.5 3.5 8.0
> library(Matrix)
> rankMatrix(A)
[1] 3
attr(,"method")
[1] "tolNorm2"
attr(,"useGrad")
[1] FALSE
attr(,"tol")
[1] 6.661338e-16
> B <- matrix(c(-1,1,0,2,-1,0,0,1,-1),nrow=3)
> B
     [,1] [,2] [,3]
[1,]   -1    2    0
[2,]    1   -1    1
[3,]    0    0   -1
> rankMatrix(B)
[1] 3
attr(,"method")
[1] "tolNorm2"
attr(,"useGrad")
[1] FALSE
attr(,"tol")
[1] 6.661338e-16
> C <- matrix(c(2,2,0,-1),nrow=2)
> C
     [,1] [,2]
[1,]    2    0
[2,]    2   -1
> rankMatrix(C)
[1] 2
attr(,"method")
[1] "tolNorm2"
attr(,"useGrad")
[1] FALSE
attr(,"tol")
[1] 4.440892e-16
> D <- matrix(c(1,-1,1,-1,-1,1,-1,1,1,-1,1,-1,-1,1,-1,1),nrow=4)
> D
     [,1] [,2] [,3] [,4]
[1,]    1   -1    1   -1
[2,]   -1    1   -1    1
[3,]    1   -1    1   -1
[4,]   -1    1   -1    1
> rankMatrix(D)
[1] 1
attr(,"method")
[1] "tolNorm2"
attr(,"useGrad")
[1] FALSE
attr(,"tol")
[1] 8.881784e-16
> C
     [,1] [,2]
[1,]    2    0
[2,]    2   -1
> rank(C)
[1] 3.5 3.5 2.0 1.0
> A <- matrix(c(1,4,7,0,8,9,1,5,4,7,98,2,14,15,2),nrow=3)
> A
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    0    1    7   14
[2,]    4    8    5   98   15
[3,]    7    9    4    2    2
> t(A)
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    0    8    9
[3,]    1    5    4
[4,]    7   98    2
[5,]   14   15    2
> A%*%t(A)
     [,1] [,2] [,3]
[1,]  247  905   53
[2,]  905 9934  346
[3,]   53  346  154
> t(A)%*%A
     [,1] [,2] [,3] [,4] [,5]
[1,]   66   95   49  413   88
[2,]   95  145   76  802  138
[3,]   49   76   42  505   97
[4,]  413  802  505 9657 1572
[5,]   88  138   97 1572  425
> rankMatrix(A%*%t(A))
[1] 3
attr(,"method")
[1] "tolNorm2"
attr(,"useGrad")
[1] FALSE
attr(,"tol")
[1] 6.661338e-16
> rankMatrix(t(A)%*%A)
[1] 3
attr(,"method")
[1] "tolNorm2"
attr(,"useGrad")
[1] FALSE
attr(,"tol")
[1] 1.110223e-15
> A <- matrix(c(1,37,0,2),nrow=2)
> A
     [,1] [,2]
[1,]    1    0
[2,]   37    2
> solve(A)
      [,1] [,2]
[1,]   1.0  0.0
[2,] -18.5  0.5
> solve(A)*2
     [,1] [,2]
[1,]    2    0
[2,]  -37    1
> solve(A)%*%A
     [,1] [,2]
[1,]    1    0
[2,]    0    1
> A%*%solve(A)
     [,1] [,2]
[1,]    1    0
[2,]    0    1
> A <- matrix(c(1,3,2,6),nrow=2)
> solve(A)
Error in solve.default(A) : 
  Lapack routine dgesv: system is exactly singular: U[2,2] = 0