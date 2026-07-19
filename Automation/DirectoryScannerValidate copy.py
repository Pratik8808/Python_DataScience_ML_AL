#template 
import sys
import os
import time
import schedule

#Make Separate Folder for Log 



def DirectoryScanner(DirectoryPath):

    Border="-"*40
    timestamp=time.ctime()
    LogFileName="Marvellous%s.log"%(timestamp)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")

    Ret=False

    Ret=os.path.exists(DirectoryPath)
    if(Ret==False):
        print("Marvellous Automation  Error : There is no Such Directory with Name",DirectoryPath)
        return
    
    Ret=os.path.isdir(DirectoryPath) # Folder madhe Folder Ahat ka 
    if(Ret==False):
        print("Marvellous Automation  Error: It is not a Driectory with name",DirectoryPath)
        return
    

    print("Log File Get created with  :",LogFileName)

    fobj=open(LogFileName,"w")
    fobj.write(Border+"\n")
    fobj.write("Marvellous  Automation Script \n")
    fobj.write(Border+"\n\n")


    fobj.write("Files from the Directory are :\n\n")
    fobj.write(Border+"\n")

    for foldername,SubFolderName,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")

            print()
    fobj.write(Border+"\n")
    fobj.write("Log file is Created at :"+timestamp)
    fobj.write("\n"+Border+"\n")
    fobj.close()

    

def main():

    Border="-"*40
    print(Border)
    print("     Automation Script             ")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script is Used  to Travel Directory")
            print("For Better Usage Please  Check --u flag")
            
        elif(sys.argv[1]=="--u" or  sys.argv[1]=="--U"):
            print("Please Except The Script as ")
            print("Python fileName.py DirectoryName")
            print("Directory Name Shoud Absoulte Path")
        else:
            
            DirectoryScanner(sys.argv[1])

  

    
    else:

        print("Invaild Arugment")
        print("Please Use --h or --u for More Information")
    print(Border)
    print("    Thank you for Using Script             ")
    print(Border)



if __name__=="__main__":
    main()