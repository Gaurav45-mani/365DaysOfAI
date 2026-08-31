📊 Day 20 – Analysis of Variance (ANOVA) & F-Distribution

📅 Date

01 September 2026

📚 Topics Covered

1. Introduction to ANOVA
Analysis of Variance (ANOVA) is a hypothesis-testing technique used to compare the means of three or more groups simultaneously. It replaces multiple pairwise t-tests to avoid accumulating Type I error (false positives).
• Factor: The independent categorical variable being studied (e.g., Medication dosage, Payment method).
• Levels: The individual categories or subgroups within that factor (e.g., 5mg, 10mg, 20mg).

2. Core Assumptions of ANOVA
For ANOVA results to be valid, four statistical assumptions must be met:
• Normality: The sampling distribution of means is normally distributed.
• Absence of Outliers: Extreme anomalous data points must be identified and treated.
• Homogeneity of Variance (Homoscedasticity): Equal population variance across all groups (σ₁² = σ₂² = σ₃²).
• Independence & Randomness: Observations within and across groups are collected independently and randomly.

3. Types of ANOVA
• One-Way ANOVA: Evaluates one factor with 2 or more independent groups (e.g., comparing headache reduction across 3 separate dosage groups).
• Repeated Measures ANOVA: Evaluates one factor where measurements are taken on the same subjects over time (dependent groups, e.g., Day 1 vs. Day 2 vs. Day 3 running scores).
• Factorial ANOVA: Evaluates the individual and interaction effects of two or more independent factors (e.g., Gender × Running Day).

4. Hypothesis Testing & F-Distribution
• Null Hypothesis (H0): μ₁ = μ₂ = μ₃ = ... = μk (All group means are equal).
• Alternative Hypothesis (H1): At least one group mean is significantly different.
• F-Test Statistic:
  F = (Variance Between Groups) / (Variance Within Groups)
  F = MS_between / MS_within

🧠 Step-by-Step Theoretical Framework

• Why Variance Measures Mean Differences:
  - Variance Between Groups measures differences caused by the actual experimental treatment or factor.
  - Variance Within Groups measures random natural noise or individual variation within the same group.
  - A large F-ratio (F >> 1) indicates that between-group differences far outweigh random within-group noise, leading to the rejection of H0.

• Sample Scenario (One-Way):
  - Factor: Medication Dosage (Levels: 10mg, 20mg, 30mg)
  - Target: Headache reduction score (1–10)
  - H0: μ_10mg = μ_20mg = μ_30mg
  - H1: At least one dosage yields a significantly different average headache score.

💻 Core Learnings

✔ Identified the structural need for ANOVA over repeated pairwise T-tests.
✔ Differentiated clearly between Factors (variables) and Levels (subgroups).
✔ Verified the four mandatory ANOVA assumptions before conducting tests.
✔ Distinguished between One-Way, Repeated Measures, and Factorial ANOVA setups.
✔ Formulated standard multi-group Null (H0) and Alternative (H1) hypotheses.
✔ Understood the derivation of the F-statistic as the ratio of between-group variance to within-group variance.

🎯 Key Takeaway

Mastered the conceptual foundation and classification of ANOVA (One-Way, Repeated Measures, and Factorial), learning how the F-distribution compares variance between groups against variance within groups to detect significant differences across multiple populations.

#365DaysOfAI #Statistics #ANOVA #FTest #HypothesisTesting #DataScience #MachineLearning #Mathematics
