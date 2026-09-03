import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error ,r2_score

#--------------------------------------------------------------#
# Step1 :Load The Data
#------------------------------------------------------------- #

df=pd.read_csv("california_housing.csv")
print("Shape is ",df.shape)


#--------------------------------------------------------------#
# Step2 :separate the data and Labels
#------------------------------------------------------------- #
X=df.drop("target",axis=1)
Y=df["target"]

print("Shape of X is :",X.shape)
print("Shape of Y is :",Y.shape)
#--------------------------------------------------------------#
# Step3 :Split DataSet for Training and Testing
#------------------------------------------------------------- #
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)


#--------------------------------------------------------------#
# Step4.1 :Create the Model
#------------------------------------------------------------- #
base_model=DecisionTreeRegressor(random_state=42)

#--------------------------------------------------------------#
# Step4.2 :Create the Model
#------------------------------------------------------------- #
model=BaggingRegressor(
    estimator=base_model,
    n_estimators=10,
    random_state=42
)
#--------------------------------------------------------------#
# Step5 :Train the Model
#------------------------------------------------------------- #
model=model.fit(X_train,Y_train)


#--------------------------------------------------------------#
# Step6 :Test the Model
#------------------------------------------------------------- #
Y_pred=model.predict(X_test)

#--------------------------------------------------------------#
# Step7 :Evalutate the Model
#------------------------------------------------------------- #

print("MSE",mean_squared_error(Y_test,Y_pred))
print("R2",r2_score(Y_test,Y_pred))





