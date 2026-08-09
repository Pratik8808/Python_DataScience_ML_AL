import math as m

def MarvellousEucDistance(P1,P2):
    Ans = m.sqrt((P1['X']-P2['Y'])**2+(P1['Y']-P2['Y'])**2)
    return Ans
    


def MarvellousKNNClassifier(k=3):
    border="-"*30
    Data=[
        {'point':'A','X':1,'Y':2,'label':'Red'},
        {'point':'B','X':2,'Y':3,'label':'Red'},
        {'point':'C','X':3,'Y':1,'label':'Blue'},
        {'point':'D','X':5,'Y':6,'label':'Blue'},
        {'point':'E','X':6,'Y':6,'label':'Blue'},
        {'point':'F','X':3  ,'Y':4,'label':'Red'},
        {'point':'G','X':3,'Y':2,'label':'Red'},



    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)


    for i in Data:
        print(i)
    print(border)

    new_point={'X':3,'Y':3}
    # Result=MarvellousEucDistance(Data[0],new_point)
    # print(Result)
    print("Distance of all Point : ")
    print(border)
    for d in Data:
        d['distance']=(MarvellousEucDistance(d,new_point))

    for d in Data:
        print(d)
       
    print(border)

    sorted_Data=sorted(Data,key=lambda item:item['distance'])

    print("Sorted Data is :")
    print(border)
    for d in sorted_Data:
        print(d)
    print(border)

  
    #Sorted keleli yeti  top 3  nearrest getle
    nearest=sorted_Data[:k]
    print(border)
    print("Nearest 3 member  are :")
   
    print(border)

    for i in nearest:
        print(i)

    print(border)

    votes={}
    for neigbhours in nearest:
        label=neigbhours['label']
        votes[label]=votes.get(label,0)+1
    print(border)
    print("Voting result is :")

    for d in votes:
        print("Name:",d,"numbers of votes ",votes[d]) 
    print(border)

    iMax=0
    Name=""
    for d in votes:
        if(votes[d]>iMax):
           iMax=votes[d]
           Name=d
    print("Final predicition is :",Name)
    print(border)




def main():
    MarvellousKNNClassifier(5)


if __name__=="__main__":
    main()