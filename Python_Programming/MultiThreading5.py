#2+4+5+6+8=20
#1+3+5+7+9=25

def SumEven(No):
    sum=0
    for i in range(2,No,2):
        sum=sum+i
    print("Summation of EVen is ",sum)


def SumOdd(No):
    sum=0
    for i in range(1,No,2):
        sum=sum+i
    print("Summation of odd  is ",sum)


  


def main():
    SumEven(1000000)
    SumOdd(1000000)
if __name__=="__main__":
    main()