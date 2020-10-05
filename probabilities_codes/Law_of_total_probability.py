"""
This programs aims to explain Law of Total Probability
Two conditions for applying law
   1.) Events are mutually  exclusive which means that both the events cannot occur simultaneously
   2.) Events are mutually exhaustive which means atleast one of the event necessarily occurs \
       when the experiment is performed
Question is taken from IIT Mains 2001 JEE Mathematics which is as below
========
An urn contains m white and n black balls. A ball is drawn at random \
and is put back into the um along with k additional balls of the same colour \
as that of the ball drawn. A ball is again drawn at random. what is the  \
probability that second ball drawn is white
"""

"""
Some ideas before proceeding to solution
Let us check whether events which is drawing a white or black ball is mutually exclusive or not
if one draws white ball at a time he cannot draw black ball at the same time and hence
event of drawing white ball or black ball is mutually exclusive

Let us check whether events are mutually exhaustive or not. To complete the experiment either black or 
white ball is drawn.
"""
"""
Defining the events 
Event that first ball drawn is white is w1
Event that first ball drawn is black is b1
Event that second ball drawn is white is w2

Probability means event/total_outcomes
"""
"""
values of m,n and k are randomnly taken to make the program
"""
m = 5
n=7
k=3
prob_w1= m/(m+n)
prob_b1 = n/(m+n)
prob_w2_when_w1_already_ocurred = (m+k)/(m+n+k)
prob_w2_when_b1_already_ocurred = m/(m+n+k) 
# According to Law of Total Probability
prob_w2 = prob_w1*prob_w2_when_w1_already_ocurred+prob_b1*prob_w2_when_b1_already_ocurred
print("probability that second ball drawn is white is: {}".format(prob_w2))
