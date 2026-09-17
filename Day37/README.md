📊 Day 37 – Feature Scaling: Normalization (Min-Max Scaler) vs. Standardization

17 September 2026

📚 Topics Covered

1. Normalization (Min-Max Scaling)
A feature scaling technique that rescales continuous numerical data into a fixed interval, typically [0, 1]. It maps the minimum value of a feature to 0 and the maximum to 1.
• Mathematical Formulation:
  x_scaled = (x - x_min) / (x_max - x_min)

2. Connecting Normalization to Standardization
• Standardization (Z-Score) centers the data at μ = 0 with σ = 1 without enforcing boundaries, preserving relative outlier deviations.
• Normalization compresses every observation into [0, 1]. While beneficial for models expecting bounded inputs, extreme minimums or maximums compress the variance of the remaining observations.

3. Decision Matrix: Standardization vs. Normalization

| Metric | Normalization (Min-Max) | Standardization (Z-Score) |
| :--- | :--- | :--- |
| **Output Range** | Strictly bounded [0, 1] | Unbounded (Mean = 0, Std = 1) |
| **Formula** | (x - x_min) / (x_max - x_min) | (x - μ) / σ |
| **Outlier Handling** | Highly sensitive (compresses in-range data) | Robust (preserves distance signals) |
| **Assumed Distribution** | Non-Gaussian / Unknown | Gaussian / Normal distributions |
| **Best Algorithmic Fit** | Neural Networks, K-NN, Image Processing | PCA, Linear Regression, Logistic Regression, SVM |
