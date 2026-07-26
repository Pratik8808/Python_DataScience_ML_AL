import sys
import os
import hashlib

# 25 july 2026

def CalculateCheckSum(FileName):
    fobj=open(FileName,"rb")
    hobj=hashlib.md5()

    Buffer=fobj.read(1024)
    while(len(Buffer)>0):
        hobj.update(Buffer)

        Buffer=fobj.read(1024)
    fobj.close()
    return  hobj.hexdigest()
   
def  FindDUplicate(DirectoryName):
    Ret=False
    Ret=os.path.exists(DirectoryName)
    if(Ret==False):
        print("Path is Invaild")
        return
    ret=os.path.isdir(DirectoryName)
    if(Ret==False):
        print("It is not Directory\n")
        return

    
    Duplicate={}

    for FolderName ,SubFolder,filename in os.walk(DirectoryName):
        for fname in filename:
            fname=os.path.join(FolderName,fname)
            CheckSUm=CalculateCheckSum(fname)
            if CheckSUm in Duplicate:
               
                Duplicate[CheckSUm].append(fname)
            else:
              
                Duplicate[CheckSUm]=[fname]
   
    return Duplicate

def DeleteDuplicate(DirectoryName):
    MyDict=FindDUplicate(DirectoryName)
    # Result=MyDict.values()
    Result=list(filter(lambda x:len(x)>1,MyDict.values()))
    return Result

def main():
   Data=DeleteDuplicate("Test")
   print(Data)

    

if __name__=="__main__":
    main()

