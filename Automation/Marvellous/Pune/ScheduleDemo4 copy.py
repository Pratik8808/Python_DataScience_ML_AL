import schedule
import time
import datetime

def Display(Message):
    print("Jay Ganesh....",datetime.datetime.now())

def main():
    print("Automation Script started")
    schedule.every(10).seconds.do(Display,)
    while True:
         schedule.run_pending()
         time.sleep(1)
    print("End of Automation Script")
if __name__=="__main__":
    main()