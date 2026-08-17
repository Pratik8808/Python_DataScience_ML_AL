import pandas as pd
import joblib

def loadModel(filename):
    model=joblib.load(filename)
    print("Model Loaded SucessFully")

    print(model.feature_names_in_)

def PredictPassenger(model):
    print("Enter the information")

    Pclass=int(input("Enter Pclas (1/2/3) :"))
    Sex=int(input("Enter the Sex(0/1) (0->Female) 1:Female :"))
    Age=int(input("Enter Age :"))
    sibsp=int(input("Enter sibsp :"))
    Parch=int(input("Enter Prach :"))
    Fare=int(input("Enter Fare :"))
    Embarked=int(input("Enter  embarked :(0/1/2) :"))

    Passengar=pd.DataFrame([{
        "Pclass":Pclass,
        "Sex":Sex,
        "Age":Age,
        "sibsp":sibsp,
        "parch":Parch,
        "Fare":Fare,
        "Embarked_1.0":1 if Embarked==1 else 0,
        "Embarked_2.0":1 if Embarked==2 else 0
    }])

    Passengar=Passengar[model.feature_names_in_]
    result=model.predict(Passengar)

    print(result)

def main():
    model=loadModel("MarvellousTitanic.pkl")
    PredictPassenger(model)

if __name__=="__main__":
    main()