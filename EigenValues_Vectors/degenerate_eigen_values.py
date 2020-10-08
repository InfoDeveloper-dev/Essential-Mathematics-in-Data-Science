"""
Aim of this code to calculate degenerate eigen values \
Degenerate means same eigen values
Degeneracy means the number of same eigen values
"""

"""
Question
========

The degenerate eigen value of the matrix M = [[4, -1, -1], [-1, 4, -1], \
                                             [-1, -1, 4]] is
"""
import numpy as np
import sympy as sym
import math
import CubicEquationSolver

Matrix_M = np.array([
	[4, -1, -1], 
	[-1, 4, -1], 
	[-1, -1, 4]
	])

greek_lambda =[chr(code) for code in range(955,956)]
greek_lambda = sym.Symbol(greek_lambda[0])

# calculating determinant of matrix
determ_Matrix_M = np.linalg.det(Matrix_M)
determ_Matrix_M = math.floor(determ_Matrix_M)
print("determinant of Matrix is: \n{}".format(determ_Matrix_M))
print('-'*30)

# calculating the diagonal sum of matrix
diagonal_elements_nparray = Matrix_M.diagonal()
sum_diagonal_elements = int(sum(diagonal_elements_nparray))
print("Sum of diagonal elements is:\n{}".format(sum_diagonal_elements))
print('-'*30)

# calculating diagonal minors
diagonal_minor1_matrix = np.array([
                         [4, -1],
                         [-1, 4]
                         ])
determ_minor1 = int(np.linalg.det(diagonal_minor1_matrix))
# minor 2 calculation
diagonal_minor2_matrix = np.array([
                         [-1, -1],
                         [-1, 4]
                         ])
determ_minor2 = int(np.linalg.det(diagonal_minor2_matrix))
# minor 3 calculation
diagonal_minor3_matrix = np.array([
                         [4, -1],
                         [-1, 4]
                         ])
determ_minor2 = int(np.linalg.det(diagonal_minor3_matrix))

print("First minor diagonal is: {}".format(determ_minor1))
print("Second minor diagonal is: {}".format(determ_minor2))
print("Third minor diagonal is: {}".format(determ_minor2))
print('-'*30)

np_concatenate_values = np.hstack([
	  determ_minor1, determ_minor2, 
	  determ_minor2
	  ])

# sum of diagonal minors
sum_of_diagonal_minors = int(sum(np_concatenate_values))
print("Sum of diagonal minors is: {}".format(sum_of_diagonal_minors))
print('-'*30)
# writing the equation to be solved
equation_to_be_solved = greek_lambda**3 - greek_lambda**2*sum_diagonal_elements \
                        + greek_lambda*sum_of_diagonal_minors - determ_Matrix_M
# use cubic solver method
eigen_values = CubicEquationSolver.solve(1, -12, 45, -50)
eigen_values_list = eigen_values.tolist()

# degenerate are thos eigen values which are same 
degenerate_list = list()
simple_list = list()
for element in eigen_values_list:
	if eigen_values_list.count(element) > 1:
		degenerate_list.append(element)
	else:
		simple_list.append(element)	

print("Degenerate eigen value list is:\n{}".format(degenerate_list))
print("Simple eigen value list is:\n{}".format(simple_list))
print("Degenerate eigen value is:\n{}".format(int(degenerate_list[0])))
print("Degeneracy is:\n{}".format(len(degenerate_list)))
