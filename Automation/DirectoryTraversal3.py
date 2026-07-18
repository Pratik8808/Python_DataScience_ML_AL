import os
def main():
    for FolderName,SubFolder,FileName in os.walk("Marevllous"):
        print("Folder Name",FolderName)

        for subf in SubFolder:
            print("SubFolder Name :",subf)
        for Fname in FileName:
             print("File Name :",Fname)
        
if __name__=="__main__":
      main()