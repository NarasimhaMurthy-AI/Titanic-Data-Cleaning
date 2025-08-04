import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv(r"D:\AIML PROJECTS\Titanic-Dataset.csv")

# Show first few rows
print(df.head())

# Show null value summary
print(df.isnull().sum())

# Show basic data types
print(df.info())
# Drop 'Cabin'
df.drop(columns=['Cabin'], inplace=True)

# Fill Age with median
df.loc[:, 'Age'] = df['Age'].fillna(df['Age'].median())

# Fill Embarked with mode
df.loc[:, 'Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Check again for nulls
print(df.isnull().sum())

# Drop unhelpful columns
df.drop(columns=['Name', 'Ticket'], inplace=True)

# Convert categorical to numerical using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

print(df_encoded.head())

# Select numeric columns for scaling
cols_to_scale = ['Age', 'Fare', 'SibSp', 'Parch']

scaler = StandardScaler()
df_encoded[cols_to_scale] = scaler.fit_transform(df_encoded[cols_to_scale])

print(df_encoded[cols_to_scale].head())

# Boxplot for outliers
sns.boxplot(x=df_encoded["Fare"])
plt.show()

# Remove extreme outliers in Fare (>99th percentile)
q99 = df_encoded["Fare"].quantile(0.99)
df_encoded = df_encoded[df_encoded["Fare"] < q99]

# Save the cleaned and processed dataset to a CSV file
# Only display — do not assign print result
print(df_encoded.head())

# Save
df_encoded.to_csv(r"D:\AIML PROJECTS\cleaned_titanic.csv", index=False)


