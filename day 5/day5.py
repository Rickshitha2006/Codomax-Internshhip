import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print(df.head())
print("Dataset Information")
print(df.info())
print(df.shape)
print(df.columns)

print("Checking Missing Values")
print(df.isnull().sum())

print("Remove missing vlaues")
df = df.dropna()

print(df.isnull().sum())
