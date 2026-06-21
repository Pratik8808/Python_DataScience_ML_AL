def Calculation(No1,No2):
    mult=No1*No2
    Div=No1/No2
    return mult,Div

def main():
  Value1=int(input("Enter First Number :"))
  Value2=int(input("Enter Second  Number :"))

  Ret1,Ret2=Calculation(Value1,Value2)

  print("Multpllication of number is :",Ret1)
  print("Divsion of the  Number is :",Ret2)

  
   

if __name__=="__main__":
    main()
   