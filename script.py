import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Load your CSV file
df = pd.read_csv('employees_cleaned_data.csv')

Department = df['Department'].unique()

print("-------------- Welcome to Employee Data --------------")
a = input("\tPress keys as you wish for "
          "\n1. You want to know total number of Department in this data "
          "\n2. You want know all names of Department in this data"
          "\n3. If you want to complete details of any Department "
          "\n4. Department-wise Gender Count (Pivot Table)"
          "\n5. Average salary per Department"
          "\n6. You want data visualization \n")

b = int(a)

match b:
    case 1:
        total_Department = len(df['Department'].unique())
        print("Total number of Department:", total_Department)

    case 2:
        print(df['Department'].unique())

    case 3:
        c = input(" Please select Team : \n "
                  "1.Finance  2.Engineering  3.Sales  4.Marketing  5.Operations  6.HR \n")
        index = int(c) - 1

        Department_count = len(df[df['Department'] == Department[index]])
        print(f"Number of employees in {Department[index]} Department : {Department_count}")
        df_Department = df[df['Department'] == Department[index]]
        gender_counts = df_Department.groupby(['Department', 'Gender']).size().unstack(fill_value=0)
        print(gender_counts)
        print("-----------------Details as below-------------------")
        pd.set_option('display.max_rows', None)
        print(df_Department)
        print("\n")

    case 4:
        print("Department-wise Gender Count (Pivot Table)")
        gender_counts = df.groupby(['Department', 'Gender']).size().unstack(fill_value=0)
        print(gender_counts)

    case 5:
        print("Average salary per Department")
        Department_stats = df.groupby('Department').agg({
            'Salary': ['mean', 'min', 'max'],
            'Bonus %': ['mean', 'std']})
        print(Department_stats)
    case 6:
        d = input(" Enter type of chart you want :"
                  "1. Bar Chart  2.Line Chart  3.Histogram  4.BoxPlot  5.ScatterPlot  6.Heatmap  7.PieChart  8.Treemap\n")
        e = int(d)
        match e:
            case 1:
                print("Best for: Categorical data (like Department, Gender, JobLevel), "
                      "compared against a numerical data (like Salary, Bonus %, PerformanceScore).")
                # Group by Department and calculate average Salary
                department_salary = df.groupby('Department')['Salary'].mean()

                # Plotting the bar chart
                department_salary.plot(kind='bar')
                plt.title('Average Salary by Department')
                plt.xlabel('Department')
                plt.ylabel('Average Salary')
                plt.show()

            case 2:
                print("Best for: Showing trends over time or continuous data. "
                      "Example: YearsExperience vs. Salary & YearsExperience vs. PerformanceScore")
                # Example: Line chart for YearsExperience vs. Salary
                plt.plot(df['YearsExperience'], df['Salary'])
                plt.title('Years of Experience vs. Salary')
                plt.xlabel('Years of Experience')
                plt.ylabel('Salary')
                plt.show()

            case 3:

                print("Best for: Displaying the distribution of a single numerical variable.")
                # Example: Histogram for Salary distribution
                df['Salary'].plot(kind='hist', bins=20, edgecolor='black')
                plt.title('Salary Distribution')
                plt.xlabel('Salary')
                plt.ylabel('Frequency')
                plt.show()

                # Example: Histogram for Age distribution
                df['Age'].plot(kind='hist', bins=20, edgecolor='black')
                plt.title('Age Distribution')
                plt.xlabel('Age')
                plt.ylabel('Frequency')
                plt.show()


            case 4:
                print("Best for: Showing the spread and identifying outliers in numerical data.")
                # Example: Boxplot for Salary distribution by Department
                sns.boxplot(x='Department', y='Salary', data=df)
                plt.title('Salary Distribution by Department')
                plt.show()

                # PerformanceScore by JobLevel
                sns.boxplot(x='PerformanceScore', y='JobLevel', data=df)
                plt.title('PerformanceScore Distribution by JobLevel')
                plt.show()

            case 5:
                print("Best for: Showing the relationship between two numerical variables.")
                # Example: Scatterplot for Salary vs. YearsExperience
                plt.scatter(df['YearsExperience'], df['Salary'])
                plt.title('Years of Experience vs. Salary')
                plt.xlabel('Years of Experience')
                plt.ylabel('Salary')
                plt.show()
                # Bonus % vs. PerformanceScore
                plt.scatter(df['PerformanceScore'], df['Bonus %'])
                plt.title('PerformanceScore vs. Bonus %')
                plt.xlabel('PerformanceScore')
                plt.ylabel('Bonus %')
                plt.show()
            case 6:
                print("Best for: Visualizing the correlation between multiple numerical variables."
                      "Correlation between Age, Salary, Bonus %, YearsExperience, and PerformanceScore:")

                # Calculate correlation matrix
                corr = df[['Age', 'Salary', 'Bonus %', 'YearsExperience', 'PerformanceScore']].corr()

                # Plot heatmap
                sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
                plt.title('Correlation Heatmap')
                plt.show()

            case 7:
                print("Best for: Visualizing the proportions of categorical data. "
                      "Gender Distribution And Department Distribution")

                # Example: Pie chart for Gender distribution
                gender_distribution = df['Gender'].value_counts()

                gender_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90)
                plt.title('Gender Distribution')
                plt.ylabel('')
                plt.show()

                # Example: Pie chart for Department distribution
                gender_distribution = df['Department'].value_counts()

                gender_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90)
                plt.title('Department Distribution')
                plt.ylabel('')
                plt.show()

            case 8:

                print("Best for: Visualizing hierarchical categorical data, with size representing numerical values."
                      "Department-wise Salary distribution And Department-wise Employee count")

                # Department-wise total salary for treemap
                department_salary = df.groupby('Department')['Salary'].sum()

                # Plot treemap
                squarify.plot(sizes=department_salary, label=department_salary.index, alpha=0.7,
                              color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])
                plt.title('Department-wise Salary Distribution')
                plt.axis('off')
                plt.show()

                # Department wise Employee Count for treemap

                department_counts = df['Department'].value_counts()
                squarify.plot(sizes=department_counts.values,
                              label=department_counts.index,
                              alpha=0.8,
                              color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6'])

                plt.title('Treemap of Department-wise Employee Count')
                plt.axis('off')  # Hide the axis
                plt.show()

            case _:
                print("please enter correct value")

    case _:
        print("please enter correct value")

