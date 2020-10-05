"""
This code aims at finding the probability of passing the exam based on below conditions

Question
--------
For a student to qualify, he must pass at least two out of three exams. 
The probability that he will pass the 1st exam is p. If he fails in one of the exams, 
then the probability of his passing in the next exam, is p/2 otherwise it remains the same.
Find the probability that he will qualify. (IIT JE-2003)
"""

"""
To solve this question let us write the total conditions possible

conditions = PPP + PPF + PFP + FPP

Let us solve each condition

PPP = p*p*p = p**3
PPF = p*p*(1-p) = p**2-p**3
PFP = p*(1-p)*p/2 = 1/2(p**2*(1-p)) = 1/2*(p**2-p**3) = p**2/2-p**3/2
FPP = (1-p)*p/2*p = 1/2*(p**2)*(1-p) = 1/2*(p**2)-p**3/2

Overall_result =  p**3 + p**2-p**3 + p**2/2-p**3/2 + 1/2*(p**2)-p**3/2
               =  2*p**2 - p**3
"""

import sympy as sym
p = sym.Symbol('p')

all_pass = p**3
first_second_pass_third_fail = p**2-p**3
first_third_pass_second_fail = 1/2*(p**2-p**3)
second_third_pass_first_fail = 1/2*(p**2-p**3)

prob_qualify = all_pass + first_second_pass_third_fail \
               + first_third_pass_second_fail + second_third_pass_first_fail

print("probability that student will qualify is: {}".format(prob_qualify))


