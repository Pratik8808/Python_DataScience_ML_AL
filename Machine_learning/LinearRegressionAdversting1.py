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

    #Step 2 EDA
    print()





def main():
    marvellousRegression("Advertising.csv")

if __name__=="__main__":
    main()