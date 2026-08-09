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

     #Step 4 :Split the DataSet for Training and testing
     print(border)
     print("Step 4:Split the DataSet for Training and testing")
     print(border)

     X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

     print(border)
     print("Details of training and testing data")
     print("Shape of X_train :",X_train.shape)
     print("Shape of X_Test :",X_test.shape)
     print("Shape of Y_train :",Y_train.shape)
     print("Shape of Y_Test :",Y_test.shape)
     print(border)

     #Step 5 :Feature Scaling 
     print(border)
     print("Step 5 :Feature Scaling ")
     print(border)

     scaler=StandardScaler()
     X_train_scaled=scaler.fit_transform(X_train)
     X_test_scaled=scaler.fit_transform(X_test)

     print("Features Scaling Done")
     print(border)

     #Step 6 :Build the Model

    #  print(border)
    #  print(" Step 6:Bulild the Model")
    #  print(border)
    #  model=KNeighborsClassifier(n_neighbors=5)
    #  print("Classfication model is Created")

    #  #Step 7: Train the model
    #  model=model.fit(X_train_scaled,Y_train)
    #  print(border)
    #  print("Step 7: Train the model")
    #  print(border)
    #  print("Model Training Completed")

    #  #Step 8: Test the model
    
    #  print(border)
    #  print("Step 8: Test the model")
    #  print(border)
    #  Y_Pred=model.predict(X_train_scaled)

    #  accuracy=accuracy_score(X_test_scaled,Y_Pred)

    #  print("Model Accuacy is :",accuracy)

    

    # step 6:HyperParameter tuning
     accuracy_scores=[]
     K_values=range(1,21)


     for k in K_values:
         model =KNeighborsClassifier(n_neighbors=k)
         model=model.fit(X_train_scaled,Y_train)
         Y_Pred=model.predict(X_test_scaled)
         accuracy=accuracy_score(Y_test,Y_Pred)
         accuracy_scores.append(accuracy)


     print("Accuraacy report :")
     for no in accuracy_scores:
         print(no*100)

     print(border)





  


     
         


def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__=="__main__":
    main()