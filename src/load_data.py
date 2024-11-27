import pandas as pd
import os

def load_income_expense_data(data_path = os.path.join(project_root, 'data', 'Inc_Exp_Data.csv')):
    """
    Load income and expense data from a CSV file.
    
    Parameters:
    -----------
    data_path : str
        Path to the CSV file containing income and expense data
    
    Returns:
    --------
    pandas.DataFrame
        Loaded dataframe with income and expense information
    """
    try:
        # Check if file exists
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"The file {data_path} does not exist.")
        
        # Read the CSV file
        df = pd.read_csv(data_path)
        
        # Basic data validation
        if df.empty:
            print("Warning: The loaded dataframe is empty.")
        
        return df
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return None