from sklearn.datasets import load_iris

def main():
    Border="-"*50
    print(Border)
    print("Iris Classification Case Study")
    print(Border)

    Dataset=load_iris()

    
    print(Dataset)
if __name__=="__main__":
    main()