import schedule
import time
import datetime

def Display():
    print("Jay Ganesh....",datetime.datetime.now())

def main():
    print("Automation Script started")
    schedule.every(1).minute.do(Display)

    #ISSUE
if __name__=="__main__":
    main()