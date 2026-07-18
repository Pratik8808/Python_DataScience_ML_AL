def main():
    try:
        fobj=open("Demo.txt","r")
        print("File Gets Opened")
        
        Data=fobj.read()
        
        print(Data)


        fobj.close()

    except FileNotFoundError as fobj:
        print("File is Not Present in Current Directory")
        

if __name__=="__main__":
    main()

    #File_Tell.py