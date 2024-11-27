def calculate_mean(data, column):
    """
    Calculates the mean of a specified column.
    """
    return data[column].mean()

def calculate_median(data, column):
    """
    Calculates the median of a specified column.
    """
    return data[column].median()

def calculate_std_dev(data, column):
    """
    Calculates the standard deviation of a specified column.
    """
    return data[column].std()
