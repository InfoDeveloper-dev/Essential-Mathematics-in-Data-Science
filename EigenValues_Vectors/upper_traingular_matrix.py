"""
This programs aims to solve problem using eigen value property \
for a upper traingular matrix

Properties used
---------------
Eigen values for upper traingular matrix
Eigen values for matrix ^n
Eigen values for matrix * n
Where n is a scalar

Question
--------
The eigen value of (A**4+3*A-2*I),Where A is [[1, 1, 1], [0,  2, ,1], [0, 0, 3]]
are:

Came in
-------
IISC
"""

import numpy as np
import sympy as sym

Matrix_A = np.array([
            [1, 1, 1],
            [0, 2, 1],
            [0, 0, 3]
	    ])
# for upper traingular matrix, eigen values are diagonal elements \
# since there are three rows and three columns hence three eigen values \ 
# are there
greek_lambda1 =[chr(code) + '1' for code in (range(955,956))][0]
greek_lambda2 =[chr(code) + '2' for code in (range(955,956))][0]
greek_lambda3 =[chr(code) + '3' for code in (range(955,956))][0]
# converting them into symbols
greek_lambda1 = sym.Symbol(greek_lambda1)
greek_lambda2 = sym.Symbol(greek_lambda2)
greek_lambda3 = sym.Symbol(greek_lambda3)
# according to the property
greek_lambda1 = 1
greek_lambda2 = 2
greek_lambda3 = 3

print("first eigen value of Matrix A is: {}".format(
	                              greek_lambda1)
                                      )
print("second eigen value of Matrix A is: {}".format(
	                               greek_lambda2)
                                       )
print("third eigen value of Matrix A is: {}".format(
	                              greek_lambda3)
                                      )
print('-'*40)

# using property of eigen value^n
eigen_values_matrix_power_four = (1, 2**4, 3**4)
first_eigen_value_matrix_power_four = eigen_values_matrix_power_four[0]
second_eigen_value_matrix_power_four = eigen_values_matrix_power_four[1]
third_eigen_value_matrix_power_four = eigen_values_matrix_power_four[2]

print("first eigen value of Matrix A**4 is: {}".format(
	           first_eigen_value_matrix_power_four)
                   )
print("second eigen value of Matrix A**4 is: {}".format(
	           second_eigen_value_matrix_power_four)
                   )
print("third eigen value of Matrix A**4 is: {}".format(
	           third_eigen_value_matrix_power_four)
                   )
print('-'*40)
# using scalar mul. property of eigen values
eigen_values_three_times_matrix = (3, 6, 9)
first_eigen_value_matrix_mul_three = eigen_values_three_times_matrix[0]
second_eigen_value_matrix_mul_three = eigen_values_three_times_matrix[1]
third_eigen_value_matrix_mul_three = eigen_values_three_times_matrix[2]

print("first eigen value of Matrix 3*A is: {}".format(
	           first_eigen_value_matrix_mul_three)
                   )
print("second eigen value of Matrix 3*A is: {}".format(
	           second_eigen_value_matrix_mul_three)
                   )
print("third eigen value of Matrix 3*A is: {}".format(
	           third_eigen_value_matrix_mul_three)
                   )
print('-'*40)
# using scalar mul. property of eigen values
# eigen value of identity matrix is 1
eigen_values_two_times_identity = (2, 2, 2)
first_eigen_value_identity_mul_two = eigen_values_two_times_identity[0]
second_eigen_value_identity_mul_two = eigen_values_two_times_identity[1]
third_eigen_value_identity_mul_two = eigen_values_two_times_identity[2]

print("first eigen value of Matrix 2*I is: {}".format(
	           first_eigen_value_identity_mul_two)
                   )
print("second eigen value of Matrix 2*I is: {}".format(
	           second_eigen_value_identity_mul_two)
                   )
print("third eigen value of Matrix 2*I is: {}".format(
	           third_eigen_value_identity_mul_two)
                   )
print('-'*40)
# Now one need to concatenate int into numpy arrays
numpy_matrix_raised_power_four = np.hstack([
        first_eigen_value_matrix_power_four,
        second_eigen_value_matrix_power_four,
        third_eigen_value_matrix_power_four     
	])

numpy_matrix_mul_three = np.hstack([
  first_eigen_value_matrix_mul_three,
  second_eigen_value_matrix_mul_three,
  third_eigen_value_matrix_mul_three
  ])

numpy_identity_mul_two = np.hstack([
  first_eigen_value_identity_mul_two,
  second_eigen_value_identity_mul_two,
  third_eigen_value_identity_mul_two
  ])

print("numpy array of matrix raised to power four is:\n{}".format(
	                           numpy_matrix_raised_power_four)
                                   )
print("numpy array of matrix multiply by three is:\n{}".format(
					numpy_matrix_mul_three)
                                        )
print("numpy array of identity matrix mul by 2 is:\n{}".format(
	                              numpy_identity_mul_two)
                                      )

result = numpy_matrix_raised_power_four \
        + numpy_matrix_mul_three \
        - numpy_identity_mul_two
print("Eigen values of the expression is:\n{}".format(result))        
