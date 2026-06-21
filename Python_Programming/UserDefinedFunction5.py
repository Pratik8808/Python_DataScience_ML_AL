#Accept:Accept Multiple Parameter
#Return:Return Mulitple Parameter

def Marvellous(value1,value2):
    print("Inside Marvellous :",value1,value2)
    return 21,51


def main():
    
    Ret1,Ret2=Marvellous(10,20)
    print("The values of Ret1,Ret2 is :",Ret1,Ret2)
   

if __name__=="__main__":
    main()
   