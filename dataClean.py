import pandas as pd

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv('C:/Users/ADMIN/Desktop/DataAnalysis/car_prices.csv')
    
    # Filter rows where 'vin' column contains '9-May'
    matching_rows = df[df['model'].str.contains('-', na=False)]
    
    # Count the number of matching rows
    number_of_matching_rows = matching_rows.shape[0]
    print(f"Number of rows containing '-' in the 'model' column: {number_of_matching_rows}")
    
    total_rows_len = len(df)
    print(f"Total number of rows (using len): {total_rows_len}")
    
    # Delete the matching rows
    df_cleaned = df[~df['model'].str.contains('-', na=False)]
    
    # Count the number of rows after deletion
    total_rows_after_deletion = len(df_cleaned)
    print(f"Total number of rows after deletion: {total_rows_after_deletion}")

    # Optionally, save the cleaned DataFrame back to a CSV file
    df_cleaned.to_csv('C:/Users/ADMIN/Desktop/DataAnalysis/car_prices_cleaned.csv', index=False)

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print("Error occurred while processing the file:", e)
