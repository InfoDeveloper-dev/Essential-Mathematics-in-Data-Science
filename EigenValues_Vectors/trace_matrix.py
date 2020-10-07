"""
Two properties of eigen values are explained here with the help of example

property 1: trace of matrix is sum of eigen values of matrix
property 2: determinant of matrix is product of eigen values of matrix
"""

"""
A traceless 4x4 unitary matrix has two eigen values -1 and 1. The other two eigen values are
GATE-2004
"""

"""
Solution
--------
Since it is a 4x4 matrix so eigen values are lambda1, lambda2, lambda3 and lambda4 
given that matrix is unitary as well as traceless hence 

lambda1 + lambda2 + lambda3 + lambda4 = 0

given: value of lambda 1 and lambda 2 are -1 and 1

-1 + 1 + lambda3 + lambda4 = 0

lambda3 = -lambda4

also matrix is unitary and hence |matrix| = 1

|lambda1*lambda2*lambda3*lambda4| = 1
Hence, 

lambda3*lambda4 = 1
"""

import sympy as sym
from sympy.solvers import solve

greek_lambda1 =[chr(code) + '1' for code in (range(955,956))][0]
greek_lambda2 =[chr(code) + '2' for code in (range(955,956))][0]
greek_lambda3 =[chr(code) + '3' for code in (range(955,956))][0]
greek_lambda4 =[chr(code) + '4' for code in (range(955,956))][0]

greek_lambda1 = sym.Symbol(greek_lambda1)
greek_lambda2 = sym.Symbol(greek_lambda2)
greek_lambda3 = sym.Symbol(greek_lambda3)
greek_lambda4 = sym.Symbol(greek_lambda4)

print("First eigen value is: {}".format(greek_lambda1))
print("Second eigen value is: {}".format(greek_lambda2))
print("Third eigen value is: {}".format(greek_lambda3))
print("Fourth eigen value is: {}".format(greek_lambda4))

# for traceless trace is zero
trace = greek_lambda1 + greek_lambda2 + greek_lambda3 + greek_lambda4 

trace_with_values = trace.subs(greek_lambda1, -1)
trace_with_values = trace_with_values.subs(greek_lambda2, 1)

solution = solve(trace_with_values, greek_lambda3)
print("solution is {} = -{}".format(greek_lambda3, greek_lambda4))