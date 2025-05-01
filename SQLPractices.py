from sqlalchemy import create_engine
import pandas as pd

#df = pd.read_csv("employees_cleaned_data.csv")

# conn = mysql.connector.connect(host="localhost", user="root", password="12345", database="employee_data")

username = "root"
password = "12345"
host = "localhost"
database = "employee_data"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# Read SQL into DataFrame

query = " SELECT Department, MAX(Salary) FROM employees GROUP BY Department HAVING MAX(Salary) > 149650"
df = pd.read_sql(query, engine)

# Display results
print(df)