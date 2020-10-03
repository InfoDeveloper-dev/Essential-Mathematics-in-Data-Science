"""
This code will explain use of probability with permutations and combinations
One can get some more example of prob. using the below links
https://bit.ly/2GphLYT
https://bit.ly/2HTXZVO
permutations means arrangement whereas combinations means selecting some items from list
"""

"""
Question is as below and taken from IIT JEE Mathematics 2001 Mains

An unbiased dice with face numbers 1, 2, 3, 4, 5 and 6 is thrown n times. \
list of n numbers showing up is noted. What is the probability that out of 6 \
numbers only three numbers appears in the list
"""

"""
Solution
========
Approach would be we will calculate
----------------------------------- 
  1.) total outcomes
  2.) we will also create number of ways event can happen
prob. of event to happen =   number of ways event can happen/total outcomes
Let us discuss in detail
========================
if a dice is thrown n times, then at each times we have 6 possible outcomes and each time \
or chance is independent of each other, hence total number of outcomes is equal to 6^n \
where n is number of times dice is thrown

Let us calculate number of ways event can happen
we have to choose exactlt three out of 6. This is problem of combinations and hence output is C(6,3)\

possible ways are:3^n where below will also be considered

 There would be two exceptions while implementing this and these are as below
    Exception1: Exactly 2 numbers as outcomes
    Exception1: Exactly 1 number as outcome

Dealing with Exception 1: Exactly 2 numbers as outcomes
So we are selecting 2 out of 3 and hence the result is C(3,2) and now we have to arrange them \
arranging 2 numbers comes with 2^n possibilities and there are 2 ways in which out of these two numbers \
list is represented by only 1 numbers and hence total result is
C(3,2)*(2*n-2)

For arranging one number out of 3 numbers in the list we have only 3 options and hence result is 3
C(6,3)*(3^n- C(3,2)*(2*n-2)-3))
Overall favourable event or event happening is: C(6,3)*(3^n- C(3,2)*(2*n-2)-3))
"""
import sympy as sym


def factorial_of_number(num):
	factorial = 1
	# check if the number is negative, positive or zero
	if num < 0:
	   print("Sorry, factorial does not exist for negative numbers")
	elif num == 0:
	   return 1
	else:
	    for i in range(1,num + 1):
       		factorial = factorial*i
	return factorial	

n = sym.Symbol('n')
total_poss_outcomes = 6**n

six_factorial =factorial_of_number(6)
three_factorial = factorial_of_number(3)
two_factorial = factorial_of_number(2)
"""
formula for combination is \
C(n, r) = n!/(n-r)!*r!
"""
comb_of_six_w_r_t_three = six_factorial/(three_factorial*three_factorial)
comb_of_three_w_r_t_two = three_factorial/two_factorial

three_power_n = 3**n
two_power_n = 2**n

fav_event =  comb_of_six_w_r_t_three*(three_power_n-comb_of_three_w_r_t_two*(two_power_n-2)-3)
total_outcome = total_poss_outcomes
probalilty_of_fav_event = fav_event/total_outcome
print("prob. of event happening is \n", probalilty_of_fav_event)
