📊 Day 72 – Mathematical Foundations of Simple Linear Regression & Cost Function

📅 Date
22 October 2026

📚 Topics Covered

1. Supervised Learning Taxonomy
• Continuous target variables utilize Regression, while categorical targets utilize Classification.

2. Simple Linear Regression Formulation
• Formulated hypothesis line $h_\theta(x) = \theta_0 + \theta_1 x_1$, where $\theta_0$ represents intercept and $\theta_1$ represents slope.

3. Mean Squared Error (MSE) Cost Function
• Derived the error optimization equation:
  $$J(\theta_0, \theta_1) = \frac{1}{n} \sum_{i=1}^{n} (y_i - h_\theta(x_i))^2$$

4. Step-by-Step Numerical Walkthrough
• Evaluated MSE across parameter variations ($\theta_1 \in \{1.0, 0.5, 0.0\}$) to demonstrate how cost functions quantify model error.

🧠 Parameter vs. Cost Evaluation Matrix

| Slope ($\theta_1$) | Predictions $h_\theta(x)$ | MSE Calculation ($J(\theta_1)$) | Cost Value |
| :--- | :--- | :--- | :--- |
| **$\theta_1 = 1.0$** | $\{1.0, 2.0, 3.0\}$ | $\frac{1}{3}[(0)^2 + (0)^2 + (0)^2]$ | **0.00** |
| **$\theta_1 = 0.5$** | $\{0.5, 1.0, 1.5\}$ | $\frac{1}{3}[(0.5)^2 + (1.0)^2 + (1.5)^2]$ | **1.16** |
| **$\theta_1 = 0.0$** | $\{0.0, 0.0, 0.0\}$ | $\frac{1}{3}[(1.0)^2 + (2.0)^2 + (3.0)^2]$ | **4.66** |

🎯 Key Takeaway
Mastered mathematical foundations of Simple Linear Regression, hypothesis formulation, and manual calculation of Mean Squared Error (MSE) cost values.
#365DaysOfAI #MachineLearning #DataScience #LinearRegression #Mathematics #AI
