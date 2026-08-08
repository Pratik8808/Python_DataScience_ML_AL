import matplotlib.pyplot as plt

def main():
    X=[1,2,3,4,5]
    Y=[10,25,18,35,30]

    plt.plot(
        X,  #Value on x Axis
        Y,  # Value on Y axis
        marker="o", #The pointer 
        linestyle="--", # Style of line
        linewidth=2, # width of line
        markersize=7, # size of Pointer 
        label="Marks" 
    )
    
    plt.title("Marvellous Line Plot")
    plt.xlabel("Student Marks")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.legend()
    plt.show()
if __name__=="__main__":
    main()