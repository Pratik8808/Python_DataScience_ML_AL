import pandas as pd



from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


from sklearn.ensemble import VotingClassifier

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

X_train,X_test,Y_train,Y_Test=train_test_split(X,Y,test_size=0.2,random_state=42)



#-----------------------
# step 4: Scaled the Features
#-----------------
scalar=StandardScaler()
X_train=scalar.fit_transform(X_train)
X_test=scalar.fit_transform(X_test)


#-----------------------
# step 5.1: Create the Individual Models
#-----------------
model_log =LogisticRegression(max_iter=1000)
model_det = DecisionTreeClassifier(random_state=42)
model_knn = KNeighborsClassifier(n_neighbors=5)




#-----------------------
# step 5.2: Create the Voting Model
#-----------------
model=VotingClassifier(
    estimators=[('logistic',model_log),('decision_tree',model_det),('knn',model_knn)],
    voting="hard"
)

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





