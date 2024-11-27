import matplotlib.pyplot as plt

def plot_bar(df, column):
    """Plot a bar chart for the given column."""
    df[column].value_counts().plot(kind="bar")
    plt.title(f"Bar chart for {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()

def plot_scatter(df, x_column, y_column):
    """Plot a scatter plot between two given columns."""
    df.plot(kind='scatter', x=x_column, y=y_column)
    plt.title(f"Scatter plot between {x_column} and {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
