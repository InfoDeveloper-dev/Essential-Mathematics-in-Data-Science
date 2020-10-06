"""
This program aims to find the probability of first one on even thrown when \
fair dice is rolled

Question:
---------
A fair die is rolled. The probability that the first time 1 occurs at the even throw is, 
IIT-2005
"""

"""
Solution
--------

Skills required
---------------
1.) Formulae for probability 
2.) Sum of GP (Geometric Progression)

P(1) = 1/6
P(not 1) = 5/6

One should come in second or fourth or sixth or so on

E = first one on even throw

P(E) = P(not 1)*P(1) + P(not 1)*P(not 1)*P(not 1)*P(1)+ P(not 1)*P(not 1)*P(not 1)*P(not 1)*P(not 1)*P(1)+...........
     = 5/6*1/6 + (5/6)^3*1/6 + (5/6)^5*1/6 + ................
     = 1/6(5/6 + 5/6^3+............)
Inside pattern is Gp and Sum of GP for infinite term if common ratio is less than 1
r = common ratio  = 25/36<1
Sum_of_gp = a/1-r = 5/6/(1-25/36)
P(E) = 1/6*(Sum_of_gp)
"""

import fractions

prob_one= fractions.Fraction(1, 6)
prob_not_one = fractions.Fraction(5, 6)
common_ratio = fractions.Fraction(25, 36)
first_term = fractions.Fraction(5, 6)
sum_gp = first_term/(1-common_ratio)
common_out_from_gp = fractions.Fraction(1, 6) # see the above solution in multistring
probaility_that_first_one_appears_at_even = common_out_from_gp*sum_gp
print("Probability in fraction that first one comes in the even throw is: {}".format(
	                                       probaility_that_first_one_appears_at_even)
                                                                                    )
