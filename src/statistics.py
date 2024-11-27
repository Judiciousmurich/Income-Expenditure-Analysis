# src/income_statistics.py

def calculate_mean(df, column):
    """Calculate the mean of a given column."""
    return df[column].mean()

def calculate_median(df, column):
    """Calculate the median of a given column."""
    return df[column].median()

def calculate_std_dev(df, column):
    """Calculate the standard deviation of a given column."""
    return df[column].std()
