📊 Day 38 – Feature Scaling: Unit Vector Scaling (L2 Normalization)

18 September 2026

📚 Topics Covered

1. Unit Vector Feature Scaling (Vector Normalization)
A sample-wise feature transformation technique that scales each observation vector to have a Euclidean norm (magnitude) of exactly 1.
• Unlike column-wise scaling (Standardization or Min-Max), Unit Vector Scaling operates row-wise across all features of an individual data point.
• Retains the directional trajectory of feature interactions while eliminating scale bias caused by large absolute vector lengths.

2. Mathematical Formulation (L2 Norm)
• Euclidean Magnitude of Vector x:
  ||x|| = √(x₁² + x₂² + ... + xₙ²)
• Unit Vector Transformation:
  û = x / ||x||
• Example:
  For vector (3, 4):
  ||x|| = √(3² + 4²) = √25 = 5
  û = (3/5, 4/5) = (0.6, 0.8)
  ||û|| = √(0.6² + 0.8²) = 1.0

3. Practical Applications
• Natural Language Processing (NLP) & Information Retrieval: Standardizing TF-IDF word embeddings so document length does not distort semantic similarity.
• Computer Vision & Deep Learning: Normalizing feature embeddings prior to computing Cosine Similarity.
• Distance-Based Models: Removing scale dominance where vector angle holds more diagnostic signal than magnitude.

🧠 Feature Scaling Landscape

| Technique | Operating Axis | Output Range | Key Use Case |
| :--- | :--- | :--- | :--- |
| **Standardization (Z-Score)** | Column-wise (Feature) | μ = 0, σ = 1 | Linear Models, SVM, PCA |
| **Min-Max Scaling** | Column-wise (Feature) | Bounded [0, 1] | Neural Networks, Image Pixels |
| **Unit Vector Scaling** | Row-wise (Sample) | Vector Norm = 1 | Text Classification, Cosine Distance |
