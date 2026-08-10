import numpy as np
dataset=[1,2,3,4,5,6,7,8,8,9]

#Find mean value of the dataset
mean=np.mean(dataset)
#Find median value of the dataset
median=np.median(dataset)
#Find mode value of the dataset
mode=np.bincount(dataset).argmax()

print("Mean:",mean)
print("Median:",median)
print("Mode:",mode)


# Example of qualitative and quantitative data
qualitative = ["Good", "Average", "Bad"]
quantitative = [5, 4, 3, 2, 1]

print("Qualitative:", qualitative)
print("Quantitative:", quantitative)
