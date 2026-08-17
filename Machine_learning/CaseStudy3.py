import pandas as pd
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
# df=df["species"].value_counts()

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