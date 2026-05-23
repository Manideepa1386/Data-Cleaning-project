import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r"C:\Users\MANIDEEPA\OneDrive\Desktop\data claeaning\netflix_titles.csv")

# Display original dataset
print("Original Dataset:")
print(data.head())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Remove missing values
data = data.dropna()

# Remove duplicates
data = data.drop_duplicates()

# Display cleaned data
print("\nCleaned Dataset:")
print(data.head())

# Dataset report
print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

# Visualization
data['release_year'].hist()

plt.title("Netflix Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Count")

plt.show()