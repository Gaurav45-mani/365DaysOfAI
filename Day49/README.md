📊 Day 49 – Feature Engineering: Categorical Data Encoding & One-Hot Encoding (OHE)

📅 Date

29 September 2026

📚 Topics Covered

1. Categorical Data Encoding Fundamentals
Machine learning algorithms require numerical input arrays to calculate gradients and optimization loss. Categorical variables must be converted into numerical features without introducing unintended numerical hierarchies.

2. Encoding Paradigms
• Nominal Encoding (One-Hot Encoding): Applied to categories without intrinsic ordering (e.g., colors, cities, blood types).
• Ordinal & Label Encoding: Applied when categories have an inherent rank or progression (e.g., Cold < Warm < Hot, B.E < Master < PhD).
• Target Guided Ordinal Encoding: Orders categories based on the expected value or mean of the target variable.

3. Mechanics of One-Hot Encoding (OHE)
• Creates a dedicated binary indicator column for every distinct level in a nominal feature.
• Assigns 1 if the record matches that category, and 0 otherwise.

4. Trade-offs & Limitations of OHE
• Sparse Matrix: Results in matrices populated mostly with zeros, leading to memory inefficiencies.
• High Cardinality Hazard: High-cardinality features (e.g., 1,000 distinct ZIP codes) explode feature space dimensionality, which increases risk of overfitting.
• Best practice: Reserve OHE for low-cardinality nominal variables.

🧠 Encoding Selection Matrix

| Categorical Type | Intrinsic Hierarchy? | Preferred Method | Example |
| :--- | :--- | :--- | :--- |
| **Nominal (Low Cardinality)** | No | One-Hot Encoding (OHE) | City: [Delhi, Lucknow, Noida] |
| **Nominal (High Cardinality)** | No | Frequency / Target Encoding | Zip Codes, User IDs |
| **Ordinal** | Yes | Ordinal / Label Encoding | Education: [B.E, Master, PhD] |
