import pandas as pd

df = pd.read_csv(r'C:\Users\Saqlain\Downloads\Compressed\train.csv_2.zip')

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Stats:\n", df.describe())

# Top selling category
print("\nTop Category by Sales:")
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))

# Top selling region
print("\nTop Region by Sales:")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

# Top 5 customers
print("\nTop 5 Customers by Sales:")
print(df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head())