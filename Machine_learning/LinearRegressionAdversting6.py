from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def marvellousRegression(DataPath):
    Border="-"*40
    #step 1 load the Data
    print(Border)
    print("Load the Data")
    print(Border)

    df=pd.read_csv(DataPath)
    print(df.head())

    #Step 2 Remove Unwanted Columns (EDA)
    print(Border)
    print("#Step 2 Remove Unwanted Columns (EDA)")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df=df.drop(columns=["Unnamed: 0"])
    print(df.head())

    #Step 3 :Check Missing Value
    print(Border)

    print("Total Missing Value are  :")
    print(Border)
    print(df.isnull().sum())
    print(Border)

    #Step 4: Statistical Summary

    print(Border)
    print("Step 4 : Statistical Summary")
    print(Border)
    print(df.describe())

    #Step 5 :Correlation
    print(Border)
    print("Step 5 :Correlation")
    print(Border)
    print(df.corr())

    #Step 6:Separate Independent and Dependent Variables

    print(Border)
    print("Step 6:Spilt Independent and Dependent Variables")
    print(Border)
    X=df[["TV","radio","newspaper"]]
    Y=df["sales"]

    print("Independet Variables :")
    print(X.head())

    print("Dependent Variables :")
    print(Y.head())

    #Step 7:Split the DataSet 
    print(Border)
    print("Step 7:Split the DataSet ")
    print(Border)

    X_Train , X_Test,_Y_test,Y_Train=train_test_split(
        X,Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Data ::",X_Train.shape)
    print("testing Data ::",X_Test.shape)


    
    




def main():
    marvellousRegression("Advertising.csv")

if __name__=="__main__":
    main()