import os
def main():
    try:
        #fobj.remove() -> Not Applicable
        os.remove("Demo.txt")
        

    except FileNotFoundError as fobj:
        print("File is Not Present in Current Directory")
        

if __name__=="__main__":
    main()

   