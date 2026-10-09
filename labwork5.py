Data Manipulation
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("students.csv")

# 2. Display first five rows
print("--- First 5 rows ---")
print(df.head())

# 3. Find number of rows and columns
rows, cols = df.shape
print(f"\nNumber of rows: {rows}, Number of columns: {cols}")

# 4. Select name and GPA
print("\n--- Name and GPA ---")
print(df[["name", "GPA"]])

# 5. Find students with GPA >= 3.5
high_gpa = df[df["GPA"] >= 3.5]
print("\n--- Students with GPA >= 3.5 ---")
print(high_gpa)

# 6. Sort students by GPA (descending order)
sorted_df = df.sort_values(by="GPA", ascending=False)
print("\n--- Sorted by GPA ---")
print(sorted_df)

# 7. Find average GPA by major
avg_gpa_by_major = df.groupby("major")["GPA"].mean()
print("\n--- Average GPA by Major ---")
print(arg_gpa_by_major)

From raw data to useful info
import pandas as pd

# 1. Load both files
df_students = pd.read_csv("students.csv")
df_scores = pd.read_csv("scores.csv")

# 2. Check missing values
print("Missing values in students:", df_students.isnull().sum())
print("Missing values in scores:", df_scores.isnull().sum())

# 3. Fill or remove missing data appropriately
df_students = df_students.dropna()
df_scores = df_scores.fillna(df_scores["score"].mean())

# 4. Merge the two datasets
merged_df = pd.merge(df_students, df_scores, on="student_id")
print("\n--- Merged Dataset ---")
print(merged_df.head())

# 5. Calculate each student's average score
student_avg = (
    merged_df.groupby(["student_id", "name"])["score"].mean().reset_index()
)
print("\n--- Each Student's Average Score ---")
print(student_avg)

# 6. Find the top 5 students
top5 = student_avg.sort_values(by="score", ascending=False).head(5)
print("\n--- Top 5 Students ---")
print(top5)

# 7. Compute average score by major
major_avg = merged_df.groupby("major")["score"].mean()
print("\n--- Average Score by Major ---")
print(major_avg)
