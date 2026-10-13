
import pandas as pd
import matplotlib.pyplot as plt

# 1. Store the student data in Python lists
data = {
    "Name": [
        " ali", "SARA ", "bilal", " Ayesha",
        "HAMZA", "zain ", "Noor", " usman "
    ],
    "Marks": [
        "72", "85", "absent", "64",
        "90", "78", "81", "69"
    ]
}

# 2. Create a DataFrame
df = pd.DataFrame(data)

# 3. Clean student names
# Remove extra spaces and capitalize the first letter
df["Name"] = df["Name"].str.strip().str.title()

# 4. Convert Marks to numeric values
# "absent" will become NaN because it is not a number
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# 5. Replace the missing mark with the mean of the other marks
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

# 6. Print the cleaned DataFrame
print("Cleaned DataFrame:")
print(df)

# 7. Create a bar plot of marks per student
plt.figure(figsize=(8, 5))

plt.bar(df["Name"], df["Marks"])

# Add title and axis labels
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")

# Adjust the layout
plt.tight_layout()

# 8. Save the plot in the current folder
plt.savefig("marks_bar.png")

print("\nSaved marks_bar.png")

# 9. Display the plot
plt.show()
