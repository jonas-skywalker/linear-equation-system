# Python file to calculate a LGS with Gaussian elimination

zero = [0]

def calcStepform(stepmatrix):
    # Stepform example
    # 2 4 2 | 1
    #   1 2 | 2
    #     3 | 3



def calcEquation(equation):
    # This is a function to calculate solution of a simple equation
    if len(equation) > 2:
        for i in range(1, len(equation)-1):
            equation[-1] = equation[-1] - equation[i]
        solution = 1 / equation[0] * equation[-1]
        return solution
    else:
        solution = 1 / equation[0] * equation[1]
        return solution


def scramble(equation):
    for i in range(len(equation) - 2):
        print(len(equation))
        if equation[i] == 0:
            equation.pop(i)


stepmatrix1 = [[1* x3, -1 * x2, 2 * x1, 0],
               [-1, -2, 0],
               [-6, 3]]

matrix1 = [[1, -1, 2, 0],
           [0, -1, -2, 0],
           [0, 0, -6, 3]]


print(calcStepform(stepmatrix1))
# calcEquation([1, 2, 3, 4])
# print(calcEquation(equation))
