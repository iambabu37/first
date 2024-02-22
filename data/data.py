import pandas as pd
import sqlite3  # Example for SQLite, replace with your database library

# Connect to the database
conn = sqlite3.connect('db.sqlite3')  # Replace with your database connection details
cursor = conn.cursor()

# Get the list of tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Create an Excel writer
excel_writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

# Loop through each table and retrieve data
for table in tables:
    table_name = table[0]
    sheet_name = table_name[:31]
    
    # Execute SQL query to retrieve data for each table
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    
    # Create a DataFrame from the result set
    df = pd.DataFrame(data, columns=[column[0] for column in cursor.description])
    
    # Write the DataFrame to the Excel sheet
    df.to_excel(excel_writer, sheet_name=table_name, index=False)

# Save and close the Excel writer
excel_writer._save()

# Close the database connection
conn.close()
