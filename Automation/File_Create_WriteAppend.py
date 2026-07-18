def main():
    try:
        fobj=open("Demo.txt","a")
        print("File Gets Opened")
        
        fobj.write(" Pune Maharashtra")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is Not Present in Current Directory")
        

if __name__=="__main__":
    main()