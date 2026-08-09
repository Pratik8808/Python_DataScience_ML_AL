import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def  MarvellousClassifier(Datapath):
     border="-"*40
     print(border)

     #Step 1 : load DataSet from CSV file
     print("Step 1 : load DataSet from CSV file")
     print(border)
     df=pd.read_csv(Datapath)

     print(border)
     print("Some entry from Dataset")
     print(df.head())

     print(border)


    #Step 2:Clean the DataSet
     print(border)
     print("#Step 2:Clean the DataSet")
     print(border)

     df.dropna(inplace=True) # delete nan and null value in any col
     print("Shape of Dataset :",df.shape)
     print("Total records :",df.shape[0])
     print("Total Columns :",df.shape[1])

     #Step 3 : Separate Independent and Dependent Variable
     print(border)
     print("Step 3 : Separate independent")
     print(border)
     X=df.drop(columns=['Class'])
     Y=df['Class']

     print("Shape of X :",X.shape)
     print("Shape of Y:",Y.shape)

     print(border)
     print("Input columns :",X.columns.tolist())
     print("Output columns : Class")
     print(border)
         


def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__=="__main__":
    main()