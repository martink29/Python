import pandas as pd
from tabulate import tabulate

data = {
    "Brand": ["Toyota", "BMW", "Ford"],
    "Country": ["Japan", "Germany", "USA"],
    "Year Founded": [1937, 1916, 1903]
}

df = pd.DataFrame(data)

print("Original Table:")
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

df.to_csv("cars.csv", index=False)

df2 = pd.read_csv("cars.csv")

print("\nTable Read from CSV:")
print(tabulate(df2, headers="keys", tablefmt="grid", showindex=False))