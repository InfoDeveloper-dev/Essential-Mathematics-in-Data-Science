"""
This code aims to find the probability with replacement one by one \
as two numbers are selected from six numbers.

Let us focus on the question which is described below
-----------------------------------------------------
Two numbers are selected randomly from the set S={1,2,3,4,5,6} \
without replacement one by one. The probability that minimum of the two number 
is less than 4 
IIT Mathematics Screening 2003
"""

"""
Solution
========
Since when one number is selected randomnly from the set, number of ways are 6
but since there is no replacement hence for the second case numbers of ways remains 5
According to the Multiplication of principle of counting, total sample space is 6*5=30
According to the statement when minimum of two numbers is calculated it must be less than 4 \

To solve these let us define two sets such that these sets satisfies the above mentioned conditions
set a ={1,2,3} and set b = {4,5,6}

Possible options from set a could be (1,2), 1,3) and it could be (2,1) also and hence for selecting \
two numbers from set a, it is the problem of permutation not combinations which is P(3,2) 

** When the order does matter it is a Permutation. **
** When the order doesn't matter, it is a Combination.**

Possible option when chosing first number from set a and second number from set b are as below 
(1,4), (1,5), (1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)
Possible option when chosing first number from set b and second number from set a are as below
(4,1),(4,2),(4,3),(5,1),(5,2),(5,3),(6,1),(6,2),(6,3)

Total possible out comes for the favourable event is = P(3,2) + 18 = 24

Probabilty = Favourable_Event/Sample Space = 24/30=4/5
"""

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

total_sample_space = 30
factorial_3 = factorial_of_number(3)
factorial_1 = factorial_of_number(1)

"""
One need to calculate P(3,2) which is n!/(n-r)! where \
n = 3 
r = 2
"""
permutation_of_2_out_of_3 = factorial_3/factorial_1
# see the explanation at the top in the multistring
favourable_event = permutation_of_2_out_of_3 + 18
proba_of_selecting_2_without_replacement = favourable_event/total_sample_space
print("Probabilty of selecting 2 numbers without replacement is: {}".format(
	                                 proba_of_selecting_2_without_replacement)
                                                                           )
