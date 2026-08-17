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
    




def main():
    marvellousRegression("Advertising.csv")

if __name__=="__main__":
    main()