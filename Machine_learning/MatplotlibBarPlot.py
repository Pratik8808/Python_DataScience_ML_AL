import matplotlib.pyplot as plt


def main():
    language=["C","C++","Java","Python"]
    student=[30,40,35,55]
    plt.bar(
        language,  # Values  of x
        student, #values of Y
        width=0.6 ,      #width of bars
        edgecolor="black", #Border color of Bars
        linewidth=1,        #width of bar border
        alpha=0.8 ,         #transperance 0.0 to 1.0
        label="Students"  #legend  text
    )
    plt.title("Marvellous  Bar")
    plt.xlabel("Languages ")
    plt.ylabel("Number of students")
    plt.legend()
    plt.grid(True)
    plt.show()    
if __name__=="__main__":
    main()