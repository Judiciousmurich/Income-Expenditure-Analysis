def calculate_mean(data, column):
    """
    Calculate the mean of a specific column in the DataFrame.
    """
    return data[column].mean()

def calculate_median(data, column):
    """
    Calculate the median of a specific column in the DataFrame.
    """
    return data[column].median()

def calculate_std_dev(data, column):
    """
    Calculate the standard deviation of a specific column in the DataFrame.
    """
    return data[column].std()
