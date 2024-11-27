import sys
import os

# Add the 'src' directory to the system path so the modules can be imported
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))

# Import necessary modules from src
from load_data import load_csv
from statistics import calculate_mean, calculate_median, calculate_std_dev
from visualizations import plot_bar, plot_scatter

def main():
    # Load the data
    data = load_csv()
    
    if data is not None:
        # Example: Calculate and print the mean of a specific column
        mean_exp = calculate_mean(data, 'Mthly_HH_Expense')
        print(f"Mean Household Expense: {mean_exp}")

        # Example: Plot a bar chart for the Highest Qualified Member
        plot_bar(data, 'Highest_Qualified_Member')

if __name__ == "__main__":
    main()
