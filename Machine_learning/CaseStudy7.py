import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border="-"*30
#Outliers  Centroid
###########################################################################################
#Step1:Load the Dataset
###########################################################################################

print(Border)
print("Step 1: Load the Dataset")
print(Border)

DataPath="iris.csv"

df=pd.read_csv(DataPath)
print("DataSet Loaded Sucessfully")
print("Initial Entry from Dataset are  :")
print(df.head())

###########################################################################################
#Step2:Data Analysis (EDA)
###########################################################################################
print(Border)
print("Step 2: Data Anaysis (EDA)")
print(Border)
print("Shape of DataSet :",df.shape)

print("Column Names:",list(df.columns))

print("Missing Values Per Column :")
print(df.isnull().sum())

print("Class Distribution (species Count)")
print(df["species"].value_counts())

print("Statistical report of DataSet :")
print(df.describe())

###########################################################################################
#Step3:Decide Independent & Dependent Variables
###########################################################################################
print(Border)
print("Step 3: Decide Independent & Dependent Variables")
print(Border)

# X : Independent Variable/Features
# Y: Independent Variable/Labels

feature_Cols=[
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]
X=df[feature_Cols]
Y=df["species"]

print("X Shape is :",X.shape)
print("Y Shape is:",Y.shape)

###########################################################################################
#Step4:Visualization of DataSet
###########################################################################################

print(Border)
print("Step 4 : Visualization of DataSet")
print(Border)

# Scattered plot
plt.figure(figsize=(7,5))
for sp in df["species"].unique():
    temp=df[df["species"]==sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label=sp)

plt.title("Marvellous Iris Case Study")


plt.xlabel("petal length (cm)")
plt.ylabel("Petal width (cm)")

plt.legend()
plt.grid()
plt.show()


###########################################################################################
#Step5:Spilt the DataSet for training and Testing
###########################################################################################

print(Border)
print("Spilt the DataSet for training and Testing")
print(Border)

X_train,X_test,Y_train,Y_Test=train_test_split(X,Y,test_size=0.5,random_state=42)

print("X :",X.shape) #(150,4)
print("Y :",Y.shape) #(150,)
print("DataSet Spiliting Activity Done")
print("X_Train :",X_train.shape)#(75,4)
print("X_Test :",X_test.shape) #(75,4)
print("Y_Train :",Y_train.shape)#(75,)

print("Y_Test :",Y_Test.shape)#(75,)

###########################################################################################
#Step6:Build The Model
###########################################################################################

print(Border)
print("Step 6 :Build the Model")
print(Border)
model=DecisionTreeClassifier(max_depth=5)
print("Model is get Created Sucessfully")

###########################################################################################
#Step:7Train the Model
###########################################################################################
print(Border)
model.fit(X_train,Y_train)

print("Model Trained Sucessufllly")

print(Border)           


