"""
This code aims to dicuss about probability of drawing coin fair and biased.

Let is understand the code with the help of example
---------------------------------------------------
A box contain N  coins, m  of which are fair and rest are biased. The probability of getting a head 
when a fair coin is tossed is 1/2, while it is 2/3 when a biased coin is tossed. A coin is drawn from the 
box at random and is tossed twice. The first time it shows head and the second time it shows tail. 
The probability that the coin drawn is fair is
Mathematics-2002 IIT JE 
"""

"""
Solution
--------
E = Coin is drawn and first time it shows head and second time it shows tail
F = Coin drawn is Fair
F' = Coin drawn in biased

Both the events are written and now let us write what to find
P(F/E) i.e probabilty of drawing fair coin given that event has occured

We will apply Bayes theorem to solve this problem

P(F/E) = P(F intersection E)/P(E)

P(F intersection E) = P(E intersection F)

P(E intersection F) = P(E/F).P(F)
P(E) = P(E/F).P(F) + P(E/F').P(F')

P(F) =m/N
P(F') = N-m/N
P(E/F) = (1/2)*(1/2)
P(E/F') = (2/3)*(1/3)

P(F/E) = (1/2)*(1/2)*(m/N)/((1/2)*(1/2)*(m/N)+(2/3)*(1/3)*(N-m/N))
"""

import sympy as sym
m = sym.Symbol('m')
N = sym.Symbol('N')
prob_of_fair_coin = m/N
prob_of_bias_coin = (N-m)/N
prob_event_fair_is_already_occured = 1/4
prob_event_bias_is_already_occured = 2/9
# calculatting numerator and denominator
numerator = prob_event_fair_is_already_occured*prob_of_fair_coin
denominator = numerator + prob_event_bias_is_already_occured*prob_of_bias_coin
# calculating probability of fair coin when event has already occured
prob_fair_when_event_occured = numerator/denominator
print("probability of fair coin when event has already occured {}".format(prob_fair_when_event_occured))
