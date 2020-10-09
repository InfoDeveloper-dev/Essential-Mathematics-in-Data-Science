"""
Questions on Probability of solving MCQ type questions

Question
--------
In answering a question on a multiple choice test, a student either \
knows or makles a guess. Let 3/4 is the probability that he knows the \
answer and 1/4 be the probability that he guess. Assuming that the student \
who guess the answer will be correct with prob. 1/4 Probability that he knows
the answer given that he answered it correctly??
"""

"""
E = answered it correctly
A = student knows answer
B = student makes guess
E is made of 2 parts
  students knows the answer and sudent makes guess
P(E) = P(E/A).P(A) + P(E/B).P(B)

P(E/A) = 1
P(A) = 3/4
P(E/B) = 1/4
P(B) = 1/4

P(E) = 3/4 + 1/16

To find

P(A/E) = P(A intersection E)/P(E)
       
P(A intersection E) = P(E intersection A)
                    = P(E/A).P(A)
                    = 1*(3/4)
                    = 3/4
"""

from fractions import Fraction 

prob_a_intersection_e = Fraction(3, 4)
prob_event = Fraction(3, 4) + Fraction(1, 16)
prob_of_knows_answer_when_answered_correct = (prob_a_intersection_e) \
                                             /(prob_event)
print("conditional probaility that he knows the answer given that he \
  answered it correctly is:\n{}".format(
  prob_of_knows_answer_when_answered_correct)
  )
