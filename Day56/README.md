📊 Day 56 – Practical EDA & Preprocessing Pipeline: Red Wine Quality Dataset

📅 Date

06 October 2026

📚 Topics Covered

1. Real-World Data Ingestion & Auditing
• Loaded UCI Red Wine Quality dataset with semicolon delimiters.
• Inspected null presence, feature types, and statistical moments using `.info()` and `.describe()`.

2. Univariate & Bivariate Visual Analysis
• Histograms & Count Plots: Audited skewness across chemical measurements and checked quality rating distributions.
• Correlation Heatmaps & Boxplots: Evaluated feature correlations and analyzed target variance (e.g., higher alcohol content correlating with higher wine quality ratings).

3. Outlier Removal via IQR Fencing
• Identified multivariate extreme anomalies across $Q_1 - 1.5 \times IQR$ and $Q_3 + 1.5 \times IQR$ bounds.
• Programmatically filtered out outlier records to stabilize training distributions.

4. Feature Transformation & Selection
• Log Transformation: Applied `np.log1p()` to right-skewed features (`free sulfur dioxide`) to approximate normality.
• Feature Scaling: Standardized independent variables using `StandardScaler()`.
• Statistical Feature Selection: Applied ANOVA F-tests via `SelectKBest(score_func=f_classif, k=5)` to isolate the top 5 predictive variables.

🧠 End-to-End EDA Execution Steps

| Phase | Method / Function | Purpose |
| :--- | :--- | :--- |
| **Inspection** | `df.info()`, `df.describe()` | Inspect data types, nulls, and central tendencies |
| **Visualization** | `sns.heatmap()`, `sns.boxplot()` | Uncover correlations and target relationships |
| **Outlier Removal** | IQR Fencing Matrix | Filter extreme noise across continuous variables |
| **Transformation** | `np.log1p()`, `StandardScaler()` | Normalize skewness and standardize feature scales |
| **Feature Selection**| `SelectKBest(f_classif)` | Extract top $K$ features driving target variance |
