import numpy as np

#Step 1 define input Function  ie X
#               ( x1,x2, x3)
input=np.array([2.0,3.0,4.0])

#Step 2 :Define Weights ie W
#                 [w1, w2   ,w3]
weights=np.array([0.5,0.3,0.2])

#Step 3: Define Bias
bia= 1.0


#Step 4 :Calculate weighted sum ie Z
#z=x1w1+x2w2+x3w3
#z=(2.0*0.5)+(3.0*0.3)+(4.0*0.2)+1

z=np.dot(input*weights)

print("Z",z)

def relu(z):
    return max(0,z)


