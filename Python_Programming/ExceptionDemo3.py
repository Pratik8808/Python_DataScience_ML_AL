def main():
 Ans=0
 try:
    print("Enter first Number")
    No1=int(input())
    print("Enter Second Number")
    No2=int(input())

    Ans=No1/No2
    print("Division is SucessFul")
 except ZeroDivisionError as zobj:
    print("Exception occured due to Second operand :",zobj)
 except ValueError as vobj:
    print("Exception Occured Due to Innavild DataTypes :",vobj)



 print(f"Result is {Ans}")


if __name__=="__main__":
    main()