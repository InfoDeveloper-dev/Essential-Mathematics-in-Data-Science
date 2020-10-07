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
