#(kuthe, kuthun)
#kuthubn : 0/1/2

# 0 Starting
# 1 Current
# 2 End 

def main():
    try:
        fobj=open("Demo.txt","r")
        print("File Gets Opened")

        fobj.seek(10,0)
        Data=fobj.read()

        print(Data)
        

    except FileNotFoundError as fobj:
        print("File is Not Present in Current Directory")
        

if __name__=="__main__":
    main()

