"""
Aim of the experimemt: possible outcomes of a event from an experiment

Question
=======
An experiment has 10 equally likely outcomes. Let A and B be two non-empty events of the experiment. 
If A consists of 4 outcomes, the number of outcomes that B must have so A and B are independent, is
IIT 2008
"""

"""
Solution
========
Skills: Events are independent of each other
Both events are independent and hence P(A Intersection B) = P(A).P(B)
P(A) = 4/10
P(A Intersection B) = 4.P(B)/10
P(B) = p/10
P(A Intersection B) = 4.p/100
where A Intersection B = 2p/10

Let us find the value of p for which the result is an integer

5 or 10 satisfies the result
"""
# importing libraries
import fractions
import sympy as sym
from sympy import sympify

p = sym.Symbol('p')

prob_a = fractions.Fraction(4, 10)
prob_b = p/10
prob_a_intersection_n = prob_a*prob_b
a_intersection_b = 2*p/5
# applying list comprehension
values_of_b_in_list = [a_intersection_b.subs(p,value) for value in range(1,11)]
for index, value in enumerate(values_of_b_in_list):
	if sympify(value).is_integer:
		print("Possible outcome for B event is: {}".format(index+1))
