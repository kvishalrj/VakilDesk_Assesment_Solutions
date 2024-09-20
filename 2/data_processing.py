import pandas as pd
import re

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Read CSV file
input_file = 'user_data.csv'  # Path to the input CSV file
output_file = 'cleaned_user_data.csv'  # Path to save the cleaned data

# Load the CSV data into a DataFrame
df = pd.read_csv(input_file)

# Remove duplicate entries based on 'user_id'
df_cleaned = df.drop_duplicates(subset='user_id')

# Filter rows with invalid email formats
df_cleaned = df_cleaned[df_cleaned['email'].apply(is_valid_email)]

# Write the cleaned data to a new CSV file
df_cleaned.to_csv(output_file, index=False)

print(f"Cleaned data has been saved to {output_file}")
