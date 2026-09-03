📊 Day 23 – End-to-End Applied Statistical Analysis Capstone Project

📅 Date

04 September 2026

📚 Project Overview

A comprehensive, production-grade statistical analysis capstone integrating all 22 days of foundational, inferential, and computational statistics. This project demonstrates how to frame testable empirical questions, clean and analyze distributions, and validate real-world hypotheses using Python (NumPy, Pandas, SciPy, Matplotlib).

🎯 Applied Statistical Methodologies

1. Exploratory Data Analysis & Descriptive Statistics
• Quantified central tendencies (Mean, Median, Mode) and spread metrics (Variance, Standard Deviation, IQR).
• Inspected distribution shapes and verified continuous variables for skewness and anomalies.

2. Two-Sample Independent T-Test (Group Mean Comparison)
• Research Question: Does smoking status significantly impact healthcare insurance charges?
• Hypotheses:
  - H0: μ_smoker = μ_nonsmoker
  - H1: μ_smoker ≠ μ_nonsmoker
• Test Applied: Welch’s Two-Sample T-test to evaluate significance without assuming equal variance.

3. Chi-Square Test of Independence (Categorical Association)
• Research Question: Is smoking prevalence independent of geographic location?
• Hypotheses:
  - H0: Smoker status and geographic region are independent.
  - H1: Smoker status and geographic region are dependent.
• Test Applied: Computed contingency matrix, degrees of freedom, and Chi-Square statistic.

4. One-Way ANOVA & F-Distribution (Multi-Group Comparison)
• Research Question: Do mean healthcare charges vary across multiple geographic regions?
• Hypotheses:
  - H0: μ_northeast = μ_northwest = μ_southeast = μ_southwest
  - H1: At least one regional mean charges differs significantly.
• Test Applied: F-test partitioning total variance into between-group and within-group variance.

🧠 Statistical Pipeline & Results Summary

• Descriptive Phase: Validated parametric requirements (normality of continuous features and variance checks).
• T-Test Outcome: Calculated extreme t-statistic with p < 0.001 (P < 0.05), rejecting H0 and confirming smokers incur significantly higher costs.
• Chi-Square Outcome: Found p > 0.05, failing to reject H0 and confirming regional distribution does not depend on smoking habit.
• ANOVA Outcome: Evaluated the F-ratio across all 4 regional subsets to test multi-group variance thresholds.

💻 Project Technologies

✔ Python • NumPy • Pandas • SciPy Stats • Matplotlib
✔ Welch’s Two-Sample T-Test (`stats.ttest_ind`)
✔ Chi-Square Test of Independence (`stats.chi2_contingency`)
✔ One-Way ANOVA (`stats.f_oneway`)

🎯 Key Takeaway

Successfully synthesized 23 days of foundational probability, inferential tests (Z, T, Chi-Square, ANOVA), and hypothesis-testing frameworks into a single real-world data science capstone project.

#365DaysOfAI #Statistics #HypothesisTesting #ANOVA #DataScience #MachineLearning #Python
