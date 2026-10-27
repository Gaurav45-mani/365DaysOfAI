📊 Day 78 – Cost Functions & Evaluation Metrics in Regression (MSE, MAE, RMSE)

📅 Date
28 October 2026

📚 Topics Covered

1. Measuring Model Error
• Evaluated prediction residuals ($y_i - \hat{y}_i$) to quantify model performance across continuous target predictions.

2. Mean Squared Error (MSE)
• Equation: $$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
• Mathematical Advantage: Forms a smooth, convex parabola with a single global minimum, enabling smooth and fast Gradient Descent convergence.
• Tradeoffs: Highly sensitive to outliers due to quadratic penalty; output is expressed in squared units ($\text{Unit}^2$), making business interpretation non-intuitive.

3. Mean Absolute Error (MAE)
• Equation: $$MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
• Mathematical Advantage: Robust against outlier distortion and retains the exact scale/unit of the target variable.
• Tradeoffs: Creates a non-differentiable sharp V-shaped corner at zero, leading to slower optimization convergence times.

4. Root Mean Squared Error (RMSE)
• Equation: $$RMSE = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$
• Mathematical Advantage: Restores the original target unit scale while retaining the smooth optimization properties of squared errors.
• Tradeoffs: Remains sensitive to extreme outlier values.

🧠 Metric Comparison & Selection Matrix

| Evaluation Metric | Mathematical Formula | Outlier Sensitivity | Scale / Unit | Optimization Gradient |
| :--- | :--- | :--- | :--- | :--- |
| **MSE** | $\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$ | High (Penalizes large errors) | Squared ($\text{Unit}^2$) | Fast & Smooth (Convex Bowl) |
| **MAE** | $\frac{1}{n} \sum_{i=1}^{n} \|y_i - \hat{y}_i\|$ | Low (Linear penalty) | Original ($\text{Unit}$) | Slower (V-Shape Corner) |
| **RMSE**| $\sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$ | High (Penalizes large errors) | Original ($\text{Unit}$) | Fast & Smooth (Convex Bowl) |

🎯 Key Takeaway
Mastered mathematical tradeoffs between MSE, MAE, and RMSE regarding outlier robustness, unit scale interpretability, and optimization convergence speed.

#365DaysOfAI #MachineLearning #DataScience #LinearRegression #RegressionMetrics #AI
