📊 Day 21 – One-Way ANOVA Calculation & F-Distribution

📅 Date

02 September 2026

📚 Topics Covered

1. One-Way ANOVA End-to-End Problem Solving
A complete manual calculation of a One-Way ANOVA to evaluate differences across three independent treatment groups (15mg, 30mg, and 45mg medication dosages on headache relief ratings).

2. Partitioning Variance (Sum of Squares & Mean Squares)
• Sum of Squares Between (SS_between): Measures variation between treatment groups due to the experimental factor.
• Sum of Squares Within (SS_within): Measures natural random error and individual variance within each group.
• Mean Squares (MS): Calculated by dividing Sum of Squares by their corresponding degrees of freedom (MS = SS / df).

3. F-Test Statistic & Decision Making
Calculating the F-ratio (F = MS_between / MS_within) and comparing it against the right-skewed F-distribution critical threshold to determine whether group differences are statistically significant.

4. Mathematical Foundations of the F-Distribution
The F-distribution arises as the ratio of two scaled, independent Chi-Square random variables:
• Formula: X = (U₁ / d₁) / (U₂ / d₂) where U₁ ~ χ²(d₁) and U₂ ~ χ²(d₂)
• Parameters: Numerator degrees of freedom (d₁) and denominator degrees of freedom (d₂).
• Characterized by non-negative support and right-skewed density.

🧠 Step-by-Step Theoretical & Numerical Framework

Problem Statement:
Doctors test 3 conditions of a headache medication: 15mg, 30mg, and 45mg across n = 7 patients each (Total N = 21). Headache ratings (1-10) are recorded. Test for differences at α = 0.05.

Group Sums:
• 15mg: [9, 8, 7, 8, 8, 9, 8] → Sum = 57
• 30mg: [7, 6, 6, 7, 8, 7, 6] → Sum = 47
• 45mg: [4, 3, 2, 3, 4, 3, 2] → Sum = 21
• Grand Total (T) = 125, Total Sample (N) = 21

Step 1: Set Hypotheses
• Null Hypothesis (H0): μ_15 = μ_30 = μ_45 (No difference between dosage levels)
• Alternative Hypothesis (H1): At least one group mean is significantly different

Step 2: Calculate Degrees of Freedom
• df_between = a - 1 = 3 - 1 = 2
• df_within = N - a = 21 - 3 = 18
• df_total = N - 1 = 21 - 1 = 20

Step 3: ANOVA Table Breakdown
• SS_between = [(57² + 47² + 21²) / 7] - [125² / 21] = 842.71 - 744.05 = 98.67
• MS_between = 98.67 / 2 = 49.34
• SS_within = Σy² - [(57² + 47² + 21²) / 7] = 853 - 842.71 = 10.29
• MS_within = 10.29 / 18 = 0.57
• F_statistic = MS_between / MS_within = 49.34 / 0.57 = 86.56

Step 4: Decision & Statistical Inference
• Critical Value from F-Table: F_critical(2, 18, α=0.05) = 3.5546
• Since F_calculated (86.56) > F_critical (3.5546), the test statistic falls deep in the rejection region.
• Decision: Reject the Null Hypothesis (H0).
• Conclusion: Medication dosage significantly affects headache relief ratings.

💻 Core Learnings

✔ Partitioned total variation into between-group and within-group sum of squares.
✔ Calculated degrees of freedom for numerator (between) and denominator (within) terms.
✔ Computed Mean Squares (MSB, MSW) and derived the empirical F-ratio.
✔ Located critical values on the right-tailed F-distribution table.
✔ Understood the mathematical relationship between the F-distribution and independent Chi-Square variables.

🎯 Key Takeaway

Mastered the end-to-end numerical computation of One-Way ANOVA by constructing a full ANOVA table, calculating the F-statistic, and using the F-distribution to prove statistically significant differences across treatment groups.

#365DaysOfAI #Statistics #ANOVA #FDistribution #HypothesisTesting #DataScience #MachineLearning #Mathematics
