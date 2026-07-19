#template 
import sys
import os

def DirectoryScanner(DirectoryPath):
    print("Files form  Directory are :")
    fobj=open("Marvellous.txt","w")
    fobj.write("Marvellous  Automation Script \n")
    fobj.write("Files from the Directory are :\n")
    for foldername,SubFolderName,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")
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