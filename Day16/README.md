📊 Day 16 – Chi-Square Test & Goodness of Fit Test in Python

📅 Date

25 August 2026

📚 Topics Covered

1. Chi-Square Test Overview
A non-parametric statistical test used to analyze categorical data (nominal and ordinal) rather than numerical/continuous measurements. It is primarily used to evaluate relationships between categorical variables or to compare sample distributions against theoretical population proportions.

2. Chi-Square Goodness of Fit Test
A hypothesis testing method used to determine whether observed frequency counts from a sample align with expected theoretical distributions.
• Observed Data (O): Real-world categorical frequency counts collected from experiments.
• Expected Data (E): Theoretical frequency counts expected if the null hypothesis is true.
• Mathematical Condition: Total observed sum must equal total expected sum (Σ Observed = Σ Expected).
• Formula: χ² = Σ [(O - E)² / E]

3. Python Implementation with SciPy
Using computational statistical libraries to calculate Chi-Square test statistics, p-values, degrees of freedom, and critical values using `scipy.stats.chisquare` and `scipy.stats.chi2.ppf`.

🧠 Step-by-Step Theoretical & Computational Framework

Example 1: Categorical Distribution Matching
• Bike Color Preference: Comparing theoretical equal distribution (1/3 each for Yellow, Orange, Red) against observed sample counts (22, 17, 59).
• Handedness Test: Class of 100 students tested against a 12% right-handed theory (Observed: 30 Right, 70 Left vs. Expected: 12 Right, 88 Left).

Example 2: Python Code & Weekly Study Hours Analysis
• Expected study hours: [8, 6, 7, 9, 6, 9, 7] (Sum = 52)
• Observed study hours: [7, 8, 6, 9, 9, 6, 7] (Sum = 52)
• Hypotheses:
  - H0: Observed study hours match the expected theoretical study hours.
  - H1: Observed study hours significantly differ from the expected hours.

Python Computation & Decision Logic:
```python
import numpy as np
import scipy.stats as stat

expected_data = [8, 6, 7, 9, 6, 9, 7]
observed_data = [7, 8, 6, 9, 9, 6, 7]

# Chi-Square Goodness of Fit Test
chisquare_stat, p_value = stat.chisquare(observed_data, expected_data)
# chisquare_stat ≈ 3.4345, p_value ≈ 0.7526

# Critical Value Calculation
significance_value = 0.05
dof = len(expected_data) - 1  # 7 - 1 = 6
critical_value = stat.chi2.ppf(1 - significance_value, dof)  # ≈ 12.59

# Decision
if chisquare_stat > critical_value:
    print("Reject the null hypothesis")
else:
    print("Accept the null hypothesis")
