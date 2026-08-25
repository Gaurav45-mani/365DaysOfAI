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
