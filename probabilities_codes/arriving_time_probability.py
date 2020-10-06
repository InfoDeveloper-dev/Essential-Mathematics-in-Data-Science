"""
This code aims to find the probability of travelling by some medium when event of 
reaching office is already happened

Question
--------
A person goes to office either by car, scooter, bus or train probability of which being
1/7, 3/7, 2/7 and 1/7 respectively.Probability that he reaches office late, if he takes car, 
scooter, bus or train is 2/9, 1/9, 4/9 and 1/9/ Given that he reached office in time, then 
what is the probability that he travelled by a car.
IIT 2005
"""

"""
Solution
Skills required: Conditional Probability

E = he reached office in time	

** P(C) =1/7 where C denotes car
P(reaching late due to car) = 2/9 and hence P(on time because of car) = 7/9
SO P(reaching office on time when person chooses car) = P(on time because of car)*P(C) \
according to conditional probability

** P(S) = 3/7 where S denoted Scotter
P(reaching late due to scotter) = 1/9 and hence P(on time because of scotter) = 8/9
So P(reaching office on time when person chooses scotter) = P(on time because of scotter)*P(S) \
according to conditional probability

** P(B) = 2/7 where B denoted Bus
P(reaching late due to bus) = 4/9 and hence P(on time because of BUS) = 5/9
So P(reaching office on time when person chooses bus) = P(on time because of bus)*P(B) \
according to conditional probability

** P(T) = 1/7 where T denoted Train
P(reaching late due to train) = 1/9 and hence P(on time because of train) = 8/9
So P(reaching office on time when person chooses train) = P(on time because of train)*P(T) \
according to conditional probability
"""
import fractions

prob_car = fractions.Fraction(1, 7)
prob_scotter = fractions.Fraction(3, 7)
prob_bus = fractions.Fraction(2, 7)
prob_train = fractions.Fraction(1, 7)

prob_reaching_time_car = fractions.Fraction(7, 9)
prob_office_time_intersection_car = prob_reaching_time_car*prob_car 


prob_reaching_time_scotter = fractions.Fraction(8, 9)
prob_office_time_intersection_scotter = prob_reaching_time_scotter*prob_scotter

prob_reaching_time_bus = fractions.Fraction(5, 9)
prob_office_time_intersection_bus = prob_reaching_time_bus*prob_bus

prob_reaching_time_train = fractions.Fraction(8, 9)
prob_office_time_intersection_train = prob_reaching_time_train*prob_train

total_outcome = prob_office_time_intersection_car+ prob_office_time_intersection_scotter \
                + prob_office_time_intersection_bus + prob_office_time_intersection_train


# prob_car_when_reached_office_happened = (prob_office_time_intersection_car)/(total_outcome)
print('probability of time intersection car is :{} divided by total outcome is:{} = {}'.format(
	                                  prob_office_time_intersection_car, total_outcome, 
	                                  prob_office_time_intersection_car / total_outcome)
                                      )




