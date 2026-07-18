def main():
    try:
        fobj=open("Demo.txt","w")
        print("File Gets Opened")
        
        fobj.write("Marvellous Infosystem")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is Not Present in Current Directory")
        

if __name__=="__main__":
    main()