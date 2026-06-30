import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Saqlain\Downloads\Compressed\train.csv_2.zip')

# Chart 1 — Sales by Category
df.groupby('Category')['Sales'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.ylabel('Sales')
plt.savefig('chart1_category.png')
plt.show()

# Chart 2 — Sales by Region
df.groupby('Region')['Sales'].sum().plot(kind='bar', color='orange')
plt.title('Total Sales by Region')
plt.ylabel('Sales')
plt.savefig('chart2_region.png')
plt.show()