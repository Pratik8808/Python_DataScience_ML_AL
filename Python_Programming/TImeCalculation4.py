import time
def Factorial(No):
    Fact=1
    for i in range (1,No+1):
        Fact=Fact*i
    return Fact

def main():
    value=int(input("Enter the Number  :"))
    start_time=time.time()

    Ret=Factorial(value)

    end_time=time.time()

    print(f"Factorial of {value} is {Ret}")

    print(f"Time required  is :{end_time-start_time:.5f} Seconds")#in Sec started from 1970 1 jan 

 

if __name__=="__main__":

    main()