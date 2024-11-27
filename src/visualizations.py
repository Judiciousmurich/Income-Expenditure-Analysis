import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(data, column):
    """
    Plot a bar chart of a specific column in the DataFrame.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x=column)
    plt.title(f"Bar Chart of {column}")
    plt.xticks(rotation=45)
    plt.show()

def plot_scatter(data, x_column, y_column):
    """
    Plot a scatter plot for two columns in the DataFrame.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_column, y=y_column)
    plt.title(f"Scatter Plot of {x_column} vs {y_column}")
    plt.show()
