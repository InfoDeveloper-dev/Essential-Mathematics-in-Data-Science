"""
This questions aims to find the probability of hitting the target by some one

Question is as below
--------------------

A is targeting to B, B and C are targeting to A. probability of hitting the target by A, B and C are 
2/3, 1/2 and 1/3, respectively. If A is hit, then find the Probability that B hits the target and C does not.
IIT-JE 2003
"""

"""
Solution
--------
P(A) = probability that A will hit B = 2/3
P(B) = probability that B will hit A = 1/2
P(C) = probability that C will hit A = 1/3
B' = Compliment of B
C' = Compliment of C

E =  A is hit

It is given in the question that A is hit by B and C
P(E) = P(BUC) = 1-P(B' intersection C')

Since B and C are independent for each other, hence \
P(B' intersection C') = P(B')*P(C') = 1/2*2/3 = 1/3

P(E) = 1-1/3 = 2/3

P(B intersection C'/E) = P(B).P(C')/P(E) = (1/2*2/3)/2/3 = 1/2
"""

prob_a_hits_b = 2/3
prob_b_hits_a = 1/2
prob_c_hits_a = 1/3
prob_event_that_a_is_hit = 2/3
# using Bayes theorem
prob_b_hits_a_not_c = prob_b_hits_a*(1-1/3)/(prob_event_that_a_is_hit)  
print("probability that b not c hits target A is: {}".format(round(prob_b_hits_a_not_c, 2)))