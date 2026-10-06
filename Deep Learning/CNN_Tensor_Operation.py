import tensorflow as tf


#1d tensor
tensor1= tf.constant([10,20,30])#11,22,33
tensor2=tf.constant([1,2,3])

addition=tf.add(tensor1,tensor2)

print("Addition is :",addition)


Subtraction=tf.subtract(tensor1,tensor2)#9,18,27

print("Subtraction  is :",addition)


Multipication=tf.multiply(tensor1,tensor2)

print("Multplication  is :",Multipication)#10,40,90



division=tf.divide(tensor1,tensor2)#10 10 10

print("divisionn  is :",addition)

square=tf.square(tensor1)#400,300,500

print("Square :",square)

sum=tf.reduce_sum(tensor1)

print("Reduced sum :",sum)

mean=tf.reduce_sum(tensor1)
print("Mean is :",mean)

