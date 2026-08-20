📊 Day 11 – Student's T-Distribution & One-Sample T-Test

📅 Date

20 August 2026

📚 Topics Covered

1. One-Sample T-Test
A parametric hypothesis test used to compare the mean of a single sample against a known population benchmark to evaluate whether the observed difference is statistically significant or merely due to random sampling chance.

2. Degrees of Freedom (df) & Critical Values
Degrees of freedom reflect the number of independent values that are free to vary in sample estimation (calculated as df = n - 1). Using df and the significance level (α = 0.05), critical t-values are determined from the T-distribution table to define two-tailed rejection boundaries.

3. Hypothesis Testing Step-by-Step Problem Solving
A complete numerical implementation applying the T-test decision mechanism to evaluate a real-world scenario (testing the impact of a medication on cognitive performance).

🧠 Step-by-Step Theoretical & Numerical Framework

Problem Statement:
In a population, the average IQ is 100. A research team tests a new medication on n = 30 participants to see if it has any positive or negative effect on intelligence. The sample yields a mean x̄ = 140 with a standard deviation of 20 at a 95% Confidence Interval.

Step 1: Set Hypotheses (Two-Tailed Test)
• Null Hypothesis (H0): μ = 100 (Medication has no effect)
• Alternative Hypothesis (H1): μ ≠ 100 (Medication affects intelligence)

Step 2: Define Significance Level & Degrees of Freedom
• Confidence Interval (CI) = 0.95 → Significance Level (α) = 0.05
• Degrees of Freedom (df) = n - 1 = 30 - 1 = 29

Step 3: Establish Decision Rule & Critical Values
• Two-Tailed Split: α / 2 = 0.025 on each tail
• Critical T-value (from T-table for df = 29): ±2.0452
• Decision Rule: If t_calc < -2.0452 or t_calc > +2.0452, Reject H0.

Step 4: Calculate T-Test Statistic
• Formula: t = (x̄ - μ) / (s / √n)
• Standard Error (SE) = 20 / √30 ≈ 3.65
• t = (140 - 100) / 3.65 = 40 / 3.65 = 10.96

Step 5: Compare & Conclude
• Since t_calc (10.96) > t_critical (2.0452), the statistic lies far into the upper rejection region.
• Decision: Reject the Null Hypothesis (H0).
• Final Conclusion: The medication statistically significantly increases intelligence.

💻 Core Learnings

✔ Identified when to choose a One-Sample T-Test over a standard Z-test.
✔ Formulated two-tailed Null and Alternative hypotheses.
✔ Computed degrees of freedom (df = n - 1) for sample data.
✔ Located critical t-values from standard T-distribution tables.
✔ Calculated Standard Error of the mean and overall T-score.
✔ Evaluated statistical significance by comparing calculated t-scores against critical region boundaries.

🎯 Key Takeaway

Mastered the full numerical pipeline of the One-Sample T-Test: establishing hypotheses, finding critical T-boundaries using degrees of freedom, calculating the T-statistic, and executing an objective hypothesis rejection decision.

#365DaysOfAI #Statistics #HypothesisTesting #TTest #DataScience #MachineLearning #Mathematics
