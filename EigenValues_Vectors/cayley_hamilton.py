"""
This code explains use case of cayley hamiltion theorem
and how it is used to solve complex problems related to 
matrix

Question
--------
Cayley-Hamilton Theorem states that a square matrix satisfies its own
characteristic equation. Consider a matrix
A = [[-3, 2], [-1, 0]]
Find A**9

Solution
-------
Finding A**9 is hectic if one needs to calculate manually but this task 
is made easy by cayley

Step 1: Calculate characteristic equation
Step 2: Replace lambda with the matrix A
Step 3: Use the below properties to complete the task
		A*A^-1 = I
		A*I = A
"""

import numpy as np
import sympy as sym
from sympy import Eq
from sympy.solvers import solve

Matrix_A = np.array([
           [-3, 2],
	       [-1, 0]
	       ])
greek_lambda =[chr(code) for code in range(955,956)]
greek_lambda = sym.Symbol(greek_lambda[0])
A = sym.Symbol('A')
y = sym.Symbol('y')
I = sym.Symbol('I')
identity_matrix_2 = np.identity(2)
greek_lambda_into_identity_matrix = greek_lambda*identity_matrix_2

matrix_a_minus_lambda_with_identity = Matrix_A \
                                      - greek_lambda_into_identity_matrix

a = matrix_a_minus_lambda_with_identity[0][0]
b = matrix_a_minus_lambda_with_identity[0][1]
c = matrix_a_minus_lambda_with_identity[1][0]
d = matrix_a_minus_lambda_with_identity[1][1]

determinant_of_matrix = a*d-b*c
# In actual A is Matrix_A
equation = Eq(y, determinant_of_matrix.subs(greek_lambda, A))
"""
for cayley theoremm, equation =0
"""
result_cayley =equation.subs(y, 0)
"""
Where A**2+3**A+2*I is L.H.S
      0 = R.H.S
"""       
simplified_equation_cayley = Eq(0, A**2+3**A+2*I) # solving result_cayley

"""
To calculate A**9
-----------------
From the results of simplified_equation_cayley we have

A**2+3**A+2*I = 0
A**2 = -3A-2I
A^4 = (-3A-2I)*(-3A-2I)
    = 9A^2 + 4I + 12A 
    = 9(-3A-2I) + 12A + 4I
    = -27A-18I+12A +4I
    =  -15A-14I

A*8 = A^4^2
    = (-15A-14I)*(-15A-14I) 
    = 225A**2 + 196I + 420A
    = 225(-3A-2I) + 196I + 420A
    = -675A - 450I + 196I + 420A
    = -255A- 254I

A**9 = (-255A- 254I)*A
     = -255A**2-254A
     = -255(-3A-2I) - 254A  
     =  765A-254A+510I
     =  511A + 510I

"""
A_power_nine = 511*A + 510*I       
print("Result of A raised to power 9 is: {}".format(A_power_nine))
# Putting A as Matrix_A and I as idenity matrix
# we have taken identity matrix of order 2 as A matrix is also of order 2
Result_after_real_subs = 511*Matrix_A + 510*np.identity(2)
print("Result after real subsitution of Matrix A and I is:\n{}".format(
	                                            Result_after_real_subs)
                                                )