from sympy import symbols, linear_eq_to_matrix


def invert(X):
    rows = len(X)
    cols = len(X[0])

    identity = makeIdentityMatrix(rows,cols)
    for i in range(0,rows):
        X[i]+=identity[i]

    i = 0
    for j in range(0,cols):
        print("On col {0} and row {1}".format(j,i))
        zero_sum, first_non_zero = check_for_all_zeros(X,i,j)
        if zero_sum==0:
            if j==cols:
                return X
            raise Exception("Matrix is singular.")
        if first_non_zero != i:
            X = swap_row(X,i,first_non_zero)
        X[i] = [m/X[i][j] for m in X[i]]

        for q in range(0,rows):
            if q!=i:
                scaled_row = [X[q][j] * m for m in X[i]]
                X[q]= [X[q][m] - scaled_row[m] for m in range(0,len(scaled_row))]
        if i==rows or j==cols:
            break
        i += 1

    for i in range(0,rows):
        X[i] = X[i][cols:len(X[i])]

    return X


def check_for_all_zeros(X, i, j):
    non_zeros = []
    first_non_zero = -1
    for m in range(i,len(X)):
        non_zero = X[m][j]!=0
        non_zeros.append(non_zero)
        if first_non_zero==-1 and non_zero:
            first_non_zero = m
    zero_sum = sum(non_zeros)
    return zero_sum, first_non_zero


def swap_row(X, i, p):
    X[p], X[i] = X[i], X[p]
    return X


def makeIdentityMatrix(num_row, num_col):
    matrix = []
    for i in range(num_row):
        new_row = []
        for j in range(num_col):
            if i == j:
                number = 1
            else:
                number = 0
            new_row.append(number)
        matrix.append(new_row)
    return matrix


def matmult(a, b):
    zip_b = zip(*b)
    # uncomment next line if python 3 :
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]


def getMatrix(lgs):
    x, y, z = symbols('x, y, z')
    A, B = linear_eq_to_matrix(lgs, (x, y, z))
    A.tolist()
    B.tolist()
    return A, B


"""
matrixA = [[3, 4, -5, 6],
           [6, 5, -6, 5],
           [9, -4, 2, 3],
           [0, 2, -3, 1]]


matrixB = [[39],
           [43],
           [6],
           [13]]
"""

LGS = ["x + 2*y + 3*z - 1", "3*x + y + z + 6", "-2*x + 4*y + 9*z - 2"]


def main():
    A, B = getMatrix(LGS)
    print(A)
    print(B)
    A_invert = invert(A)
    X = matmult(A_invert, B)
    print(X)


if __name__ == '__main__':
    main()
