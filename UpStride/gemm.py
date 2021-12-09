from typing import List
Vector = List
Matrix = List

def GEMM1(A: Vector, B: Vector) -> Vector:
    # GEMM with ReLU
    return [n if n >=0 else 0 for n in [a*b for a,b in zip(A, B)] ]

def GEMM2(A: Matrix, B: Matrix) -> Matrix:
    # GEMM with ReLU
    return [[i if i>=0 else 0 for i in line] for line in \
            [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]]

if __name__ == "__main__":
    # Vector by Vector
    A = [1,2,3]
    B = [-2,5,6]

    assert GEMM1(A, B) == [0, 10, 18], "Calculation Error"

    # Matrix by Matrix
    C = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
    D = [[5,8,1,2],
        [6,7,3,0],
        [-22,5,9,1]]

    assert GEMM2(C, D) == [[36, 160, 60, 27], 
                           [0, 97, 73, 14], 
                           [0, 157, 112, 23]], "Calculation Error"