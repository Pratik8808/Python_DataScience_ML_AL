import pandas as pd



from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


#Step 1: Load the DataSet

df=pd.read_csv("breast_cancer.csv")
print(df.shape)
print("First few Records")
print(df.head())

#-----------------------
# step 2: separate Feature and labels
#-----------------

X=df.drop("target",axis=1)
Y=df["target"]

print("X Shape : ",X.shape)
print("Y Shape :",Y.shape)


#-----------------------
# step 3: Spilt Dataset for training and testing
#-----------------

X_train,X_test,Y_train,Y_Test=train_test_split(X,Y,test_size=0.5,random_state=42)



#-----------------------
# step 4: Scaled the Features
#-----------------
scalar=StandardScaler()
X_train=scalar.fit_transform(X_train)
X_test=scalar.fit_transform(X_test)


#-----------------------
# step 5: Train the Model
#-----------------

model=DecisionTreeClassifier(random_state=42)

model=model.fit(X_train,Y_train)


#-----------------------
# step 6: Test the Model
#-----------------

Y_Pred=model.predict(X_test)


#-----------------------
# step 7: Evluate the Model
#-----------------
print("Accuaracy Score")
accuarcy= accuracy_score(Y_Test,Y_Pred)

print(accuarcy)

print("Confusion Matrix :")

print(confusion_matrix(Y_Test,Y_Pred))





