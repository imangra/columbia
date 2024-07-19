#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"/Users/ianmangra/Downloads/cereal.csv")

print("First 5 rows of the dataset:")
print(data.head())

print("\nDescription of the dataset:")
print(data.describe())

correlation_matrix = data.corr()

print("\nCorrelation matrix:")
print(correlation_matrix)

highest_corr = correlation_matrix.unstack().sort_values(ascending=False)
highest_corr = highest_corr[highest_corr < 1].idxmax()
lowest_corr = correlation_matrix.unstack().sort_values().idxmin()

print(f"\nHighest correlation: {highest_corr} with a value of {correlation_matrix.loc[highest_corr]}")
print(f"Lowest correlation: {lowest_corr} with a value of {correlation_matrix.loc[lowest_corr]}")

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Cereal Dataset')
plt.show()


# %%
