import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=[23,34,5,23,54,53,32,43,59]
print("DATASET:",dataset)

#Previous day revision
#Find mean value of the dataset
mean=np.mean(dataset)
print("Mean value of the dataset:",mean)

#Find median value of the dataset
median=np.median(dataset)
print("Median value of the dataset:",median)

#Find mode value of the dataset
mode=np.bincount(dataset).argmax()
print("Mode value of the dataset:",mode)

#Find variance value of the dataset
#Population Variance
variance=np.var(dataset)
print("Population variance value of the dataset:",variance)
#Sample Variance
variance_sample=np.var(dataset,ddof=1)
print("Sample variance value of the dataset:",variance_sample)

#Find standard deviation value of the dataset
#Population Standard Deviation
std_dev=np.std(dataset)
print("Population Standard Deviation value of the dataset:",std_dev)
#Sample Standard deviation
std_dev_sample=np.std(dataset,ddof=1)
print("Sample Standard deviation value of the dataset:",std_dev_sample)

df=pd.DataFrame({"Dataset":dataset})
print("Pandas variance:")
print(df.var())

print("Pandas standard deviation:")
print(df.std())

#Histogram
plt.hist(dataset,bins=5,edgecolor='black')
plt.title("Histogram of the dataset")
plt.xlabel("Data values")
plt.ylabel("Frequency")
plt.savefig("Histogram_output.png")
plt.show()
