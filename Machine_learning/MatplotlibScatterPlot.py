import matplotlib.pyplot as plt


def main():
    study_hours=[1,2,3,4,5,6,7,9]
    marks=[35,42,50,62,72,85,90,95]
    plt.scatter(
        study_hours,
        marks,
        s=100,
        marker="o",
        alpha=0.8,
        egdecolor="black",
        linewidth=1,
        label="Student"
    )
    plt.title("Marvellous Scatter plot")
    plt.xlabel("Study Hours")
    plt.ylabel("Obtanined Marks")
    plt.grid(True)
    plt.legend()
    plt.show()
if __name__=="__main__":
    main()