from sympy import *


LGS = ["6*w - 1*x + 1*y - 12*z + 5",
       "6*w - 2*x + 2*y - 8*z - 8",
       "3*w + 0*x + 2*y - 4*z - 5",
       "3*w - 1*x + 0*y - 4*z - 9"]

w, x, y, z = symbols('w, x, y, z')
A, B = linear_eq_to_matrix(LGS, (w, x, y, z))
A_inverse = A.inv()
X = A_inverse * B

print(X)
