import seaborn as sns
import matplotlib.pyplot as plt

def plot_bar(data, column):
    """
    Plots a bar chart for the specified column.
    """
    data[column].value_counts().plot(kind="bar")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()

def plot_scatter(data, x_column, y_column):
    """
    Plots a scatter plot between two columns.
    """
    data.plot(x=x_column, y=y_column, kind="scatter", alpha=0.5)
    plt.title(f"{x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
