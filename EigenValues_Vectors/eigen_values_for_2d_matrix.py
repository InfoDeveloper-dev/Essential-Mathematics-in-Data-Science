"""
Aim of the code is 
------------------
To calculate eigen values
matrix = [[4, 1], [1, 4]]

Since, it is a 2 x 2 matrix formula for calculating eigen values \
|A-lambda*I| = 0, 
"""

import numpy as np
import sympy as sym
from sympy.solvers import solve

matrix_a = np.array([
               [4, 1],
               [1, 4]
	           ])

greek_lambda =[chr(code) for code in range(955,956)]
greek_lambda = sym.Symbol(greek_lambda[0])

identity_matrix_2 = np.identity(2)
greek_lambda_into_identity_matrix = greek_lambda*identity_matrix_2

matrix_a_minus_lambda_with_identity = matrix_a \
                                      - greek_lambda_into_identity_matrix

a = matrix_a_minus_lambda_with_identity[0][0]
b = matrix_a_minus_lambda_with_identity[0][1]
c = matrix_a_minus_lambda_with_identity[1][0]
d = matrix_a_minus_lambda_with_identity[1][1]

determinant_of_matrix = a*d-b*c
eigen_values = solve(determinant_of_matrix, greek_lambda)

for i in range(len(eigen_values)):
    print("Eigen value is: {}".format(int(eigen_values[i]))) 