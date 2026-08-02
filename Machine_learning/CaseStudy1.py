import pandas as pd
Border="-"*30
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


