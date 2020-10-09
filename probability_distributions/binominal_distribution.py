"""
Calculate probability that n lines are busy when \
prob. of success and failure is given as well as total is also given

In such cases one need to apply binomial distribution
"""

"""
Question
--------
probability that at any moment one telephone line out of 10 will be busy is 0.2
Find the probability that 5 lines are busy
"""

total = 10
# p denotes success which is telephone line busy
prob_tele_busy = 0.2
prob_not_busy = 0.8
"""
x is the random variable which is given in the statement
in this question x = 5

According to the binomial distribution
x= 5

P(X=x) = C(total, x)*(prob_tele_busy)**x*(prob_not_busy)**(total-x) 

C(n, r) is combination which is n!/(n-r)!r!
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
					
fact_of_ten = factorial_of_number(10)
fact_of_five = factorial_of_number(5)
comb_of_five_out_of_ten = fact_of_ten/(fact_of_five*fact_of_five)
prob_that_five_lines_busy = comb_of_five_out_of_ten*(prob_tele_busy) \
                            **5*(prob_not_busy)**5
print("According to binomial distribution probability that 5 lines is busy is:\n{}".format(
	                                               round(prob_that_five_lines_busy, 3))
                                                       )                            
