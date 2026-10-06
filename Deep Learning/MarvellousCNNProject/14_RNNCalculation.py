#ht=tanH(Wx*Xt+Wh *ht-1 +b)

#Xt      Current input
#Wx       weight of input
#Wh      weight of previous hiddent state
#b        bias
#ht-1   Previous hidden state
#tanh    Activation function (-1 to 1)
#ht     New Hidden state
import numpy as np 


def sigmoid(x):
    return 1/(1+np.exp(-x))

def MarvellousRNNPrediction():
    print("Calculation of RNN")

    #Food was not good
    inputs=[1,2,5,3]

    #RNN paramenters
    Wx=0.5
    wh=0.8
    bias =0.1
    hidden_state=0
    for time_step,x in enumerate(inputs):
        previous_hidden_state=hidden_state

        weighted_memory=Wx*x

        weighted_memory=wh*previous_hidden_state

        total=weighted_memory +weighted_memory+bias

        hidden_state=np.tanh(total)

        print("Time Step :",time_step+1)

        print("Input :",x)

        print("Hidden state :",hidden_state)

        print("-"*30)

        print("Final Hidddn State :",hidden_state)

def main():
    MarvellousRNNPrediction()

if __name__=="__main__":
    main()