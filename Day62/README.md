📊 Day 62 – Advanced Imputation & Categorical Encoding: Titanic Dataset

📅 Date
12 October 2026

📚 Topics Covered

1. Text Feature Extraction via Regular Expressions
• Extracted structural title honorifics (`Mr.`, `Mrs.`, `Master.`) from passenger names using `.str.extract()` to uncover demographic subgroups.

2. Groupby Conditional Median Imputation
• Advanced beyond global mean/median filling by imputing missing `Age` values conditionally based on combined `Pclass` and `Title` groupings.

3. K-Nearest Neighbors (KNN) Imputation
• Implemented Scikit-Learn's `KNNImputer(n_neighbors=5)` to estimate missing numerical values using multi-feature distance proximity.

4. Target-Guided Ordinal Encoding
• Transformed high-cardinality categorical variables into continuous features weighted directly by their target variable survival mean rates (`df.groupby('Embarked')['Survived'].mean()`).

🧠 Execution Matrix

| Strategy | Applied Column | Function / Model | Analytical Objective |
| :--- | :--- | :--- | :--- |
| **Regex Extraction** | `Name` | `.str.extract(' ([A-Za-z]+)\.')` | Isolate demographic title signals |
| **Conditional Imputation** | `Age` | `df.groupby(['Pclass', 'Title']).transform()` | Impute missing values using demographic medians |
| **KNN Distance Imputation**| Numeric features | `KNNImputer(n_neighbors=5)` | Predict missing values using nearest neighbors |
| **Target Encoding** | `Embarked` | `.map(target_mean)` | Preserve category-target statistical correlation |

