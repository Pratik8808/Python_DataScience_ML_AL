import time
import multiprocessing
import os

def SumCube(No):
     print("Process is running with PID ",os.getpid())
     sum=0
     for i in range(1,No+1):
          
          sum=sum + (i**3)
    
     return sum



def main():
     Data=[1000000,20000000,30000000,40000000,5000000]
     Result=[]

     start_time=time.perf_counter()
     
     pobj=multiprocessing.Pool()

     Result = pobj.map(SumCube,Data)

     pobj.close()

     pobj.join()

     end_time=time.perf_counter()


     print("Result is ")
     print(Result)
     print(f"Time required is {end_time-start_time:4f} Seconds")
   
    
  


if __name__=="__main__":
    main()