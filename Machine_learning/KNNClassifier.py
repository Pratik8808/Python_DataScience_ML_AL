import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():
    #Indepedent
    X=np.array(
        [1,2],
        [2,3],
        [3,1],
        [5,6]
    )
    new_point=np.array([3,3])

    #Dependent
    Y=np.array(["Red","Red","Blue"])

    #Model Creation

    model=KNeighborsClassifier(n_neighbors=3)
    model.fit(X,Y)
    Y_Pred=model.predict(new_point)
    print("Printed Label :",Y_Pred)


if __name__=="__main__":
    main()