import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

df.head()

df.info()

df.describe()

print("Survival Counts:\n", df['Survived'].value_counts(), "\n")
print("Passenger Class Counts:\n", df['Pclass'].value_counts(), "\n")
print("Sex Counts:\n", df['Sex'].value_counts(), "\n")
print("Embarked Counts:\n", df['Embarked'].value_counts(), "\n")

df_plot = df.copy()

df_plot['Sex'] = df_plot['Sex'].map({'male': 0, 'female': 1})
df_plot['Embarked'] = df_plot['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

sns.pairplot(df_plot[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']])
plt.suptitle("Pairplot of Survival vs Key Features", y=1.02)
plt.show()

numeric_df = df_plot.select_dtypes(include='number')

plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(df['Age'].dropna(), kde=True, bins=30, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Age Distribution Across Passenger Classes')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title('Fare vs Age (Colored by Survival)')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend(title='Survived')
plt.show()

print("\n🔍 Summary of EDA Findings")
print(f"- Total passengers: {len(df)}")
print(f"- Survival rate: {df['Survived'].mean() * 100:.2f}%")
print("- Women had a much higher survival rate than men.")
print("- 1st class passengers had better survival.")
print("- Age and Fare show meaningful spread and trends.")
print("- 'Cabin' column dropped due to many missing values.")