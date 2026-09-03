import numpy as np
import math

#-------------------------------------
#Step 1: Input Layer
#-------------------------------------

x1=2.0
x2=3.0

print("Step 1 : Input Layer")

print("Input Feature : X(This are features)")

print(f"X1={x1}")
print(f"x2={x2}")



#-------------------------------------
#Step 2: This Are Hidden Layer
#-------------------------------------
print("Step 2 : Hidden Layer (2 Neurons)")

print("Hidden Neuron 1 ")
w11=0.5
w12=-0.2
b1=0.1

print("Weights  :")
print(f"W1 :{w11}")
print(f"W1 :{w12}")

print("Bias")

print(f"b: {b1}")

print("weighted Sum :")
print("z1=(x1*w1 +x2 *w12 )+b1")

z1=(x1*w11)+(x2*w12)+b1

print("Weighted Sum z1  :",z1)

h1=max(0,z1)

print("Output of hiddent neuron  1 is",h1)

##############

print("Hidden Neuron 2 ")
w21=0.8
w22=0.4
b2=-0.1

print("Weights  :")
print(f"W21 :{w21}")
print(f"W22 :{w22}")

print("Bias")

print(f"b: {b2}")

print("weighted Sum :")
print("z2=(x1*w21 +x2 *w22 )+b2")

z2=(x1*w21)+(x2*w22)+b2

print("Weighted Sum z2  :",z2)

h2=max(0,z2)

print("Output of hiddent neuron  2 is",h2)


#-------------------------------------
#Step 3: OutPut Layer
#-------------------------------------
w_out1=1.0
w_out2=1.5
b_out=0.2

print("Step 3: OutPut Layer")

print("weights")

print(f"w_out1 :{w_out1}")
print(f"w_out2 :{w_out2}")


print("Bias")
print(f"b_out : {b_out}")

z_out=h1*w_out1+h2*w_out2+b_out


print("Weighted Sum :",z_out)
#sigmoid
z=1/(1+math.exp(-z_out))

print("----------------------------------------------------------")

print("------------Neural Network Summary  --------------")

print("---------------------------------------------------------")

print("Input Layer")

print(f"X1:{x1}")
print(f"x2:{x2}")

print("Hiddent layer")

print(f"h1:{h1}")
print(f"h2 : {h2}")

print("output Layer")
print(f"z:{z}")


print("Predication of Neural Network")


if(z>=0.5):
    print("predicated as Positive Class")
else:
    print("Predicated as Negative Class ")





