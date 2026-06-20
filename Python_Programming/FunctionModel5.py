from Marvellous import *

def main():
   print("enter first Number ")
   value1=int(input())
   print("enter Second Number ")
   value2=int(input())
   Ret=Addition(value1,value2)
   print("Addition is :",Ret)
   Ret=Subtraction(value1,value2)#Error NameError: name 'Subtraction' is not defined


   print("Subtraction  is :",Ret)
   

if __name__=="__main__":
    main()
   