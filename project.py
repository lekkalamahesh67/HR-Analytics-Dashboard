import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Database Connection


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mahesh@1234",
    database="hr_project"
)


# Read Data


query = "SELECT * FROM emp"

df = pd.read_sql(query, conn)

print("========== HR ANALYTICS DASHBOARD ==========\n")


# Basic Information


print("First 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())

print("\nColumn Names")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())


# KPI's


print("\n========== KPI'S ==========\n")

print("Total Employees :", len(df))

print("Average Salary :", df["salary"].mean())

print("Highest Salary :", df["salary"].max())

print("Lowest Salary :", df["salary"].min())

print("Average Experience :", df["experience"].mean())


# Filtering


print("\nEmployees from Hyderabad")
print(df[df["city"]=="Hyderabad"])

print("\nEmployees Salary Greater than 50000")
print(df[df["salary"]>50000])

# Sorting


print("\nSalary Ascending")
print(df.sort_values("salary"))

print("\nSalary Descending")
print(df.sort_values("salary",ascending=False))


# Group By


print("\nDepartment Wise Average Salary")

dept_salary=df.groupby("dept")["salary"].mean()

print(dept_salary)

print("\nDepartment Wise Employee Count")

dept_count=df.groupby("dept")["emp_id"].count()

print(dept_count)

print("\nDepartment Wise Maximum Salary")

print(df.groupby("dept")["salary"].max())


# Value Counts

print("\nGender Count")

gender=df["gender"].value_counts()

print(gender)

# Apply Function

df["Bonus"]=df["salary"].apply(lambda x:x*0.10)

print("\nEmployee Bonus")

print(df[["ename","salary","Bonus"]])


# Correlation


print("\nCorrelation Between Salary and Experience")

correlation=df["salary"].corr(df["experience"])

print(correlation)


# Charts


plt.figure(figsize=(6,4))

plt.bar(dept_count.index,dept_count.values)

plt.title("Department Wise Employee Count")

plt.xlabel("Department")

plt.ylabel("Employees")

plt.show()

plt.figure(figsize=(6,6))

plt.pie(gender.values,
labels=gender.index,
autopct="%1.1f%%")

plt.title("Gender Distribution")

plt.show()

plt.figure(figsize=(6,4))

plt.hist(df["salary"],bins=5)

plt.title("Salary Distribution")

plt.xlabel("Salary")

plt.ylabel("Frequency")

plt.show()

plt.figure(figsize=(6,4))

plt.scatter(df["experience"],df["salary"])

plt.title("Experience vs Salary")

plt.xlabel("Experience")

plt.ylabel("Salary")

plt.show()

plt.figure(figsize=(6,4))

sns.boxplot(y=df["salary"])

plt.title("Salary Outliers")

plt.show()

plt.figure(figsize=(6,4))

sns.countplot(x="dept",data=df)

plt.title("Department Count")

plt.show()

corr=df.corr(numeric_only=True)

plt.figure(figsize=(8,6))

sns.heatmap(corr,annot=True,cmap="Blues")

plt.title("Correlation Heatmap")

plt.show()


# Top Performers


print("\nTop Performers")

top=df[df["performance_rating"]==5]

print(top)


# Business Insights


print("\n========== BUSINESS INSIGHTS ==========\n")

print("Highest Paid Employee")

print(df.loc[df["salary"].idxmax()])

print("\nLowest Paid Employee")

print(df.loc[df["salary"].idxmin()])

print("\nAverage Salary Department Wise")

print(dept_salary)

print("\nEmployee Count Department Wise")

print(dept_count)

print("\nCorrelation Between Salary and Experience")

print(correlation)

print("\n========== PROJECT COMPLETED ==========")

conn.close()

# hr_analyatics.py
