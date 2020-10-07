"""
This code aims to understand eigen values and vectors using all the steps \
and practical codes
Credit for understanding the concept 
------------------------------------
https://www.youtube.com/watch?v=h8sg_XBp6VA
"""
import numpy as np
import sympy as sym
import math
import CubicEquationSolver

list_elements = [
                [1, 4, 8], 
                [2, 3, 6],
                [4, 6, 8] 
                ]

list_elements_np = np.asarray(list_elements, dtype=float)
identity_matrix = np.identity(3, dtype = float)

# decimal value for the letter lambda is 955 as covered under unicode representation
greek_lambda =[chr(code) for code in range(955,956)]
greek_lambda = sym.Symbol(greek_lambda[0])
identity_mul_greek_lambda = greek_lambda*identity_matrix

diagonal_elements_nparray = list_elements_np.diagonal()
sum_diagonal_elements = int(sum(diagonal_elements_nparray))
print("Sum of diagonal elements is: {}".format(sum_diagonal_elements))
print('-'*30)
"""
Let us find the diagonal minors
"""
diagonal_minor1_matrix = np.array([[3, 6], [6, 8]])
minor1_diagonal = np.linalg.det(diagonal_minor1_matrix)

diagonal_minor2_matrix = np.array([[1, 8], [4, 8]])
minor2_diagonal = np.linalg.det(diagonal_minor2_matrix)
minor2_diagonal = math.floor(minor2_diagonal)

diagonal_minor3_matrix = np.array([[1, 4], [2, 3]])
minor3_diagonal = np.linalg.det(diagonal_minor3_matrix)
minor3_diagonal = math.ceil(minor3_diagonal)

print("First minor diagonal is: {}".format(minor1_diagonal))
print("Second minor diagonal is: {}".format(minor2_diagonal))
print("Third minor diagonal is: {}".format(minor3_diagonal))
print('-'*30)

np_concatenate_values = np.hstack([minor1_diagonal, minor2_diagonal, minor3_diagonal])
sum_of_diagonal_minors = int(sum(np_concatenate_values))
print("Sum of diagonal minors is: {}".format(sum_of_diagonal_minors))
print('-'*30)

determinant_a = np.linalg.det(list_elements_np)
determinant_a = math.floor(determinant_a)
print("determinant of matrix is: {}".format(determinant_a))
print('-'*30)

equation_to_be_solved = greek_lambda**3 - greek_lambda**2*sum_diagonal_elements \
                        + greek_lambda*sum_of_diagonal_minors - determinant_a
print("Equation to solve value of lambda or eigen values is: {}".format(
	                                               equation_to_be_solved)
                                                                        )
print('-'*82)
print("Result using CubicEquationSolver \n{}".format(
	                                CubicEquationSolver.solve(1, -12, -41, -20)
	                                            ))
print('-'*82)
print("Result using numpy root \n{}".format(
	                                np.roots([1, -12, -41, -20])
	                                   ))

# Now let us calculate the eigen vectors corresponding to eigen values
first_eigen_value = CubicEquationSolver.solve(1, -12, -41, -20)[0]
first_eigen_value_round = round(first_eigen_value, 2)
print('-'*32)
print("First eigen value after solving cubic equation is: {}".format(first_eigen_value_round))

matrix_after_eigen_value_subs = [
                		[1-first_eigen_value_round, 4, 8], 
                		[2, 3-first_eigen_value_round, 6],
                		[4, 6, 8-first_eigen_value_round] 
                		]

print("matrix after subtracting first eigen value from its diaginal is:\n{}".format(
	                                                matrix_after_eigen_value_subs)
                                                                                 )
print('-'*65)
"""
we are now solving equation AX=0
where X=[x1, x2, x3]
we will solve it using cramers rule
"""
x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')
x3 = sym.Symbol('x3')

eigen_vectors = np.array([x1, x2, x3])
eigen_vectors = np.reshape(eigen_vectors,[3, 1])
AX = np.dot(matrix_after_eigen_value_subs, eigen_vectors)
print("Multiplication of Matrix with eigen vectors is:\n{}".format(AX)) 
print('-'*85)
"""
Applying cramer's rule to solve for x1, x2 and x3
"""
matrix_x1 = np.array([
                     [4, 8],
                     [-11.85, 6]
	             ])
x1 = np.linalg.det(matrix_x1)
x1 = math.ceil(x1)

matrix_x2 = np.array([
                     [-13.85, 8],
                     [2, 6]
	             ])
x2 = np.linalg.det(matrix_x2)
x2 = math.ceil(x2)

matrix_x3 = np.array([
                     [-13.85, 4],
                     [2, -11.85]
	             ])
x3 = np.linalg.det(matrix_x3)
x3 = math.floor(x3)

eigen_vector_corr_to_first_eigen = np.hstack([x1, x2, x3])
print("eigen vector corresponds to eigen value {} is:\n{}".format(
	                     first_eigen_value_round, eigen_vector_corr_to_first_eigen)
                                                                 )
"""
Again using cramers rule one can find the eigen vector \
corresponding to other eigen values also
"""
