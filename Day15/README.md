📊 Day 13 – Confidence Intervals & Margin of Error

📅 Date

22 August 2026

📚 Topics Covered

1. Confidence Intervals (CI)
A Confidence Interval is an inferential range constructed around a sample point estimate to approximate the true, unknown population parameter with a chosen level of confidence (e.g., 95%). Instead of relying on a single point value, it accounts for sampling uncertainty.

2. Margin of Error (MoE) & Critical Values (Z_α/2)
The Margin of Error defines the radius of uncertainty around the point estimate. It is calculated by multiplying the critical standard score (Z_α/2) by the standard error of the mean:
• Formula: Margin of Error = Z_α/2 * (σ / √n)
• Confidence Level vs Significance: For a 95% Confidence Interval, the error margin is α = 0.05.
• Two-Tailed Split: The remaining 5% is split evenly across both tails (α/2 = 0.025), giving a critical Z-value of ±1.96.

3. Step-by-Step Problem Solving (CAT Exam Score Analysis)
A practical calculation demonstrating how to construct lower and upper confidence limits from sample statistics.

🧠 Step-by-Step Mathematical & Numerical Framework

General Formula:
Confidence Interval = x̄ ± Z_α/2 * (σ / √n)

Problem Statement:
On the verbal section of the CAT exam, the population standard deviation is known to be σ = 100. A random sample of n = 25 test takers has a mean score x̄ = 520. Construct a 95% Confidence Interval for the population mean score.

Step 1: Identify Given Data
• Sample Mean (x̄) = 520
• Population Standard Deviation (σ) = 100
• Sample Size (n) = 25
• Confidence Interval (CI) = 95% (0.95) → α = 0.05

Step 2: Determine Critical Z-Value
• Tail probability: α / 2 = 0.05 / 2 = 0.025
• Z_0.025 (from standard normal Z-table) = 1.96

Step 3: Calculate Standard Error & Margin of Error
• Standard Error (SE) = σ / √n = 100 / √25 = 100 / 5 = 20
• Margin of Error (MoE) = 1.96 * 20 = 39.2

Step 4: Compute Upper & Lower Confidence Limits
• Lower Limit = 520 - (1.96 * 20) = 520 - 39.2 = 480.8
• Upper Limit = 520 + (1.96 * 20) = 520 + 39.2 = 559.2

Step 5: Statistical Conclusion
• We are 95% confident that the true population mean CAT verbal score lies between 480.8 and 559.2.

💻 Core Learnings

✔ Defined the mathematical link between point estimation, standard error, and confidence intervals.
✔ Evaluated two-tailed significance distribution splits (α/2 = 0.025 for 95% CI).
✔ Looked up and applied the standard critical Z-value (Z = 1.96).
✔ Computed the Margin of Error using population standard deviation and sample size.
✔ Calculated and interpreted the upper and lower boundaries for population parameters.

🎯 Key Takeaway

Mastered the full analytical workflow of constructing Confidence Intervals and Margin of Error using Z-scores to provide statistically robust bounds for unknown population parameters.

#365DaysOfAI #Statistics #ConfidenceInterval #MarginOfError #DataScience #MachineLearning #Mathematics
