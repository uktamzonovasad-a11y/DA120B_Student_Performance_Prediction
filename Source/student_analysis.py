import pandas as pd

print("Student Performance Prediction")

dataset_path = "Data/student.csv"

try:
    df = pd.read_csv(dataset_path)

    print(df.head())
    print(df.info())
    print(df.describe())

except FileNotFoundError:
    print("Dataset will be added later.")
