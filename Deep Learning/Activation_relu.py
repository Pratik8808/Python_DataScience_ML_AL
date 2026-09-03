import numpy as np


def Relu(z):
    return max(0,z)

def Marvellous_Neuron_Forwad(input,weights,Bias):
    print("Input are (X): ",input)
    print("Weights are(W) : ",weights)
    print("Bias are (b) : ",Bias)

    # z=sum(w*x for w,x in zip(weights,input))+Bias
    z=0
    for i in range(len(input)):
        z=z+(input[i]*weights[i])
    print("Weighted Sum :",z)

    y=Relu(z)
    return y


def main():
    print("------------ Neural Network-----------------")

    input=[1.0,2.0,3.0]
    weights=[0.6,0.4,-0.2]
    Bias=0.5

    Result=Marvellous_Neuron_Forwad(input,weights,Bias)

    print("Predicted Result : ",Result)

if __name__=="__main__":
    main()