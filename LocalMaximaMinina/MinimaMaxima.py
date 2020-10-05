"""
This code is divided into two parts
Part 1: Plotting the curve whose local maxima or minima is to found
Part2 : Finding the local minima or maxima using derivatives
"""
import matplotlib.pyplot as plt # import library for plotting 
import sympy as sym
from sympy import solve
# Implementing Part 1 
# Solving for equation x**3-3*x+2
class YValues:
    # *input_values means tuple object (single star)
    # if two stars, it means dictionary
	def __init__(self, *input_values):
		self.input_values = input_values
	"""
    Input values are -1,-2,1,2,3
    Equation is y = x**3-3*x+2
    Function get_y_values is used to get the output
	"""
	def get_y_values(self):
		output_values = list()
		for each_input in self.input_values:
			each_output = each_input**3-3*each_input+2
			output_values.append(each_output)
		output_values_tuple = tuple(output_values)
		return output_values_tuple	

# creating the object of the class
x_value = (-1,-2,1,2,3)
y_values_object = YValues(-1,-2,1,2,3)
# getting the output using get_y_values function 
y_values = y_values_object.get_y_values()
# plotting the values in the graph
plt.plot((-1,-2,1,2,3), y_values, color='green', linewidth = 2, marker='*', markerfacecolor='#ffdab9', markersize=2)
plt.xlabel('Input Values')
plt.ylabel('Ouput Values')
plt.title('Plotting Equation of Curve y = x**3-3*x+2')
plt.grid(True)

for x,y in zip(x_value, y_values):
	plt.text(x,y,'{},{}'.format(x,y))
	
plt.savefig('curve.png', bbox_inches='tight')
"""
Part 2: For calculating the local minima or maxima we need to \
find those critical value from inout variable where slope of \
curve or slope of tangent or derivate is zero. In other words \
slope is horizontal at those points
SymPy is a Python library for symbolic mathematics.
"""
# declare a variable that is used as input variable for the function
x = sym.Symbol('x')
first_derivate = sym.diff(x**3-3*x+2)
sol = solve(first_derivate)
print("Number of critical values are : {}".format(len(sol)))
print()
first_critical_value = sol[0]
second_critical_value = sol[1]
"""
Now we got two values named as \
first critical value 
second critical value
To find which value corresponds to local minima or maxima calculate \
second derivate of the function
"""
second_derivate = sym.diff(first_derivate)
# put the first critical value in above
first_output_second_derivate_first_critical_value = second_derivate.subs(x, first_critical_value)
print("Value of function after substituting first critical value {} in second derivative is : {}".format(first_critical_value,first_output_second_derivate_first_critical_value))
print()
second_output_second_derivate_first_critical_value = second_derivate.subs(x, second_critical_value)
print("Value of function after substituting second critical value {} in second derivative is : {}".format(second_critical_value,second_output_second_derivate_first_critical_value))
"""
Some inferences from above:
if answer to second derivate comes out to postive then that critical\
point is point of local minima
if answer to second derivate comes out to be negative then that critical \
point is point of local maxima
"""
LocalMinima = second_critical_value
LocalMaxima = first_critical_value
print()	
print("Local Minima of the function x**3-3*x+2 is {}".format(LocalMinima))
print()	
print("Local Maxima of the function x**3-3*x+2 is {}".format(LocalMaxima))
"""
Calculating the maximum and minimum value of the function
"""
exp = x**3-3*x+2
Minimum_value = exp.subs(x,LocalMinima)
Maximum_value = exp.subs(x,LocalMaxima)
print("Minimum Value of function x**3-3*x+2 is {}".format(Minimum_value))
print()
print("Maximum Value of function x**3-3*x+2 is {}".format(Maximum_value))
