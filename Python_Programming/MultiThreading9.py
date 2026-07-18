
import time
import  threading


def SumEven(No):
   print("TID of SumEven is :",threading.get_ident())
   print("TID of SumEven is :",threading.get_ident())


def SumOdd(No):
    print("TID of SumOdd is :",threading.get_ident())
    


  


def main():
    print("TID of MAIN thread is :",threading.get_ident())
    start_time=time.perf_counter()
    tobj1=threading.Thread(target=SumEven,args=(10000000,))
    tobj2=threading.Thread(target=SumOdd, args=(10000000,))
    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()
   
    end_time=time.perf_counter() # Problem main start and end time run before thread execution

    print(f"Time taken to Excute is,{end_time-start_time:.4f} seconds")
if __name__=="__main__":
    main()