
#Python Automation args --h and --u started

  #Valid
#python Automation.py --h
#python  Automation.py --u
#python  Automation.py Marvellous

import sys
def main():
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("Help")
        elif(sys.argv[1]=="--u" or  sys.argv[1]=="--U"):
            print("Usage")
        else:
            DirectoryName=sys.argv[1]
            print("Directory name is",DirectoryName)
    else:   
        print("Invaild Arugment")
        print("Please Use --h or --u for More Information")
    


if __name__=="__main__":
    main()