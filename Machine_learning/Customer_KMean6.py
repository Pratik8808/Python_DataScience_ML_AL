import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    #Step1
    df=pd.read_csv("Mall_Customers.csv")

    print(df.head())

    print("Missing Values :",df.isnull().sum())

    #Step2:Feature Selection

    X=df[["AnnualIncome","SpendingScore"]]

    print("Selected Features :")

    print(X.head())

    #Step 3 Scale the Data
    Border="-"*40
    print("Step 3  Scale the Data")
    scale=StandardScaler()
    X_Scaled=scale.fit_transform(X)
    print(X_Scaled[:5])

    #Step 4:Elbow Method 
    print(Border)

    print("Step 4 Elbow Method ")
    print(Border)
    WCSS=[]
    for k in range(1,11):
        model=KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )
        model.fit(X_Scaled)

        WCSS.append(model.inertia_)

    print("Value  of WCSS :")
    for i in range(len(WCSS)):
        print(f"{i+1}:{WCSS[i]}")


    #Step 5Visulause
    print(Border)
    print("Step 5Visulause")

    plt.plot(range(1,11),WCSS,marker="o")
    plt.xlabel("Number of Clusterss :k")
    plt.ylabel("WCSS")
    plt.title("Marvellous Elbow Method")
    plt.grid(True)
    plt.show()

    #Step 6
    model=KMeans(
            n_clusters=4,
            random_state=42,
            n_init=10
        )
    clusters=model.fit_predict(X_Scaled)

    df["Cluster"]=clusters

    print("Dataset with Cluster :")
    print(df.head(100))

    WCSS.append(model.inertia_)


if __name__=="__main__":
    main()