📊 Day 36 – Feature Engineering: Feature Scaling & Standardization (Z-Score)

16 September 2026

📚 Topics Covered

1. Feature Engineering Foundations
• Feature Extraction: Transforming raw attributes into representative summary features using statistical methods (Mean, Median, Standard Deviation, Covariance, Correlation, and Regression Analysis).
• Feature Selection: Identifying and retaining the most predictive features while dropping redundant or noisy attributes.

2. Why Feature Scaling is Essential
Machine learning models calculating geometric distances (k-NN, K-Means, SVM) or updating parameters using gradient descent are distorted when features operate on mismatched numeric ranges (e.g., Salary in thousands vs. Age in tens). Scaling brings all features to a common scale without distorting relative differences.

3. Scaling Techniques
• Standardization (Z-Score Scaling): Shifts the mean to 0 and scales the standard deviation to 1 (μ = 0, σ = 1).
• Min-Max Scaling: Compresses values into a fixed boundary, typically [0, 1].
• Unit Vector Scaling: Scales feature vectors to unit norm (magnitude = 1).

4. Mathematics of Standardization
• Z-Score Formula:
  Z = (x - μ) / σ
  where x is the feature value, μ is the feature mean, and σ is the standard deviation.
• Unlike min-max scaling, standardization is unbounded and does not compress outliers into an artificial interval.

🧠 Scaling Method Comparison

| Scaling Technique | Mathematical Formulation | Output Range | Outlier Sensitivity |
| :--- | :--- | :--- | :--- |
| **Standardization (Z-Score)** | (x - μ) / σ | Unbounded (μ=0, σ=1) | Preserves outlier distances |
| **Min-Max Normalization** | (x - min) / (max - min) | [0, 1] | Highly compressed by outliers |
| **Unit Vector Scaling** | x / ||x|| | Length = 1 | Sensitive to directional extremes |

