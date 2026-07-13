import ssl
# Bypass SSL certification verification
ssl._create_default_https_context = ssl._create_unverified_context

import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = sns.load_dataset('iris')

print("First 3 rows")
print(df.head(3))
print("\n")

print("Summary")
print(df.describe())
print("\n")

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Boxplot
sns.boxplot(ax=axes[0], data=df, x="species", y="sepal_length", palette="Set2")
axes[0].set_title("Sepal Length Distribution")

# Plot 2: Scatterplot
sns.scatterplot(ax=axes[1], data=df, x="petal_length", y="petal_width", hue="species")
axes[1].set_title("Petal Width vs Petal Length")

plt.tight_layout()
plt.show()