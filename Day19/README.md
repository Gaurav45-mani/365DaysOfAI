📊 Day 19 – Chi-Square Goodness of Fit Test (Census Case Study)

📅 Date

31 August 2026

📚 Topics Covered

1. Chi-Square Goodness of Fit Test
A non-parametric test used to evaluate whether categorical sample observations follow a specific historical, theoretical, or census population distribution.

2. Transforming Population Percentages into Expected Counts
How to compute absolute expected frequencies (E) when baseline population data is given in proportions or percentages, ensuring that the sum of expected counts matches the sample size (Σ E = Σ O = n).

3. Degrees of Freedom (df) & Critical Rejection Thresholds
Understanding right-skewed Chi-Square distribution boundaries:
• Degrees of Freedom: df = k - 1 (where k is the number of categorical bins).
• Setting critical regions using significance level α = 0.05 and locating the cutoff threshold from the Chi-Square lookup table.

🧠 Step-by-Step Theoretical & Numerical Framework

Problem Statement:
A 2010 census categorized city weights as: <50 kg (20%), 50-75 kg (30%), and >75 kg (50%). In 2020, a sample of n = 500 individuals showed: 140 (<50 kg), 160 (50-75 kg), and 200 (>75 kg). At α = 0.05, test whether the weight distribution has changed over 10 years.

Step 1: Formulate Hypotheses
• Null Hypothesis (H0): The sample data meets the expected census distribution (no change in weights).
• Alternative Hypothesis (H1): The sample data does not meet the expected distribution (weights have changed).

Step 2: Calculate Expected Counts (n = 500)
• E(<50 kg)   = 20% of 500 = 100
• E(50-75 kg) = 30% of 500 = 150
• E(>75 kg)   = 50% of 500 = 250
• Sum Check: Σ E = 100 + 150 + 250 = 500 (Matches Σ O = 500)

Step 3: Degrees of Freedom & Decision Rule
• Categories (k) = 3 → df = 3 - 1 = 2
• Significance level: α = 0.05
• Critical Value (χ²_critical from table for df = 2, α = 0.05) = 5.991
• Decision Rule: If χ²_calculated > 5.991, Reject H0.

Step 4: Compute Chi-Square Statistic
• Formula: χ² = Σ [(O - E)² / E]
• χ² = [(140 - 100)² / 100] + [(160 - 150)² / 150] + [(200 - 250)² / 250]
• χ² = [1600 / 100] + [100 / 150] + [2500 / 250]
• χ² = 16 + 0.67 + 10 = 26.67

Step 5: Statistical Conclusion
• Since χ²_calculated (26.67) > χ²_critical (5.991), the result falls into the rejection region.
• Decision: Reject the Null Hypothesis (H0).
• Final Inference: The weight distribution in the city has significantly changed over the 10-year period.

💻 Core Learnings

✔ Converted percentage-based population parameters into absolute expected frequency values.
✔ Formulated categorical Null (H0) and Alternative (H1) hypotheses for demographic data.
✔ Derived degrees of freedom for multi-category bins (df = k - 1).
✔ Mapped the rejection region on a right-skewed Chi-Square distribution curve.
✔ Evaluated the test statistic using manual summation and validated against critical tabular values.

🎯 Key Takeaway

Mastered end-to-end Chi-Square Goodness of Fit testing on demographic census data by converting percentages to absolute expected frequencies, finding critical boundaries, and executing hypothesis rejection decisions.

#365DaysOfAI #Statistics #HypothesisTesting #ChiSquare #GoodnessOfFit #DataScience #MachineLearning #Mathematics
