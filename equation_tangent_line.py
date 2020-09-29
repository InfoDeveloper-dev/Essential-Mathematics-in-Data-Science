"""
Code is to find the equation of tangent \
passing through the curve y=x**2 at point(1,1)
"""
import sympy as sym
x = sym.Symbol('x')
y = sym.Symbol('y')
y =x**2
x_point=1 # tangent passes curve at point (1,1)
y_point=1 # tangent passes curve at point (1,1)
"""
Slope of curve at a point = Slope of tangent passing through that point
Slope represents change in y with respect to change in x which is also \
called as derivative of y with respect to x
"""
slope_of_curve = sym.diff(y)
print("Slope of curve or slope of tangent is: {}".format(slope_of_curve))
"""
To find slope of curve at a point, substitute that point in the            
slope_of_curve calculated in line 14
"""
Slope_of_curve_after_values = slope_of_curve.subs(x, 1)
print("Slope of curve or slope of tangent after substituation is: {}".format(Slope_of_curve_after_values))
m = Slope_of_curve_after_values # slope is denoted by m, one can use anything
"""
Equation of tangent is y-y1=m(x-x1)
where x1 = 1
y1=1
"""
y_tangent= sym.Symbol('y_tangent')
x_tangent = sym.Symbol('x_tangent')
y_tangent = m*(x_tangent-x_point) + y_point
print("Equation of tangent passiing through point(1,1 on curve is: {}".format(y_tangent))
"""
From the equation of y_tangent which comes out to be 2*x_tangent - 1 \
Compare the above equation with equation of straight line which is y=mx+c
where m = 2 and c or y_intercept is -1
y_intercept is the point line touches y_axis
"""
