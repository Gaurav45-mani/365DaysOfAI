import numpy as np
import pandas as pd
import matplotlib .pyplot as plt

# Sample data
maths_marks=[50,60,70,80,90]
science_marks=[48,66,69,87,91]

df=pd.DataFrame({
    "Maths":maths_marks,
    "Science":science_marks
})
print(df)

# Covariance
print("Covariance between Maths and Science marks:")
print(df.cov())

# Pearson correlation coefficient
print("Pearson correlation coefficient between Maths and Science marks:")
print(df.corr(method='pearson'))

# Spearman correlation coefficient
print("Spearman correlation coefficient between Maths and Science marks:")
print(df.corr(method='spearman'))

# Scatter Plot (Positive Correlation)
plt.scatter(maths_marks,science_marks)
plt.title("Scatter Plot of Maths vs Science Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Science Marks")
plt.grid(True)
plt.show()


# Scatter Plot (Negative Correlation)
x=[10,20,30,40,50]
y=[100,90,80,70,60]
plt.scatter(x,y)
plt.title("Scatter Plot of x and y (Negative Correlation)")
plt.xlabel("x values")
plt.ylabel("y values")
plt.grid(True)
plt.show()

