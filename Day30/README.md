📊 Day 30 – Handling Imbalanced Datasets: Upsampling & Downsampling

📅 Date

10 September 2026

📚 Topics Covered

1. The Imbalanced Dataset Problem
Occurs in classification tasks when target classes are heavily skewed (e.g., 900:100 or 9:1 ratio). Common in real-world scenarios like fraud detection, disease diagnosis, and rare event prediction.

2. The Accuracy Paradox ("Dumb Model")
A baseline model trained on a 90:10 imbalanced dataset can predict the majority class 100% of the time and achieve 90% overall accuracy, despite having 0% recall on the minority class.

3. Resampling Strategies
• Upsampling (Oversampling): Increasing minority class instances by sampling with replacement until the size matches the majority class.
• Downsampling (Undersampling): Reducing majority class instances randomly to equal the minority count.

🧠 Resampling Comparison Matrix

| Strategy | Action | Target Ratio | Trade-off |
| :--- | :--- | :--- | :--- |
| **Raw Data** | No change | 900 : 100 | Susceptible to accuracy paradox |
| **Upsampling** | Duplicate minority rows (`replace=True`) | 900 : 900 | Increases dataset size; may cause overfitting |
| **Downsampling** | Prune majority rows (`replace=False`) | 100 : 100 | Fast training; discards potentially useful data |

💻 Core Learnings

✔ Simulated synthetic imbalanced feature sets using `np.random.normal`.
✔ Partitioned DataFrames using conditional masking (`df['target'] == 1`).
✔ Implemented upsampling using Scikit-Learn's `resample(..., replace=True)`.
✔ Implemented downsampling using Scikit-Learn's `resample(..., replace=False)`.
✔ Reconstructed balanced training sets using `pd.concat()`.


#365DaysOfAI #MachineLearning #DataScience #DataPreprocessing #ImbalancedData #Python #ScikitLearn
