import sys
import os
import hashlib



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

    for FolderName ,SubFolder,filename in os.walk(DirectoryName):
        for fname in filename:
            fname=os.path.join(FolderName,fname)
            CheckSUm=CalculateCheckSum(fname)
            print(f"{fname}: {CheckSUm}")

def main():
   FindDUplicate("Test")

    

if __name__=="__main__":
    main()