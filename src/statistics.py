import pandas as pd
import numpy as np

def calculate_income_statistics(df):
    """
    Calculate key statistics for income data.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing income data
    
    Returns:
    --------
    dict
        Dictionary of key income statistics
    """
    if df is None:
        return None
    
    income_stats = {
        'total_income': df['Income'].sum(),
        'average_income': df['Income'].mean(),
        'median_income': df['Income'].median(),
        'income_std_dev': df['Income'].std(),
        'min_income': df['Income'].min(),
        'max_income': df['Income'].max()
    }
    
    return income_stats

def categorize_income(df, bins=None):
    """
    Categorize income into predefined or custom bins.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing income data
    bins : list, optional
        Custom income bins. If None, uses default categorization
    
    Returns:
    --------
    pandas.Series
        Series of income categories
    """
    if bins is None:
        bins = [0, 20000, 40000, 60000, 80000, np.inf]
        labels = ['Low', 'Lower Middle', 'Middle', 'Upper Middle', 'High']
    else:
        labels = [f'Category {i+1}' for i in range(len(bins)-1)]
    
    return pd.cut(df['Income'], bins=bins, labels=labels)