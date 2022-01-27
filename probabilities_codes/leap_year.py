# find the probability that leap year has 53 saturdays

# SOLUTION
"""
Leap year has 366 days which means 52 weeks and 2 days
Suppose if 53rd day is monday then leap year will have 53 mon and 53 tuesday
In the same way it can have 53 tuesday and 53 wednesday
In the same way it can have 53 thursday and 53 friday
In the same way it can have 53 friday and **53 saturday**
In the same way it can have **53 saturday** and 53 sunday 
In the same way it can have sunday and 53 monday

Favourable cases are 2
Total cases are 7
Probability is 2/7
"""

sample_space = 7
favourable_cases = 2
probability_of_saturday = favourable_cases / sample_space
print("Probability of leap year having 53 saturdays is...{}".format(probability_of_saturday))