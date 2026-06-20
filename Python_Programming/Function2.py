def Addition(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans


def main():
   print("enter first Number ")
   value1=int(input())
   print("enter Second Number ")
   value2=int(input())
   Ret=Addition(value1,value2)
   print("Addition is :",Ret)
   

if __name__=="__main__":
    main()
   