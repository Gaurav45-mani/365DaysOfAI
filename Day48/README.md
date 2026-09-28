📊 Day 48 – Dimensionality Reduction: Principal Component Analysis (PCA)

📅 Date

28 September 2026

📚 Topics Covered

1. The Dimensionality Reduction Dilemma
• When working with multiple correlated features (e.g., `No. of Rooms` and `House Size`), simply discarding one feature discards valuable variance and information.
• Dropping an axis leads to high projection loss and poor model performance.

2. Principal Component Analysis (PCA)
• An unsupervised machine learning algorithm designed to reduce feature dimensions (e.g., 2D → 1D) while preserving the maximum variance of the original data.
• Finds a new coordinate system:
  - PC1 (First Principal Component): The axis capturing the maximum variance across data points.
  - PC2: Orthogonal (perpendicular) to PC1, capturing the next highest remaining variance.

3. Mathematical Workflow
• Standardize data to ensure unit variance.
• Compute the Covariance Matrix of features.
• Calculate Eigenvalues and Eigenvectors to extract principal directions.
• Project original data points orthogonally onto the new principal axes.

🧠 Decision Framework

| Approach | Dimensionality | Information Retained | Trade-off |
| :--- | :--- | :--- | :--- |
| **Raw Data** | 2D (`Rooms`, `Size`) | 100% | High dimensionality, multicollinearity |
| **Drop 1 Feature** | 1D (`Rooms`) | Very Low | Severe information loss |
| **PCA (PC1)** | 1D (New Axis) | Maximum possible | Preserves variance without collinearity |
