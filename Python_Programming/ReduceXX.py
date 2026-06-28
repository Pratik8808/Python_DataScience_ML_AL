from functools import reduce

CheckEven=lambda No:(No%2==0)
Increment=lambda No:No+1
Addition=lambda no1,no2:(no1+no2)


def main():
    Data=[13,12,8,10,11,20]
   
    print("Input Data is :",Data)

    FData=list(filter(CheckEven,Data))
    print("AFTER FData is :",FData)
    
    MData=list(map(Increment,FData))
    print("Data after map :",MData)

    RData=(reduce(Addition,MData))
    print("Data after Reduce",RData)





if __name__=="__main__":
    main()