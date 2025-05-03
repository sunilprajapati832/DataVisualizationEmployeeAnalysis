from sqlalchemy import create_engine
import pandas as pd

username = "root"
password = "12345"
host = "localhost"
database = "employee_data"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# Read SQL into DataFrame
""" Employees with above average salary in their department
query = " SELECT * FROM employees e WHERE Salary > (SELECT AVG(Salary) FROM employees WHERE Department = e.Department) "
"""
""" Nth Highest Salary
query = " SELECT Salary FROM ( SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS rnk FROM employees ) tmp WHERE rnk = 3"
"""
"""Second Highest Salary
query = "SELECT MAX(Salary) FROM employees WHERE Salary < (SELECT MAX(Salary) FROM employees)"

"""
query = " SELECT Department, MAX(Salary) FROM employees GROUP BY Department HAVING MAX(Salary) > 149650"
df = pd.read_sql(query, engine)

# Display results
print(df)
