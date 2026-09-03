import numpy as np
import scipy.stats as stats

# ============================================================
# 1. Descriptive Statistics (Summary Metrics)
# ============================================================
# Sample patient medical charges (in USD)
charges = [2400, 3100, 2800, 9500, 12000, 3100, 2900, 4200, 8900, 3500]

mean_val = np.mean(charges)
median_val = np.median(charges)
std_dev = np.std(charges)

print("--- 1. Descriptive Statistics ---")
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Standard Deviation: {std_dev:.2f}\n")


# ============================================================
# 2. Two-Sample T-Test (Comparing 2 Groups)
# Goal: Check if Smokers pay significantly more than Non-Smokers
# H0: Means are equal | H1: Means are different
# ============================================================
smokers = [9500, 12000, 8900, 10500, 11200]
non_smokers = [2400, 3100, 2800, 3100, 2900]

t_stat, p_val_t = stats.ttest_ind(smokers, non_smokers)

print("--- 2. Two-Sample T-Test ---")
print(f"T-statistic: {t_stat:.4f}, P-value: {p_val_t:.6f}")
if p_val_t < 0.05:
    print("Decision: Reject H0 (Smokers have significantly different charges)\n")
else:
    print("Decision: Fail to reject H0\n")


# ============================================================
# 3. Chi-Square Test (Testing Relationship Between 2 Categories)
# Goal: Test if Smoking habit is related to Region
# H0: Variables are independent | H1: Variables are dependent
# ============================================================
# Rows: [Smoker, Non-Smoker]
# Columns: [North, South, East, West]
contingency_table = [
    [15, 20, 18, 12],  # Smokers across 4 regions
    [35, 30, 32, 38]   # Non-smokers across 4 regions
]

chi2_stat, p_val_chi2, dof, _ = stats.chi2_contingency(contingency_table)

print("--- 3. Chi-Square Test of Independence ---")
print(f"Chi2-statistic: {chi2_stat:.4f}, df: {dof}, P-value: {p_val_chi2:.4f}")
if p_val_chi2 < 0.05:
    print("Decision: Reject H0 (Smoking depends on region)\n")
else:
    print("Decision: Fail to reject H0 (Smoking is independent of region)\n")


# ============================================================
# 4. One-Way ANOVA (Comparing 3 or More Groups)
# Goal: Test if charges differ across 3 hospital clinic branches
# H0: All clinic means are equal | H1: At least one clinic is different
# ============================================================
clinic_A = [2800, 3200, 3100, 2900, 3000]
clinic_B = [4500, 4800, 4300, 4700, 4600]
clinic_C = [2900, 3100, 3000, 3200, 2800]

f_stat, p_val_f = stats.f_oneway(clinic_A, clinic_B, clinic_C)

print("--- 4. One-Way ANOVA (F-Test) ---")
print(f"F-statistic: {f_stat:.4f}, P-value: {p_val_f:.6f}")
if p_val_f < 0.05:
    print("Decision: Reject H0 (Significant difference across clinic branches)")
else:
    print("Decision: Fail to reject H0")
