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

    #Step 3 Scale the Data
    Border="-"*40
    print("Step 3  Scale the Data")
    scale=StandardScaler()
    X_Scaled=scale.fit_transform(X)
    print(X_Scaled[:5])    

if __name__=="__main__":
    main()