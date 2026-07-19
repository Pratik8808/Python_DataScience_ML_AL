def main():
    try:
        fobj=open("Demo.txt","r")
        print("File Gets Opened")
        print("File Offset is :",fobj.tell())

        Data=fobj.read(10)
        
        print(Data)
        print("File Offset is :",fobj.tell())


        fobj.close()

    except FileNotFoundError as fobj:
        print("File is Not Present in Current Directory")
        

if __name__=="__main__":
    main()

    #File_Tell.py