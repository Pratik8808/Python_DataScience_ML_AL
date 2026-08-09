import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():
    #Indepedent
    X=np.array([
        [1,2],
        [2,3],
        [3,1],
        [5,6]
    ])
    Y=np.array(["Red","Red","Blue"])
    new_point=np.array([[3,3]])

    print("InDepedent  Variables are :")
    print(X)

    print("Dependent Variables are :")
    print(Y)

if __name__=="__main__":
    main()