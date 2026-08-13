import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import scipy for statistical functions 
from scipy.stats import bernoulli
p= 0.6

print("X=1:", bernoulli.pmf(1, p))
print("X=0:", bernoulli.pmf(0, p))

# Mean using Bernoulli distribution
print("Mean:", bernoulli.mean(p))

# Variance using bernoulli Distribution
# Variance = p*(1-p)
print("Variance:", bernoulli.var(p))

# Standard Deviation using bernoulli Distribution 
print("Standard Deviation:", bernoulli.std(p))

# PMF Plot
x=[0,1]
y=bernoulli.pmf(x,p)
plt.bar(x,y)
plt.title("Bernoulli Distribution PMF")
plt.xlabel("x")
plt.ylabel("Probability")
plt.xticks([0,1],["failure (0)","success (1)"])
plt.grid(axis='y')
plt.show()

# Frequency Plot of Simulation 
sample=np.random.binomial(1,p,1000)
plt.hist(sample,bins=2,rwidth=0.8)
plt.xticks([0,1],["failure (0)" , "success (1)"])
plt.title("Bernoulli distribution Frequency Plot")
plt.grid(axis='y')
plt.show()
