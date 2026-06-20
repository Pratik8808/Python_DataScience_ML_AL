

def main():
   print("enter first Number ")
   value1=int(input())
   print("enter Second Number ")
   value2=int(input())
   Ret=Addition(value1,value2) #NameError: name 'Addition' is not defined
   print("Addition is :",Ret)
   

if __name__=="__main__":
    main()
   