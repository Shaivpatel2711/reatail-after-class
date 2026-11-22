import numpy as np
import pandas as pd

# 1. Generate 60 sales transactions
np.random.seed(42)  # For reproducible results
n = 60

data = {
    'Transaction_ID': range(1001, 1001 + n),
    'Store': np.random.choice(['North', 'South', 'East', 'West'], size=n),
    'Category': np.random.choice(
        ['Electronics', 'Clothing', 'Home', 'Groceries'], size=n
    ),
    'Quantity': np.random.randint(1, 15, size=n),
    'Unit_Price': np.round(np.random.uniform(10.0, 200.0, size=n), 2),
    'Discount': np.random.choice([0.0, 0.05, 0.10, 0.15], size=n),
}

df = pd.DataFrame(data)

# 2. Add calculated revenue columns
df['Gross_Revenue'] = df['Quantity'] * df['Unit_Price']
df['Net_Revenue'] = np.round(df['Gross_Revenue'] * (1 - df['Discount']), 2)

# 3. Filter and sort data (e.g., transactions with Net Revenue > $500, sorted descending)
high_value_sales = df[df['Net_Revenue'] > 500].sort_values(
    by='Net_Revenue', ascending=False
)

# 4. Use groupby aggregation to find top-performing stores and categories
top_stores = (
    df.groupby('Store')['Net_Revenue']
    .agg(Total_Revenue='sum', Avg_Revenue='mean', Transaction_Count='count')
    .sort_values(by='Total_Revenue', ascending=False)
)

top_categories = (
    df.groupby('Category')['Net_Revenue']
    .agg(Total_Revenue='sum', Total_Units=('Quantity', 'sum'))
    .sort_values(by='Total_Revenue', ascending=False)
)


# 5. Apply a custom function using apply()
def categorize_sale(revenue):
  if revenue >= 1000:
    return 'High'
  elif revenue >= 300:
    return 'Medium'
  else:
    return 'Low'


df['Sale_Tier'] = df['Net_Revenue'].apply(categorize_sale)

# Display results
print('--- Sample Processed Data ---')
print(df.head())
print('\n--- Top Performing Stores ---')
print(top_stores)
print('\n--- Top Performing Categories ---')
print(top_categories)
