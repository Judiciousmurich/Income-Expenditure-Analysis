import pandas as pd

def load_csv():
    
    file_path = "../data/Inc_Exp_Data.csv"  # Path to the CSV file
    try:
        data = pd.read_csv(file_path)
        print(f"Successfully loaded data from: {file_path}")
        return data
    except FileNotFoundError:
        print(f"File not found. Please check if the file exists at: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading CSV from {file_path}: {e}")
        return None

# Main script to load and display data
if __name__ == "__main__":
    data = load_csv()
    
    if data is not None:
        print("First 5 rows of the dataset:")
        print(data.head())
    else:
        print("Failed to load the dataset.")
