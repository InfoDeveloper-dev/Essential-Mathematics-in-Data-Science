"""
Code is to update weights to minimize the error
Change of error with respect to weights is calculated \
which is backpropagated
Equation is w1 = w0-learning_rate*gradient_cost_function_with_respect_t0_weights
w1= new weights
w0= previous weight
we did subtraction so that we are moving in the direction opposite to steepest direction \
This is why name is gradient descent
calculation is only restricted to update w5. one can try for other weights also
"""

"""
I am making this program using multllayer perception neural network
Network has one input layer with 2 neurons
            one hidden layer with 2 neurons
            one output layer with 2 neurons
"""
import math


i1 = 0.05  # random value of first input or input at first node in input layer
i2 = 0.10  # random value of first input or input at first node in input layer
b1 = 0.35  # random value of bias which will be used at hidden layer
b2 = 0.60  # random value of bias which will be used at output layer
o1_actual = 0.3     # actual output at node 1 of output layer
o2_actual = 0.5     # actual output at node 2 of output layer
w1 = .10   # weight 1  from i1 to h1 
w2 =.15    # weight 2 from i2 to h1
w3 = .20   # weight 3  from i1 to h2
w4 = .25   # weight 4  from i2 to h2
w5 = .30   # weight 5 from h1 to o1_actual
w6 = .35   # weight 6 from h2 to o1_actual
w7 = .40   # weight 7 from h1 to o2_actual
w8 = .45   # weight 8 from h2 to o2_actual
learning_rate = 0.5

"""
Aim is to calculate the value of o1_actual and o2_actual from the neural network and see how \
much is the difference between actual output and calculated output from neural network
It is also called cost function and aim is to minimize the loss function using gradient descent method
"""
# neuron at h1 contains two parts one is summation and another is activation_function
h1_summation = i1*w1+i2*w2+b1
print(
      "Summation of all incoming values at h1 is: {}".format(h1_summation)
)
# activation function used is standard logistic sigmoid function
h1_activation = 1/(1+math.exp(-h1_summation))
print(
      "Activation after summation at h1 is: {}".format(h1_activation)
)
h2_summation =i1*w3+i2*w4+b1
print('-'*80)
print(
      "Summation of all incoming values at h2 is: {}".format(h2_summation)
)
h2_activation = 1/(1+math.exp(-h2_summation))
print(
      "Activation after summation at h2 is: {}".format(h2_activation)
)
print('-'*80)
o1_summation = h1_activation*w5+h2_activation*w6+b2
print(
      "Summation of all incoming values at o1_actual is: {}".format(o1_summation)
)
o1_predicted = 1/(1+math.exp(-o1_summation))
print("predicted output o1_actual is: {}".format(o1_predicted))
print('-'*80)
o2_summation = h1_activation*w7+h2_activation*w8+b2
print(
      "Summation of all incoming values at o2_actual is: {}".format(o2_summation)
)
o2_predicted = 1/(1+math.exp(-o2_summation))
print(
      "predicted output o2_actual is: {}".format(o2_predicted)
)
print('-'*80)
"""
we have predicted output as well as actual output at o1_actual and o2_actual
Let us calculate loss or cost function
"""
squared_error_E1 = (o1_actual-o1_predicted)**2
E1 = (1/2)*squared_error_E1

squared_error_E2 = (o2_actual-o2_predicted)**2
E2 = (1/2)*squared_error_E2

e_total = E1+E2
print("Total error is: {}".format(e_total))
print('-'*80)
"""
Now we will calculate what is the change in the e_total, if 
we change some value in w5. In simple words \
we are calculating the gradient of e w.r.t w5
we will use chain rule to achieve this step
equation would be partial_diif_of_etotal w.r.t w5 = \
partial_diif_of_o1_summation w.r.t w5 * partial_diif_of_o1_predicted w.r.t o1_summation \
* partial_diif_of_e_total w.r.t o1_predicted
"""
e_total = 1/2*((o1_actual-o1_predicted)**2 + (o2_actual-o2_predicted)**2)
partial_diff_of_e_total_w_r_t_o1_predicted = -(o1_actual-o1_predicted)
print(
      "partial diff of e_total w.r.t o1 predicted is: {}".format
       (partial_diff_of_e_total_w_r_t_o1_predicted)
)
"""
we are calculating partial diff of e_total w.r.t o1 predicted.
Since output is standard logistic sigmoid function  
partial_derivate_of standard logistic sigmoid function = f(x)(1-f(x))
"""
partial_diff_of_o1_predicted_w_r_t_o1_summation = o1_predicted*(1-o1_predicted)
print(
      "partial diff of o1_predicted w.r.t o1_summation is: {}".format
       (partial_diff_of_o1_predicted_w_r_t_o1_summation)
)
"""
we are calculating the partial_diif_of_o1_summation w.r.t w5
o1_summation = h1_activation*w5+h2_activation*w6+b2
partial_derivate of o1_summation w.r.t w5 = h1_activation 
"""
partial_diff_of_o1_summation_w_r_t_w5 = h1_activation
print(
      "partial diff of o1 summation w.r.t w5 is: {}".format
       (partial_diff_of_o1_summation_w_r_t_w5)
)
print('-'*80)
partial_derivative_of_etotal_w_r_t_w5 = partial_diff_of_e_total_w_r_t_o1_predicted \
                                        * partial_diff_of_o1_predicted_w_r_t_o1_summation \
                                        * partial_diff_of_o1_summation_w_r_t_w5
print(
      "partial derivative of total error with respect to w5: {}".format
       (partial_derivative_of_etotal_w_r_t_w5)
)

updated_weight_w5 = w5-learning_rate*partial_derivative_of_etotal_w_r_t_w5
print('-'*80)
print("Updated weight for w5 is as: {}".format(updated_weight_w5))
