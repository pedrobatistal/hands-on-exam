#4. Use a data processing library of your choice to open the provided CSV file in this test. Load the CSV and efficiently organize the numbers in descending order using appropriate sorting methods. After the sorting process, save the data to another CSV file with the sorted numbers. Be sure to document the process and provide clear, commented code for completing this task. (1 point)

# Note: Angelo, the prompt mentioned a provided CSV file, but I couldn't find it. 
# I used a generic name in the code and assumed a "numbers" column in the file since the task requires sorting numbers.

import pandas as pd

# Function to load CSV, sort numbers, and save to another CSV
def sort_and_save_csv(input_file, output_file):
    # Load CSV into a DataFrame
    df = pd.read_csv(input_file)

    # Check if the DataFrame has a column named 'numbers'
    if 'numbers' not in df.columns:
        raise ValueError("The CSV file should have a column named 'numbers'.")

    # Sort DataFrame by the 'numbers' column in descending order
    df_sorted = df.sort_values(by='numbers', ascending=False)

    # Save the sorted DataFrame to another CSV file
    df_sorted.to_csv(output_file, index=False)

# Example: Sort and save CSV file
input_csv_file = 'input_numbers.csv'  # Replace with your input file name
output_csv_file = 'output_sorted_numbers.csv'  # Replace with your output file name

try:
    sort_and_save_csv(input_csv_file, output_csv_file)
    print(f"CSV file '{output_csv_file}' created with sorted numbers.")
except Exception as e:
    print(f"Error: {e}")