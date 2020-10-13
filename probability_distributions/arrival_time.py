"""

Question is on arrival time and service time

Probability of system being idle is 1-(arrival time /service time)

Question
========
Arrivals at a telephone both are considered to be poisson with an average time of \
of 10 minutes between arrivals. The length of a phone call is distributed exponentially with \
mean 3 minutes. The probability that an arrival does not have to wait before service
"""

arrival_time_per_hour = 60/10
service_time_per_hour = 60/3

prob_does_not_wait = arrival_time_per_hour/service_time_per_hour
print("Probability that an arrival does not have to wait: {}".format(
	                                           prob_does_not_wait)
                                                   )
