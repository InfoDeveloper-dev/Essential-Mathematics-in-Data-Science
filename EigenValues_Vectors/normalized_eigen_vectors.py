"""
Code explains about normalized eigen vectors

Suppose eigen vectors are[a, b] then 
normalized eigen vectors are [a/sqrt(a**2+b**2), a/sqrt(a**2+b**2)]

Let us explain the concept with the help of code
For a matrix A = [[5, 3], [1, 3]], one of the normalized Eigen vector is \
"""
import numpy as np
import sympy as sym
import math
from sympy.solvers import solve
from sys import exit

matrix_a = np.array([
	           [5, 3],
	           [1, 3]
	           ])

greek_lambda =[chr(code) for code in range(955,956)]
greek_lambda = sym.Symbol(greek_lambda[0])
x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')

identity_matrix_2 = np.identity(2)
greek_lambda_into_identity_matrix = greek_lambda*identity_matrix_2

matrix_a_minus_lambda_with_identity = matrix_a \
                                      - greek_lambda_into_identity_matrix

a = matrix_a_minus_lambda_with_identity[0][0]
b = matrix_a_minus_lambda_with_identity[0][1]
c = matrix_a_minus_lambda_with_identity[1][0]
d = matrix_a_minus_lambda_with_identity[1][1]

determinant_of_matrix = a*d-b*c
print("Determinant of matrix is:{}".format(determinant_of_matrix))
print('-'*50)
eigen_values = solve(determinant_of_matrix, greek_lambda)
eigen_values_int = [int(each) for each in eigen_values]
print("Eigen values are: {}".format((eigen_values_int)))

# let us proceed with first eigen value to find eigen vectors
# since this is 25*2 matrix we have only two eigen values

if len(eigen_values_int) == 2:
	print("proceeding further...........")
else:
	print("Stopping here as condition fails..........")
	exit()	

first_eigen_value = eigen_values_int[0]
print("first eigen value is: {}".format(
	             first_eigen_value)
                     )
"""
let us find eigen vector corresponding to this eigen value
AX= 0 where A is matrix given, X is eigen vector and 0 is null
A = [[5, 3], [1, 3]]
X = [x1, x2]
"""
"""
lambda =1
matrix_a_with_first_eigen_value = np.array([
	                                  [5-lambda, 3],
	                                  [1, 3-lambda]
	                                  ])
"""
matrix_a_with_first_eigen_value = np.array([
	                                  [3, 3],
	                                  [1, 1]
	                                  ])
X = np.array([
	      [x1],
	      [x2]
	     ])
# dot product of A and X
dot_a_x = np.dot(matrix_a_with_first_eigen_value, X)
print("Dot product of matrix with first eigen value {} and X {} is:\n{}".format(
	                            matrix_a_with_first_eigen_value, X, dot_a_x)
                                    )
print('-'*50)
first_simultaneous_equation = dot_a_x[0]
second_simultaneous_equation = dot_a_x[1]

first_simultaneous_equation = first_simultaneous_equation[0]
solution_first_simultaneous_equation = solve(first_simultaneous_equation, x1)

second_simultaneous_equation = second_simultaneous_equation[0]
solution_second_simultaneous_equation = solve(second_simultaneous_equation, x1)

print("Show the first value of eigen vector is: {}".format(
	           solution_first_simultaneous_equation[0])
                   )
print("Show the second value of eigen vector is: {}".format(
	           solution_second_simultaneous_equation[0])
                   )

"""
This implies that x1=-x2 and hence we can choose for x1 we will get x2
suppose x1 = 1
        x2= -1 as x2=-x1
"""
"""
let us verify that above values are right choice or not
we will put in the equation AX
"""

X_calculated = np.array([
	              [1],
	             [-1]
	             ])

dot_a_x_calculated = np.dot(matrix_a, X_calculated)
"""
From the value calculated above, 1 can be taken out
which is A*X=lambda*X
lambda = 1
Hence, 1 and -1 is verified value
"""
normalized_term = math.sqrt(1**2 + (-1)**2)
print("Normalized term is: {}".format(normalized_term))

normalized_eigen_vector = normalized_term*X_calculated
print("Normalized eigen vector is: {}".format(normalized_eigen_vector))
