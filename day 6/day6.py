"""print("Bar Chart (Average Math Score by Gender)")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

avg_math = df.groupby("gender")["math score"].mean()

plt.bar(avg_math.index, avg_math.values)

plt.title("Average Math Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Math Score")

plt.show()
"""
print(" Line Chart (Math Scores of First 20 Students)")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

plt.plot(df.index[:20], df["math score"][:20], marker='o')

plt.title("Math Scores of First 20 Students")
plt.xlabel("Student Index")
plt.ylabel("Math Score")

plt.grid(True)

plt.show()
