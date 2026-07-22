import pandas as pd

df = pd.read_csv("pos_tags.csv")

print("5 Rows of the table")
print(df.head())

print("information the table")
print(df.info())

print("Columns of the table")
print(df.columns)
