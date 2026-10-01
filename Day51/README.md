📊 Day 51 – Feature Engineering: Target Guided Ordinal Encoding

📅 Date

01 October 2026

📚 Topics Covered

1. What is Target Guided Ordinal Encoding?
An encoding technique where nominal or high-cardinality categorical variables are transformed based on their direct statistical relationship (mean, median) with the dependent target variable.

2. Solving the High-Cardinality Challenge
• One-Hot Encoding on high-cardinality features (e.g., 500 cities) explodes feature space dimensionality into a sparse matrix, leading to overfitting.
• Target Guided Encoding condenses categorical levels into a single informative continuous column without creating new dimensions.

3. Mathematical & Logic Pipeline
• Group records by categorical feature levels (`df.groupby('City')`).
• Aggregate target statistics across groups (`['price'].mean()`).
• Map target mean values back to individual categories (`df['City'].map(mean_price)`).

🧠 Encoding Decision Framework

| Method | Target Dependency | Cardinality | Output Shape | Best Suited For |
| :--- | :--- | :--- | :--- | :--- |
| **One-Hot Encoding** | Independent | Low | N Binary Columns | Nominal data with few unique levels |
| **Ordinal Encoding** | Independent | Low / Medium | Single Integer Column | Data with natural rank (S, M, L, XL) |
| **Target Guided Encoding** | Dependent on Target | High | Single Float Column | High-cardinality nominal features (Cities, Zip Codes) |
