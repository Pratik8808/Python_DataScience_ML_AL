
def checkEven(No):
   return(No%2==0)

def main():
    Value=int(input("Enter the Number :"))
    Ret=checkEven(Value)

    if(Ret==True):
        print("It is Even Number ")
    else:
         print("It is Odd Number ")




if __name__=="__main__":
    main()