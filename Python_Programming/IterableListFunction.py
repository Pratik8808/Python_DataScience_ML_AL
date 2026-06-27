def Summation(Data):
     Sum=0
     for i in Data:
       Sum=Sum+i

     return sum
    

def main():
   
   Marks=[78,90,56,98,77]
   Ret=Summation(Marks)
   print("Addition is :",Ret)

if __name__=="__main__":
    main()