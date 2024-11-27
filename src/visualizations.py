import matplotlib.pyplot as plt
import seaborn as sns

def plot_income_distribution(df):
    """
    Create a histogram of income distribution.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing income data
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Income', kde=True)
    plt.title('Income Distribution')
    plt.xlabel('Income')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('income_distribution.png')
    plt.close()

def plot_income_by_category(df):
    """
    Create a box plot of income by category.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing income data with categories
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Income_Category', y='Income', data=df)
    plt.title('Income Distribution by Category')
    plt.xlabel('Income Category')
    plt.ylabel('Income')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('income_by_category.png')
    plt.close()