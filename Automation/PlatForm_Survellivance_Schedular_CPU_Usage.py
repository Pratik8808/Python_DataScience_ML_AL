import psutil
import sys
import os
import time
import schedule


def PlatformSurvillance(FolderName):
    Border="-"*60
    Ret=False
    Ret=os.path.exists(FolderName)
    if(Ret):
        Ret=os.path.isdir(FolderName)
        if(Ret==False):
            print("Unable to as Directory name is existing but its not a Directory")
            return
    else:
        os.mkdir(FolderName)
        print("Driectory for log File is Created Sucessfully with Name")
    
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    filename=os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj=open(filename,"w")
    print(f"Log File Sucessfully Created With Name {filename}")
    fobj.write(Border+"\n")
    fobj.write("------------------Marvellous Platform Survillence System --------------\n")
    fobj.write(f"Log file is Created at {timestamp}\n")
    print(Border,"\n\n")

    fobj.write("-----------System Report --------------------------\n")
    fobj.write("Number of active Cpu cores : %s \n" %psutil.cpu_count() )

    fobj.write("CPU usaage : %s %%\n "%psutil.cpu_percent())
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")

    fobj.write("-------------------------------End of the Logic -------------------------\n")
    fobj.write(Border+"\n")

    fobj.close()



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

        print("CPU Usage :",psutil.cpu_percent())
        print("Schedular Started Sucessfully")
        print("Press Ctrl +C to abort the Automation Script ")
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance,sys.argv[2])
        while True:
            schedule.run_pending()
            time.sleep(1)

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
