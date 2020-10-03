"""
Problem aims to solve a real time manufacturing industry problem using \
law of total probability. 
One can learn more about law of total probability from the below mentioned link \
https://github.com/InfoDeveloper-dev/Essential-Mathematics-in-Data-Science/blob/master/Law_of_total_probability.py
Let us define the problem as below
"""

"""
In a manufaturing factory parts are made by 3 machines. 
     Machine 1: It makes 40% of the parts (Event1)
     Machine 2: It makes 50 % of the parts (Event2)
     Machine 3: It makes 10% of the parts (Event3)

Given that these three events are mutally exclusive. Out of these three parts
    Machine 1 makes 10 % of the defective
    Machine 2 makes 9 % of the defective
    Machine 3 makes 20 % of the defective

To find: A part is selected at random.what is the probability that it is defective
"""

"""
Solution: 
Given that events are mutally exclusive and let us see whether these are collective exhaustive 
For this we can sum the probability of machine 1, 2 and 3 is 1 and hence covers the full sample space
Now, we can go for total probability theorem
"""
prob_machine1 = .4
prob_machine2 = .5
prob_machine3 = .1
prob_def_from_machine1 = .1
prob_def_from_machine2 = .09
prob_def_from_machine3 = .2

prob_defective = prob_machine1 * prob_def_from_machine1 + prob_machine2 * prob_def_from_machine2 + \
                 prob_machine3 * prob_def_from_machine3

print("Probability that part is defective: {}".format(round(prob_defective, 2)))               
