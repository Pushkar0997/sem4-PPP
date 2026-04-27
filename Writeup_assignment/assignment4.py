import pandas as pd
from pathlib import Path


csv_path = Path(__file__).resolve().parent.parent / "students.csv"
df = pd.read_csv(csv_path)

print("Dataset:")
print(df)

print("\nBasic Statistics (numeric columns):")
print("Mean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nMode:\n", df.mode(numeric_only=True).iloc[0])

# Frequently Asked Questions (2-line answers)
# 1. What is a CSV file?
# A CSV file is a plain-text file that stores tabular data using commas to separate values.
# It is commonly used for sharing data between tools like Excel, databases, and Python.

# 2. How does Pandas handle missing values?
# Pandas reads missing values as NaN by default and provides functions like isna() and fillna().
# You can remove missing data with dropna() or replace it with suitable values.

# 3. Can this program handle large datasets?
# Yes, Pandas can handle large datasets, but performance depends on available RAM.
# For very large files, use chunking (chunksize) or libraries like Dask.

# 4. How can I calculate statistics for a specific column?
# Use column selection, for example: df['Marks'].mean(), df['Marks'].median(), df['Marks'].mode().
# This returns statistics only for that selected column.
