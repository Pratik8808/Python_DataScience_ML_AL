import tensorflow as tf

input=tf.constant([1.0,2.0,3.0])

weights=tf.constant([0.5,-0,2,0.8])

bias=tf.constant(0.1)

weighted_sum=tf.reduce_sum(input*weights)+bias

print("Inputs : ",input.numpy)#1.0,2.0,3.0
print("Weights :",weights)#0.5,-0,2,0.8
print("Bias",bias)#0.1

print("Weighted Sum :",weighted_sum.numpy())#2.6

output=tf.sigmoid(weighted_sum)#0.93

print("Ouput :",output.numpy())
