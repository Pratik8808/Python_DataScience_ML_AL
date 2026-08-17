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

    X_Train ,X_Test,Y_Train,Y_Test=train_test_split(
        X,Y,
        test_size=0.2,
        random_state=42
    )



    print("Training Data ::",X_Train.shape)
    print("testing Data ::",X_Test.shape)


    #step 8: Create and & Train Model
    print(Border)
    print("Step 8 Create and & Train Model")
    print(Border)

    model=LinearRegression()
    model=model.fit(X_Train,Y_Train)

    print("Model Trained Sucessfully")

    #Step 9:Test The Model

    print(Border)
    print( "Step 9:Test The Model")
    print(Border)

    Y_Pred=model.predict(X_Test)
    print("Expected Answer :")
    print(Y_Test[:3])

    print("Predicted Answer :")
    print(Y_Pred[:3])



    #Step 10 :Evaluate the Model

    print(Border)
    print( "Step 10:Evaulate the model")
    print(Border)

    MSE=mean_squared_error(Y_Test,Y_Pred)

    RMSE=np.sqrt(MSE)

    R2= r2_score(Y_Test,Y_Pred)

    print("MSE:",MSE)
    print("RMSE :",RMSE)#Root Means Square
    print("R2 :",R2)

    #Step 11:Display Co-efficient

    print(Border)
    print("Step 11 Display Co-efficicent")
    print(Border)
    

    print("Tv Coeffecicent :",model.coef_[0])
    print("Radio Coeffecicent :",model.coef_[1])
    print("Newspaper Coeffecicent :",model.coef_[2])


    print("Intercept :",model.intercept_)




    
    




def main():
    marvellousRegression("Advertising.csv")

if __name__=="__main__":
    main()