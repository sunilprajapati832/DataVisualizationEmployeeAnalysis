import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("employees_cleaned_data.csv")  # Make sure this file is correct

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="employee_data"
)

# Create cursor
cursor = conn.cursor()

# Create table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    EmployeeID INT PRIMARY KEY,
    Age INT,
    Salary FLOAT,
    BonusPercent FLOAT,
    YearsExperience FLOAT,
    PerformanceScore FLOAT,
    Department VARCHAR(50),
    Gender VARCHAR(10),
    JobLevel INT
)
""")

# Insert data
for i, row in df.iterrows():
    sql = """
    INSERT IGNORE INTO employees (
        EmployeeID, Age, Salary, BonusPercent, YearsExperience,
        PerformanceScore, Department, Gender, JobLevel
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        int(row['EmployeeID']),
        int(row['Age']),
        float(row['Salary']),
        float(row['Bonus %']),
        float(row['YearsExperience']),
        float(row['PerformanceScore']),
        row['Department'],
        row['Gender'],
        row['JobLevel']
    )
    cursor.execute(sql, values)

conn.commit()
cursor.close()
conn.close()
print("Data inserted successfully!")


# Connect again
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="employee_data"
)

# Query the database
query = "SELECT * FROM employees"
df = pd.read_sql(query, conn)

conn.close()

# Display data
print(df.head())

