📊 Day 63 – Multi-Label Splitting & High-Cardinality Feature Engineering: TMDB Movie Dataset

📅 Date
13 October 2026

📚 Topics Covered

1. Multi-Label String Binarization
• Transformed pipe-separated multi-label categories (`'Action|Adventure|Sci-Fi'`) into binary indicator matrices using `.str.get_dummies(sep='|')`.

2. Quantitative Category Count Feature Extraction
• Synthesized `genre_count` to capture target variance linked to category complexity and multi-genre tagging.

3. Financial Metric Engineering
• Synthesized financial performance metrics: `profit` (Revenue - Budget) and `roi` (Return on Investment ratio), utilizing `np.where` for zero-division guardrails.

4. Multi-Label Group Aggregation
• Merged engineered indicator features with primary target metrics to evaluate profitability across individual genres.

🧠 Feature Engineering Execution Matrix

| Raw Feature | Format Issue | Transformation Applied | Output Type |
| :--- | :--- | :--- | :--- |
| **`genres`** | Delimited String (`'Action\|Sci-Fi'`) | `.str.get_dummies(sep='\|')` | Binary Feature Matrix |
| **`genres`** | Text Tags | `.apply(lambda x: len(x.split('\|')))` | Discrete Integer (`genre_count`) |
| **`revenue` / `budget`**| Continuous Financials | `revenue - budget` & `(revenue - budget)/budget` | Continuous Numeric (`profit`, `roi`) |
