"""
Aim of the experiment

To find the probability of getting atleast one head when three \
coins are tossed simultaneously

Question
--------
If three coins are tossed simultaneously, the probability of \
getting atleast one head is

These question can be solved using binomial distribution because of \
following reasons 

1.) Each trail or experiment has two outcomes (head or tail) (discrete outcome)
2.) Each trail is statistical independent
3.) Probability of outcome of any trail is fixed over time

Mathematical formulation for Binomial distribution

P(X=x) = C(n, x)(success)**x (failure)**n-x

where n is total 
      x is seen from the questions 

P(getting atleast one head)= 1-P(NO HEAD)
P(no head or x= 0) = C(3, 0)*(0.5)**0*(0.5)**3      
"""

# function which will calculate factorial of number
def factorial_of_number(num):
# factorial of 0 is always one	
	if num ==0:
		return 1
# factorial of negative number does not exist
	elif num<0:
		return 0
	else:
		fact = 1
		while(num>=1):
			fact = fact*num
			num = num-1
		return fact	

fact_of_three = factorial_of_number(3)
factorial_of_zero =factorial_of_number(0)
comb_of_zero_out_three = fact_of_three/(factorial_of_zero*fact_of_three)

prob_atleast_one_head = 1 - comb_of_zero_out_three*0.5**0*0.5**3
print("probability that atleast one head:\n{}".format(
	                        prob_atleast_one_head)
                                )
