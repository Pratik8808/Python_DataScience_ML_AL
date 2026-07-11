class Arithmatic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B

# Ret=Addition(aobj,Value1,Value2)
    def Addition(self):
        Ans=self.No1+self.No2
        return Ans

    def Subtraction(self):
        Ans=self.No1-self.No2
        return Ans


print("Enter First NUmber")
Value1=int(input())

print("Enter Second NUmber")
Value2=int(input())

aobj=Arithmatic(Value1,Value2)

# Ret=Addition(aobj,Value1,Value2)
Ret=aobj.Addition()
print("Addition of two Number is ",Ret)

Ret=aobj.Subtraction()
print("Subtraction of two Number is",Ret)   
