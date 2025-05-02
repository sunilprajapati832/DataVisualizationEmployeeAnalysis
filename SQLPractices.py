from sqlalchemy import create_engine
import pandas as pd

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
