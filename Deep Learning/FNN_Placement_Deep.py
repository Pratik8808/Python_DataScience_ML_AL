# ---------------------------------------------#
#Deep Learning PipLine
#----------------------------------------------#
# 1.Read the Data from  CSV
# 2. Data Analaysis(EDA)
# 3.Preprocessing
# 4.Train Test Spilt
# 5.Feature Scaling
# 6.FNN model Training
# 7.Model Evaluation
# 8.Graphical Respresention
# 9.Model Preserve
# 10. Model Loading and preserve
# 11.Test Unseen Data
# 
# ---------------------------------------------#


import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix


#Step 1:Read the Data from  CSV

print("Step 1 : Read the Data from  CSV")

Data=pd.read_csv("placement_data.csv")
print("Complete Dataset :")
print(Data)

#step 2: Data Anaylsis
print("step 2: Data Anaylsis")

print("First 5 Rows")
print(Data.head())

print("Columns names:")
print(Data.columns)

print("Shape of Dataset :")
print(Data.shape    )

print("Statistical Summary :")
print(Data.describe())


#Step3:Preprocesssing

print("3:Preprocesssing")

X=Data[['Aptitude','Coding','Communication','Academics','Internship']]
Y=Data['Placed']

print("Input features : ")
print(X.head())

print("Target :")
print(Y.head())


#Step 4:Train and Spilt

print("4. Train test spilit")

X_train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.30,random_state=42)

print("Training Input Shape  :" ,X_train.shape)
print("Testing Input Shape  :" ,X_Test.shape)
print("Training Output Shape  :" ,Y_Train.shape)
print("Testing  Output Shape  :" ,Y_Test.shape)


#
# 5 Features Scaling
#

print("5 Feeature Scaling")
scalar=StandardScaler()

X_trained_Scaled=scalar.fit_transform(X_train)
X_Test_Scaled=scalar.fit_transform(X_Test)


print("Scaled Training Data :")
print(X_Test_Scaled[:5])


#-----------------------
# 6.FNN model Training
#----------------------

print("FNN Model Training")
model=MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print(model)
#------------------------
# Train train the Model
#-----------------------

model.fit(X_trained_Scaled,Y_Train)
print("Model training Completed ")



#------------------
# 7.Model Evaluation
#------------------

print("7.Model Evaluation")
Y_Pred=model.predict(X_Test_Scaled)


accuary=accuracy_score(Y_Test,Y_Pred)

print("Accuarcy is :",accuary)

cm=confusion_matrix(Y_Test,Y_Pred)

print("Confusion matrix",cm)
print("Predict the Probility")
Y_Prob=model.predict_proba(X_Test_Scaled)

print(Y_Prob[:5])


# #------------------
# # 9.Model Preserve
# #------------------
# print("Model Preserve")

# joblib.dump(model,"placement_FNN_model.pkl")
# joblib.dump(scalar,"placement_Scalar.pkl")

# print("Model and Scalar gets Dumped  Sucessfully ")

#--------------------------------
#10: Load the Model
#--------------------------------

print("10: Load the Model")
loaded_model=joblib.load("placement_FNN_model.pkl")
loaded_scalar=joblib.load("placement_Scalar.pkl")

print("Models Gets loaded Sucessfully")


#------------------------
# 11.Test Unseen Data
# Aptitude:         70
# coding:           75
# communication:    80
# academics:        85
# internship:       1
#------------------------


new_student=pd.DataFrame([[70,75,80,85,1]],columns=['Aptitude','Coding','Communication','Academics','Internship'])

new_student_scaled=loaded_scalar.transform(new_student)

new_preddiction=loaded_model.predict(new_student_scaled)


new_proabiltiy=loaded_model.predict_proba(new_student_scaled)


print("New Student Data :")
print(new_student)
print("Predication Proability : ",new_proabiltiy)


if new_preddiction[0]==1:
    print("Predication :Placed ")

else:
    print("Prediction:Not placed ")
