"""
This program aims to solve the problem of error in received digit 
using possion distribution

Parameters of Possion distribution
=================================
p probability of success
n = total
x = random variable which is found in the last line of the statement
m = mean

P(X=x) = (e^-m)*(m^x)/x!

"""

"""
Question

A transmission channel has per digit error with probabilty = 0.01. Calculate \
probability of more than 1 error in 10 received digits.

P(X>1) = 1-(P(X=0) + P(X=1))

"""
import math

n = 10
p = 0.01
m = n*p
exponent = -m

prob_x_zero = (math.exp(exponent)*m**0)/math.factorial(0)
prob_x_one = (math.exp(exponent)*m**1)/math.factorial(1)

overall_prob = 1-(prob_x_zero + prob_x_one)
print("Probability of more than 1 error in 10 received digit is :{}".format(
	                                                  round(overall_prob,4))
                                                      )