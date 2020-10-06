"""
Aim of the program is to find the probability of drawing balls without replacement

Question
========

A bag contains 12 red balls 6 white balls. Six balls are drawn one by one 
without replacement of which at least 4 balls are white. Find the probability 
that in the next two drawn exactly one white ball is drawn. (IIT-2004) 

"""

"""
Skills used
-----------
Conditional probability

Solution
--------
Given that atleast 4 balls are white which also means 5 balls can also be white \
and 6 balls can also be white. So we can have three variables to represent that

A = exactly 4 balls are white
B = exactly 5 balls are white
C = exactly 6 balls are white

To find the event that in the next two draw exactly one ball is white which also means
that one ball is red
E = next two draw exactly one ball is white

P(E) = P(E Intersection A) + P(E Intersection B) + P(E Intersection C)

Applying the conditional probability

P(E Intersection A) = P(E/A).P(A)
P(E Intersection B) = P(E/B).P(B)
P(E Intersection C) = P(E/C).P(C)

P(E) = P(E/A).P(A) + P(E/B).P(B) + P(E/C).P(C)

We have used combination becuase we need to choose items out of total items

P(A) = C(6, 4)*C(12, 2)/C(18, 6) Where C means combination
P(E/A) = C(2, 1)*C(10, 1)/C(12, 2)

P(B) = C(6, 5)* C(12, 1) / C(18, 6)
P(E/B) = C(1,1)*C(11,1)/C(12,2)

we are not considering P(E/C).P(C) because P(C) contains all six white balls and hence P(E/C) cannot take place \
as it required atleast on one white ball

P(E) = C(6, 4)*C(12, 2)/C(18, 6) * C(2, 1)*C(10, 1)/C(12, 2) + C(1,1)*C(11,1)/C(12,2) * C(6, 5)* C(12, 1) / C(18, 6) 
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


factorial_of_six = factorial_of_number(6)
factorial_of_four = factorial_of_number(4)
factorial_of_twelve = factorial_of_number(12)
factorial_of_two = factorial_of_number(2)
factorial_of_six = factorial_of_number(6)
factorial_of_ten = factorial_of_number(10)
factorial_of_eighteen = factorial_of_number(18)
factorial_of_five = factorial_of_number(5)
factorial_of_one = factorial_of_number(1)
factorial_of_eleven = factorial_of_number(11)
"""
combination(n,r) = n!/(n-r)!r!
calculating the P(A) using below
"""
comb_six_out_of_eighteen =  factorial_of_eighteen/(factorial_of_twelve*factorial_of_six)
comb_two_out_of_twelve = factorial_of_twelve/(factorial_of_ten*factorial_of_two)

comb_four_out_of_six = factorial_of_six/(factorial_of_four*factorial_of_two)
prob_A = (comb_four_out_of_six*comb_two_out_of_twelve)/comb_six_out_of_eighteen

# caculating P(B) using the below data
comb_of_five_out_of_six = factorial_of_six/(factorial_of_one*factorial_of_five)
comb_of_one_out_of_twelve = factorial_of_twelve/(factorial_of_one*factorial_of_eleven)
prob_B = (comb_of_five_out_of_six*comb_of_one_out_of_twelve)/comb_six_out_of_eighteen

# calculating probability of event provided A is already occured
comb_of_one_out_of_two = 2 # C(n, 1) = n
comb_of_one_out_ten = 10
prob_of_event_when_a_occured = (comb_of_one_out_of_two*comb_of_one_out_ten)/comb_two_out_of_twelve

# calculating probability of event when B is already occured
comb_of_one_out_of_one = 1 # C(n, 1) = n
comb_of_one_out_of_eleven = 11
prob_of_event_when_b_occured = (comb_of_one_out_of_one*comb_of_one_out_of_eleven)/comb_two_out_of_twelve

# caculating Event E as below
prob_event = (prob_of_event_when_a_occured*prob_A) + (prob_of_event_when_b_occured*prob_B)
print("Probability that in last two draws exactly one is white is: {}".format(round(prob_event, 2)))
