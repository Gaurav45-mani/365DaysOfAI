📊 Day 50 – Feature Engineering: Label Encoding & Ordinal Encoding

📅 Date

30 September 2026

📚 Topics Covered

1. Categorical Ranking Problem
When categories contain meaningful hierarchy or progression, standard One-Hot Encoding increases dimensionality unnecessarily and ignores order. Instead, rank-aware integer mapping is used to preserve relative magnitude.

2. Label Encoding (Target / Alphabetic Mapping)
• Maps unique labels to integers (0 to n_classes - 1) based on alphabetical order.
• Primarily meant for 1D dependent target vectors (y).
• Using it on independent features (X) with nominal data introduces artificial mathematical order (e.g., Red = 2 > Blue = 0).

3. Ordinal Encoding (Feature Hierarchy Mapping)
• Designed specifically for multi-dimensional feature matrices (X).
• Allows explicit assignment of custom category hierarchies via the `categories` parameter.
• Ensures that real-world progressions (e.g., Small < Medium < Large) map directly to proportional numerical intervals (0 < 1 < 2).

🧠 Encoding Comparison Matrix

| Method | Target Variable Type | Accepts Custom Order? | Expected Input Shape | Typical Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **LabelEncoder** | Nominal / Target Labels | No (Alphabetical) | 1D Array / Series (`df['col']`) | Target variable `y` in classification |
| **OrdinalEncoder** | Ordinal Features | Yes (`categories=[...]`) | 2D Matrix (`df[['col']]`) | Independent features `X` with rank |
