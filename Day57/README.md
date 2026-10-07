📊 Day 57 – Exploratory Data Analysis (EDA): Student Performance Dataset

📅 Date

07 October 2026

📚 Topics Covered

1. Data Auditing & Programmatic Feature Segregation
• Checked dataset health: shape inspection, missing value auditing (`isnull().sum()`), and duplicate removal (`drop_duplicates()`).
• Programmatically segregated columns into numerical features (`dtype != 'O'`) and categorical features (`dtype == 'O'`).

2. Feature Engineering & Score Aggregation
• Synthesized overall academic performance metrics:
  - Total Score = Math Score + Reading Score + Writing Score
  - Average Score = Total Score / 3

3. Multi-Panel Subplot Visualizations & Demographic Categorization
• Used `plt.subplots(1, 2)` and `plt.subplots(1, 3)` to build comparative side-by-side distribution plots.
• Leveraged Seaborn's `hue` parameter to overlay sub-category distributions (e.g., `hue='gender'`, `hue='lunch'`).
• Key Finding: Students receiving standard lunch consistently outperform students receiving free/reduced lunch across both male and female sub-demographics.

4. Score Correlation Matrix
• Calculated score correlations using `sns.heatmap(annot=True)`, revealing strong linear relationships between reading and writing performance.

🧠 Student Dataset EDA Summary Matrix

| Pipeline Phase | Primary Function / Tool | Analytical Objective |
| :--- | :--- | :--- |
| **Audit & Clean** | `df.isnull().sum()`, `df.drop_duplicates()` | Remove nulls and redundant duplicate rows |
| **Segregation** | List comprehension via `df[col].dtype` | Separate numeric variables from object categories |
| **Feature Synthesis** | Math + Reading + Writing scores | Create `total_score` and `average` metrics |
| **Comparative Plots**| `sns.histplot(hue='lunch')` | Analyze impact of lunch type on exam performance |
| **Correlation** | `sns.heatmap(df.corr(), annot=True)` | Measure inter-score linear relationships |
