# Data Visualization Employee Analysis
A comprehensive end-to-end employee analytics project that demonstrates how Python, SQL, and Data Visualization can be combined to extract insights from real-world HR data. The project covers CSV-based analysis, MySQL database integration, SQL querying and interactive visual exploration using multiple chart types.


## Project Overview
This project analyzes an employee dataset (2000+ records) containing numerical and categorical attributes such as: Salary, Age, Bonus %, Performance Score, Years of Experience, Job Level, Department, Gender

The goal is to:
- Perform exploratory data analysis (EDA)
- Choose the right visualization technique for each data type
- Integrate MySQL with Python for scalable, query-driven analysis
- Practice advanced SQL queries used in real-world analytics

## Dataset Details
File: employees_cleaned_data.csv (2000+ employee records)
| Column Name      | Data Type   | Description                |
| ---------------- | ----------- | -------------------------- |
| EmployeeID       | Integer     | Unique employee identifier |
| Age              | Integer     | Employee age               |
| Salary           | Float       | Annual salary              |
| Bonus %          | Float       | Bonus percentage           |
| YearsExperience  | Float       | Total experience           |
| PerformanceScore | Float       | Performance rating         |
| Department       | Categorical | Employee department        |
| Gender           | Categorical | Gender                     |
| JobLevel         | Integer     | Job hierarchy level        |


## Technolgy
| Category        | Tools Used                    |
| --------------- | ----------------------------- |
| Programming     | Python                        |
| Data Analysis   | Pandas                        |
| Visualization   | Matplotlib, Seaborn, Squarify |
| Database        | MySQL                         |
| SQL Integration | SQLAlchemy, MySQL Connector   |
| Environment     | Local Machine                 |

## Project Structure
| File Name                  | Purpose                                   |
| -------------------------- | ----------------------------------------- |
| employees_cleaned_data.csv | Cleaned employee dataset                  |
| script.py                  | Interactive analysis & visualization menu |
| mysql_upload.py            | CSV → MySQL data insertion                |
| mysql_upload1.py           | SQLAlchemy-based MySQL integration        |
| SQLPractices.py            | Advanced SQL analytical queries           |
| README.md                  | Project documentation                     |

## Key Functionalities
### Interactive Employee Analysis (script.py)
A menu-driven Python program that allows users to:
- View total number of departments
- List all departments
- Analyze department-wise employee details
- Generate pivot tables (Department × Gender)
- Calculate department-wise salary & bonus statistics
- Create multiple visualizations interactively

### MySQL Data Upload (mysql_upload.py)
- Reads employee data from CSV
- Creates employees table in MySQL
- Inserts records using INSERT IGNORE
- Fetches data back into Pandas for validation

### SQL + Python Integration (mysql_upload1.py)
Enhanced version with SQLAlchemy integration
- Connects MySQL with Python using SQLAlchemy
- Performs database reads directly into Pandas DataFrames
- Enables scalable SQL-based analytics
This update simulates real-world analytics pipelines, where data lives in databases—not CSV files.

### Advanced SQL Practice (SQLPractices.py)
SQL queries commonly asked in interviews:
- Employees earning above department average salary
- Nth highest salary using window functions
- Second highest salary using subqueries
- Department-wise maximum salary with conditions

### Key Insights Generated
- Salary growth trends with experience
- Department-wise salary inequality & outliers
- Gender distribution across departments
- Strong correlations between salary, experience and performance
- Department contribution to total salary expense

## Visualizations Used
| Chart Type   | Best Used For            | Example Insight                  |
| ------------ | ------------------------ | -------------------------------- |
| Bar Chart    | Categorical vs Numerical | Avg salary by department         |
| Line Chart   | Trend Analysis           | Experience vs salary             |
| Histogram    | Distribution             | Salary & age spread              |
| Box Plot     | Outliers & spread        | Department salary variation      |
| Scatter Plot | Relationships            | Bonus % vs performance           |
| Heatmap      | Correlation              | Salary, age, experience          |
| Pie Chart    | Proportions              | Gender & department ratio        |
| Treemap      | Hierarchical view        | Salary & headcount by department |

## Connect with Me 🤝
If you found this project interesting, let’s connect!  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Follow%20Me-blue?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/in/sunil-prajapati832)
