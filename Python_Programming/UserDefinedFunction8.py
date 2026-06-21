def BigBazaar():
    print("Inside BigBazaar")
    
    def Amul():
        print("Inside Amul Ice Cream Parlor")

def main():
    BigBazaar()
    Amul() #Error
    BigBazaar.Amul() #Error
 

    
if __name__=="__main__":
    main()
   