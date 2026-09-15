📊 Day 35 – Outlier Detection Using 5-Number Summary & IQR Fencing

📅 Date

16 September 2026

📚 Topics Covered

1. Understanding Outliers in Data Preprocessing
An outlier is an observation that lies an abnormal distance from other values in a random sample. If unaddressed, outliers skew distribution moments (mean, variance) and degrade gradient-based machine learning models.

2. The 5-Number Summary
A descriptive statistical method to capture the shape and spread of continuous distributions:
• Minimum: 0th percentile
• Q1 (First Quartile): 25th percentile
• Median (Q2): 50th percentile
• Q3 (Third Quartile): 75th percentile
• Maximum: 100th percentile

3. Interquartile Range (IQR) & Tukey’s Fences
• Formula: IQR = Q3 - Q1 (represents the central 50% spread).
• Lower Fence = Q1 - 1.5 * IQR
• Upper Fence = Q3 + 1.5 * IQR
• Decision Rule: Any data point x < Lower Fence or x > Upper Fence is mathematically categorized as an outlier.

🧠 Detection Breakdown

| Metric | Calculation | Result on Dataset |
| :--- | :--- | :--- |
| **Q1 (25th Percentile)** | `np.quantile(..., 0.25)` | 54.0 |
| **Q3 (75th Percentile)** | `np.quantile(..., 0.75)` | 89.5 |
| **IQR** | Q3 - Q1 | 35.5 |
| **Lower Fence** | Q1 - 1.5 * IQR | 0.75 |
| **Upper Fence** | Q3 + 1.5 * IQR | 142.75 |
| **Identified Outliers** | Values > 142.75 | [1000, 1100] |
