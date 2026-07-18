import os
import time
import  multiprocessing


def SumEven(No):
    print(f"PID of SumEven :{os.getpid()}  PPID of SumEven :{os.getppid()}")

    sum=0
    for i in range(2,No,2):
        sum=sum+i
    print("Summation of EVen is ",sum)


def SumOdd(No):
    print(f"PID of SumOdd :{os.getpid()}  PPID of Sumodd :{os.getppid()}")


    sum=0
    for i in range(1,No,2):
        sum=sum+i
    print("Summation of odd  is ",sum)


  


def main():
    print(f"PID of MAIN :{os.getpid()}  PPID of MAIN :{os.getppid()}")

    start_time=time.perf_counter()
    
    tobj1=multiprocessing.Process(target=SumEven,args=(100,))
    tobj2=multiprocessing.Process(target=SumO   dd, args=(100,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()
   
    end_time=time.perf_counter() # Problem main start and end time run before thread execution

    print(f"Time taken to Excute is,{end_time-start_time:.4f} seconds")
if __name__=="__main__":
    main()