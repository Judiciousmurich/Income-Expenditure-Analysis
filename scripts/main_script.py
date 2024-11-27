import os
import sys

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.load_data import load_income_expense_data
from src.income_statistics import calculate_income_statistics, categorize_income
from src.visualizations import plot_income_distribution, plot_income_by_category

def main():
    # Load the data
    df = load_income_expense_data(project_root)
    
    if df is not None:
        # Calculate income statistics
        income_stats = calculate_income_statistics(df)
        print("Income Statistics:")
        for stat, value in income_stats.items():
            print(f"{stat}: {value}")
        
        # Add income categories to the dataframe
        df['Income_Category'] = categorize_income(df)
        
        # Create visualizations
        plot_income_distribution(df)
        plot_income_by_category(df)
        
        print("\nVisualizations have been saved in the project directory.")
    else:
        print("Failed to load data. Please check the file path and data.")

if __name__ == "__main__":
    main()