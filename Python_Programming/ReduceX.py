from functools import reduce

def CheckEven(No):
    return (No%2==0)

def Increment(No):
    return No+1

def Addition (no1,no2):
    return no1+no2

def main():
    Data=[13,12,8,10,11,20]
   
    print("Input Data is :",Data)

    FData=list(filter(CheckEven,Data))
    print("I FData is :",FData)
    
    MData=list(map(Increment,FData))
    print("Data after map :",MData)

    RData=(reduce(Addition,MData))
    print("Data after Reduce",RData)





if __name__=="__main__":
    main()