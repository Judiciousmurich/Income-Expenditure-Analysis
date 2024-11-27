import os
import sys

# Define the project root and src paths
project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))  # Jupyter-compatible
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

# Print paths for debugging
print(f"Project root added to sys.path: {project_root}")
print(f"Source path added to sys.path: {src_path}")

# Import modules from src
try:
    from load_data import load_income_expense_data
    from income_statistics import calculate_income_statistics, categorize_income
    from visualizations import plot_income_distribution, plot_income_by_category
    print("Modules imported successfully!")
except ModuleNotFoundError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

def main():
    # Load data
    try:
        df = load_income_expense_data(project_root)
        if df is not None:
            print("\nData loaded successfully:")
            print(df.head())

            # Calculate income statistics
            income_stats = calculate_income_statistics(df)
            print("\nIncome Statistics:")
            for stat, value in income_stats.items():
                print(f"{stat}: {value}")

            # Add income categories to the dataframe
            df['Income_Category'] = categorize_income(df)
            print("\nIncome categories added to dataframe.")

            # Create visualizations
            plot_income_distribution(df)
            plot_income_by_category(df)
            print("\nVisualizations saved successfully in the 'outputs' folder.")
        else:
            print("Data loading failed. Please check the file path.")
    except Exception as e:
        print(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
