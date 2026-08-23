import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    #Step1
    df=pd.read_csv("Mall_Customers.csv")

    print(df.head())

    print("Missing Values :",df.isnull().sum())

    #Step2:Feature Selection

    X=df[["AnnualIncome","SpendingScore"]]

    print("Selected Features :")

    print(X.head())
    
    

if __name__=="__main__":
    main()