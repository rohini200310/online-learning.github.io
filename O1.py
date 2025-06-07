import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load data
student=pd.read_csv('student_data.csv')

#display first few rows
print(student.head())



# EDA: Plot activity counts distribution
plt.figure(figsize=(8,5))
plt.hist(student['sessions_count'], bins=30, color='skyblue')
plt.title('Distribution of Student Activity Counts')
plt.xlabel('Number of Activities')
plt.ylabel('Number of Students')
plt.show()

# EDA: Scatter plot attendance vs average score
plt.figure(figsize=(8,5))
sns.scatterplot(data=student, x='sessions_count', y='avg_test_score', hue='dropped_out')
plt.title('Activity Count vs Average Score (Colored by Dropout)')
plt.show()

#Linear Regression

from sklearn.metrics import mean_squared_error
X = student[['sessions_count']]
y = student['avg_test_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)



# Calculate MSE
mse = mean_squared_error(y_test, y_pred)

# Manually compute RMSE
rmse = mse ** 0.5
print("RMSE:", rmse)
