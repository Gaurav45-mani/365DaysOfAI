📊 Day 31 – Handling Imbalanced Datasets: SMOTE (Synthetic Minority Oversampling Technique)

11 September 2026

📚 Topics Covered

1. Limitations of Random Upsampling
Standard random oversampling duplicates existing minority records with replacement. While it balances class counts, it causes the model to memorize identical data points repeatedly, leading to overfitting and poor decision boundary generalization.

2. SMOTE (Synthetic Minority Oversampling Technique)
SMOTE solves the duplication problem by creating entirely new, plausible synthetic instances rather than copying existing ones.
• Uses the k-Nearest Neighbors (k-NN) algorithm to identify neighboring instances within the minority class.
• Applies Linear Interpolation along the line segment connecting adjacent minority samples to generate realistic synthetic data points.

3. End-to-End Implementation with Imbalanced-Learn (`imblearn`)
• Generated a synthetic imbalanced dataset (90:10 ratio) using `sklearn.datasets.make_classification`.
• Visualized the skewed feature space using Matplotlib scatter plots.
• Applied `imblearn.over_sampling.SMOTE` with `fit_resample` to expand the minority class from 106 to 894 instances, balancing the dataset to 1,788 samples.

🧠 Conceptual Comparison Matrix

| Metric / Technique | Random Upsampling | SMOTE (Synthetic Oversampling) |
| :--- | :--- | :--- |
| **Data Generation Mechanism** | Exact row duplication (`replace=True`) | Feature vector interpolation via k-NN |
| **Variance Introduced** | Zero new variance | High, realistic synthetic variance |
| **Overfitting Risk** | High (memorizes duplicate rows) | Low (generalizes feature space) |
| **Compute Overhead** | Negligible | Moderate (calculates nearest neighbors) |
