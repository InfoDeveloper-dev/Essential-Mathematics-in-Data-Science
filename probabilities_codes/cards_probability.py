"""
Some information regarding cards

There are total 
              12 Face cards named as King, Queen and Jack
              16 Honor cards  
              36 Digit Cards
Total there are 52 cards which are divided into 2 categories
              26 Red
              26 Black
26 Red cards are further divided into 2 categories
              13 Heart
              13 Diamond
26 Black cards are further divided into 2 categories
              13 Spade
              13 Club
Question
=======
From a pack of regular playing cards, two cards are drawn at random. What is the probability that \
both cards will be kings if the first card is not replaced

Solution
========

What to choose
==============
Both cards being king so one one is taken out we have no option for replacement

total there are 4 kings in the deck of 52 cards and hence prob of first card being king is 4/52
Second time there will be 3 kings left and total 51 cards and hence prob is 3/51

Overall_prob = 4/52*3/51
"""

from fractions import Fraction

prob_first_card_being_king = Fraction(4, 52)
prob_second_card_being_king = Fraction(3, 51)

prob_both_card_king_without_replace = prob_first_card_being_king \
                                      * prob_second_card_being_king
print("Probability that both cards are king without replacement is: {}".format(
	                                       prob_both_card_king_without_replace)
	                                       )                                       