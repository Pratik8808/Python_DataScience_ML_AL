def main():
    try:
        open("Demo.txt","r")
        print("File Gets Opened")
    except FileNotFoundError as fobj:
        print("File is Not Present in Current Directory")
        

if __name__=="__main__":
    main()

    #File_Create.py