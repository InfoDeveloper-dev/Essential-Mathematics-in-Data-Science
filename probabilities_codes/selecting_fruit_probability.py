"""
Aim is to select fruit out of list of fruit based on some conditions
Problem is solved using bayes theorem
"""
import numpy as np
import pandas as pd

array_fruits = np.array([
    [400, 100, 350, 150, 450, 50],
    [0, 300, 150, 150, 300, 0],
    [100, 100, 50, 50, 50, 150]
    ])
total_fruits= 1000
total_banana = 500
index_values = ['banana', 'orange', 'apple']
column_values = ['Long', 'Not Long', 'Sweet', \
                'Not Sweet', 'Yellow', 'Not Yellow']

df_fruits = pd.DataFrame(data = array_fruits,  
                  index = index_values,
                  columns = column_values  
                  ) 
# to find probability that fruit is banana given that it is long, sweet and yellow
"""
This can be solved using bayes theorem.
P(A/B) = P(A Intersection B)/P(B)
       = P(B Intersection A)/P(B)  

P(B Intersection A) = P(B|A).P(A)
 
P(A/B) = P(B|A).P(A)/P(B)

This is also categorized into Joint Probability

P(B/l,s,y) = P(B intersection l,s,y)/P(l,s,y)

Since events are independent of each other 

P(l,s,y) = P(l).P(s).P(y)

P(B intersection l,s,y) = P(l,s,y intersection B)
                         = P(l, s, y|B).P(B)
                         = P(l|B).P(s|B).P(y|B).P(B)

P(B/l,s,y) = P(l|B).P(s|B).P(y|B).P(B)/P(l).P(s).P(y)
where P(B/l,s,y) is called Posterior Probability or Class given Data
      P(B) is called Class Prior
      P(l|B).P(s|B).P(y|B) is called Data likelihood or Data given class
      P(l).P(s).P(y) is called Data Prior (Marginal)
"""

long_col_sum = df_fruits['Long'].sum(skipna = True) 
not_long_col_sum = df_fruits['Not Long'].sum(skipna = True)
sweet_col_sum = df_fruits['Sweet'].sum(skipna = True)
not_sweet_col_sum = df_fruits['Not Sweet'].sum(skipna = True)
yellow_col_sum = df_fruits['Yellow'].sum(skipna = True)
not_yellow_col_sum = df_fruits['Not Yellow'].sum(skipna = True)
sum_each_column = df_fruits.sum(axis=1) 

sum_banana_row_wise = df_fruits.sum(axis=1)[0]
sum_orange_row_wise = df_fruits.sum(axis=1)[1]
sum_apple_row_wise = df_fruits.sum(axis=1)[2]

prob_long = long_col_sum/total_fruits
prob_sweet = sweet_col_sum/total_fruits
prob_yellow = yellow_col_sum/total_fruits

long_banana = df_fruits['Long'][0]
prob_long_given_banana = long_banana/long_col_sum

sweet_banana = df_fruits['Sweet'][0]
prob_sweet_given_banana = sweet_banana/sweet_col_sum

yellow_banana = df_fruits['Yellow'][0]
prob_yellow_given_banana = yellow_banana/yellow_col_sum

prob_banana = total_banana/total_fruits

prob_long_sweet_yellow_banana = (prob_banana*prob_long_given_banana \
                  	*prob_sweet_given_banana*prob_yellow_given_banana) \
                        /(prob_long*prob_sweet*prob_yellow)

print("probability of banana given that it is long, sweet and yellow:{}".format(
	                                          prob_long_sweet_yellow_banana)
                                                  )                    
                     
