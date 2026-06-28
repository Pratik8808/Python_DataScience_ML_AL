def filterX(Task,Elements):
    Result=list()
    for no in Elements:
        Ret=Task(no) #checkEven(no)
        if(Ret == True):
            Result.append(no)
    return Result

def mapX(Task,Elemets):
    Result=list()

    for no in Elemets:
        Ret=Task(no) #Increment(no)
        Result.append(Ret)

    return Result

def reduceX(Task,Elements):
    Sum=0
    for no in Elements:
        Ret=Task(Sum,no) #Addition(no1,no2)
        Sum=Ret
    return Sum
        
     