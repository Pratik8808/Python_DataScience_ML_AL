import psutil
import sys
import os

#python Process Survillence.py MarvellousLog
#pythonProcess Survellence.py    time_interval   Folder_name
#                    0               1               2

#len(sys.argv)-3

#python Process Survillence.py  --h
#                  0              1
                
def main():
    Border="-"*60
    print(Border)
    print("------------------Marvellous Platform Survillence System ---------------")
    print(Border)

    # 0 --h and  --u Handling
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h"or sys.argv[1]=="--H"):
            print("This Automation Script is used to perform")
            print("1:it Fetch the Information of running Process")
            print("2:It Fetch information about the Primary Storage as Ram")
            print("3:It Fetch information about the Secondary storage as HDD")
            print("4:It Fetch the Information about  the Microprocessor")
            print("5:Its get auto Scheduled periodically")
            print("6 :It maintainall record  into log file")
            print("7:Its sends the log files through mail periodically")

        elif(sys.argv[1]=='--u'or sys.argv[1]=="--U"):
            print("Use the Automation Script as:")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval :Time in minutes for periodic Exceution")
            print("Folder_Name: Name of the Folder for the log file Creation")
        else:
            print("Unable to proceed as there is not matching Arugment")
            print("Please Use --h or --u  flag or getting more details")
    #Acutal Project Code
    elif(len(sys.argv)==3):
        pass
    else:
        print("Invaild Number of Arugement !!")
        print("Unable to proceed  as Arugement is not matching")
        print("Please Use --h or --u  flag or getting more details")
    print(Border)

    print("----Thank you for using Our Platform Survillence System---------")

    print(Border)
if __name__=="__main__":
    main()


# for(Map.Entry<Integer,Integer)s1:s3.mapEntry(){
#
#}
##
