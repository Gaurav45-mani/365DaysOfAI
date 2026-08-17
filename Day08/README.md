📊 Day 08 – Uniform Distribution, Standard Normal Distribution & Z-Scores

📅 Date

17 August 2026

📚 Topics Covered

1. Continuous Uniform Distribution
A symmetric, rectangular probability distribution where every outcome within a defined continuous interval [a, b] has an equal likelihood of occurring. It is defined by constant probability density between its boundaries, zero probability outside them, and straightforward formulas for its mean, median, and variance.
2. Standard Normal Distribution
A specific form of the Gaussian (bell-shaped) normal distribution that has been standardized to have a mean (μ) of 0 and a standard deviation (σ) of 1. It serves as the universal reference benchmark for measuring how far individual data points deviate from the population average.
3. Z-Score & Area Under the Curve
A metric that indicates exactly how many standard deviations an observation lies above or below the mean. Converting raw values to Z-scores enables the use of standard Z-tables to determine cumulative percentiles, tail probabilities, and exact proportions of data falling above, below, or between specific intervals.

🧠 Theory & Core Mathematical Formulas

Continuous Uniform Distribution:

* PDF: f(x) = 1 / (b - a) for x ∈ [a, b], otherwise 0
* CDF: F(x) = (x - a) / (b - a) for x ∈ [a, b]
* Mean = (a + b) / 2
* Median = (a + b) / 2
* Variance = (b - a)² / 12

Standard Normal Distribution & Z-Score:

* Z-Score Formula: Z = (x - μ) / σ
* Standardization transformation: Converts any N(μ, σ) distribution into standard N(0, 1) space.
* Solved practical distribution problem: For μ = 4, σ = 1, evaluated P(X > 4.5) by computing Z = (4.5 - 4) / 1 = 0.5. Found cumulative area up to 4.5 as 69.15% (0.69146), leaving the upper-tail probability as 1 - 0.69146 = 30.85% (0.30854).

💻 Practical Implementation & Problem Solving

✔ Evaluated and derived the mathematical properties of Continuous Uniform Distributions.
✔ Transformed raw sample distributions into standard normal distributions with μ = 0 and σ = 1.
✔ Computed precise Z-scores for individual data observations across a distribution.
✔ Solved continuous probability problems using standard normal table lookups.
✔ Analyzed and interpreted total area under the curve to distinguish cumulative density from upper-tail percentages.

🎯 Key Takeaway

Gained a strong conceptual and mathematical foundation in modeling equal-probability bounded data using Uniform Distributions, alongside mastering Z-score standardization to compute precise percentiles and tail probabilities on normal curves.

#365DaysOfAI #Statistics #Probability #DataScience #MachineLearning #Python
