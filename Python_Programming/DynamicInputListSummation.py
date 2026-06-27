def Summation(Data):
    sum=0
    for no in Data:
        sum=sum+no

    return sum




def main():
    Size=0
    Arr=list()
    print("Enter the Number of Elements")
    Size=int(input())

    print("Enter the Elments ")
    for i in range(Size):
        no=int(input())
        Arr.append(no)
    Ret=Summation(Arr)

    print("summation is :",Ret)


   
   

if __name__=="__main__":
    main()