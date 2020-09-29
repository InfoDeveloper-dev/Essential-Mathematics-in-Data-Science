"""
Aim is to calculate minima and maxima of below function
y = f(x) = 200-3*x1**2-4*x1+2*x1*x2-5*x2**2+48*x2
"""

"""
Solution
since there are two variable involved in the equation \
we will go with partial differentiation to solve x1 and x2
"""

import sympy as sym
import numpy as np
import math
x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')
y = sym.Symbol('y')
y = 200-3*x1**2-4*x1+2*x1*x2-5*x2**2+48*x2
print("Equation with multi arguments is", y)
print('-'*60)
# partial differentiation with respect to x1
partial_diff_x1 = sym.diff(y,x1)
partial_diff_x2 = sym.diff(y,x2)

print("First order partial differentiation w.r.t x1", partial_diff_x1)
print("First order partial differentiation w.r.t x2", partial_diff_x2)
print('-'*60)
partial_diff_x1_coeff = sym.Poly(partial_diff_x1, x1,x2)
partial_diff_x2_coeff =  sym.Poly(partial_diff_x2, x1,x2)

partial_diff_x1_coeff = partial_diff_x1_coeff.coeffs()
partial_diff_x2_coeff = partial_diff_x2_coeff.coeffs()

"""
Since to find the critical points we know at \
those points the slope of the tangent or the curve
is always horizontal and hence zero so we need to equate these both 
equations equal to zero and solve simaltenously equations
For this we will use numpy array
We are Solving AX=B where x is x1 and X2
A contains coefficients of x1 and x2
B contains constant terms in two  equations
"""

A = np.array([[partial_diff_x1_coeff[0], partial_diff_x1_coeff[1]],
 			  [partial_diff_x2_coeff[0], partial_diff_x2_coeff[1]],
 			  ], dtype='float')

B = np.array([-partial_diff_x1_coeff[2],-partial_diff_x2_coeff[2]])
inverse_of_A = np.linalg.inv(A)
critical_values = np.dot(inverse_of_A, B)

list_critical_values=list()
for i in critical_values:
	value = str(i).split('.')[0]
	list_critical_values.append(int(value))

print("There are {} critical values for the equation".format(len(list_critical_values)))
for i in range(len(list_critical_values)):
	print("critical value is {}".format(list_critical_values[i]))
print('-'*60)	
"""
Now, we cannot say that these critical values are point of local minima or local maxima
In the case of multiple argument function we need to calculate second order direct partial \
derivative and second order cross partial derivative as next step
"""
second_order_direct_partial_derivative_x1 = sym.diff(partial_diff_x1, x1)
second_order_direct_partial_derivative_x2 = sym.diff(partial_diff_x2, x2)

print("Second order direct partial derivative w.r.t x1 is: {}".format(
	                                                               second_order_direct_partial_derivative_x1)
                                                                    )

print("Second order direct partial derivative w.r.t x2 is: {}".format(
	                                                               second_order_direct_partial_derivative_x2)
                                                                    )
print('-'*60)
second_order_cross_partial_derivative_x1 = sym.diff(partial_diff_x2, x1)
second_order_cross_partial_derivative_x2 = sym.diff(partial_diff_x1, x2)

print("Second order cross partial derivative w.r.t x1 is: {}".format(
	                                                               second_order_cross_partial_derivative_x1)
                                                                    )

print("Second order cross partial derivative w.r.t x2 is: {}".format(
	                                                               second_order_cross_partial_derivative_x2)
                                                                    )
print('-'*60)
f11 = second_order_direct_partial_derivative_x1
f22 = second_order_direct_partial_derivative_x2
f12 = second_order_cross_partial_derivative_x1
f21 = second_order_cross_partial_derivative_x2

if f12==f21:
	print("partial_diff_x1 and partial_diff_x2 are continous according to youngs theorem")
print("-"*60)
"""
Show the matrix formed by using these values
"""
matrix_second_order_partial_derivative = np.array([[f11, f12],
                                                  [f21,f22] 
	                                              ], dtype='float')
"""
Now we will calculate first principal minor
second principal minor and so on 
if the alternative symbols appears it means the point (x1,x2) is point of local maxima
if same sign appears it means point(x1,x2) is point of local minimas
first principal minor= f11
second principal minor = determinat of matrix_second_order_partial_derivative or determinant of \
hessain matrix
"""
hessian_matrix = matrix_second_order_partial_derivative
first_principal_minor = f11
determinant_hessain_matrix = np.linalg.det(hessian_matrix)
print("Hessian Matrix is \n", matrix_second_order_partial_derivative)
print('-'*60)
determinant_hessain_matrix = str(determinant_hessain_matrix).split('.')[0]
"""
change the type of both first principal minor and second principal minor to int 
"""
first_principal_minor = int(first_principal_minor)
determinant_hessain_matrix = int(determinant_hessain_matrix)

print("first principal minor is {}".format(first_principal_minor))
print("second principal minor is", determinant_hessain_matrix)

list_of_minors = [first_principal_minor, determinant_hessain_matrix]
list_of_boolean = list()
for i in range(len(list_of_minors)):
	if list_of_minors[i]<0:
		list_of_boolean.append(False)
	else:
		list_of_boolean.append(True)

print("Show boolean result is: {}".format(list_of_boolean))			
print('-'*60)
if False in list_of_boolean and True in list_of_boolean:
	print("Critical value pair {} and {} is a local maxima".format(list_critical_values[0],
                                                                   list_critical_values[1]
		                                                            )
																                                )
else:
	print("Flase")	
