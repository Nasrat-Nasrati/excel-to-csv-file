import os
import pandas as pd

# Create output directory if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")

# Load the Excel file
df = pd.read_excel("data/AnswerKey-2.xlsx")  # Replace with your actual file name

# Try to save as CSV
try:
    df.to_csv("output/output_file.csv", index=False)  # Specify the output file name
    print("Your file is created successfully")
except Exception as e:
    print("Sorry, your file is not processed. Try again later.")
    print(f"Error: {e}")