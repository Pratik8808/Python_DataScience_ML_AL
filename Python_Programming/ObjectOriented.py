class Arithmatic:
# Ret=Addition(aobj,Value1,Value2)
    def Addition(No1,No2): # ISSUE ERROR
        Ans=No1+No2
        return Ans

    def Subtraction(No1,No2):# ISSUE ERROR
        Ans=No1-No2
        return Ans
    
aobj=Arithmatic()

print("Enter First NUmber")
Value1=int(input())

print("Enter Second NUmber")
Value2=int(input())
# Ret=Addition(aobj,Value1,Value2)
Ret=aobj.Addition(Value1,Value2)
print("Addition of two Number is ",Ret)

Ret=aobj.Subtraction(Value1,Value2)
print("Subtraction of two Number is",Ret)   
