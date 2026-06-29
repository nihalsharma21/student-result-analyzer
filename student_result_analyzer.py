import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("student-result-analyzer/student_analyzer.csv")

# Calculate Total and Average
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

# Assign Grades
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"
df["Grade"] = df["Average"].apply(grade)

# Find Top Performer
top_student = df.loc[df["Total"].idxmax()]
print("\n========== STUDENT RESULT ANALYZER ==========\n")
print(df)
print("\n========== TOP PERFORMER ==========")
print("Name :", top_student["Name"])
print("Total Marks :", top_student["Total"])
print("Average :", round(top_student["Average"], 2))
print("Grade :", top_student["Grade"])

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Total"])
plt.title("Student Total Marks")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie Chart
grade_count = df["Grade"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    grade_count,
    labels=grade_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Grade Distribution")
plt.show()