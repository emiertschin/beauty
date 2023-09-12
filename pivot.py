import pandas as pd

# Read the CSV file
df = pd.read_csv("high_benefits.csv", usecols=['ID', 'Name', 'Brand', 'Price', '1', '2', '3', '4', '5', '6', '7'])

# Iterate through the DataFrame
for index, row in df.iterrows():
    for col_name in ['1', '2', '3', '4', '5', '6', '7']:
        cell_value = row[col_name]
        if not pd.isnull(cell_value):  # Check if the cell is not empty
            print(row['ID'],":"+cell_value)
