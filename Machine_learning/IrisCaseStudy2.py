from sklearn.datasets import load_iris

def main():
    Border="-"*50
    print(Border)
    print("Iris Classification Case Study")
    print(Border)

    Dataset=load_iris()
    #MetaData of the DataSet()
    print("Independent Variable are :")
    print(Dataset.feature_names)

    print("Dependent variable are : ")
    print(Dataset.target_names)

if __name__=="__main__":
    main()