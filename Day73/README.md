📊 Day 73 – Gradient Descent Optimization & Convergence Algorithm

📅 Date
23 October 2026

📚 Topics Covered

1. Cost Function Geometry & Global Minima
• Analyzed the convex U-shaped parabola formed by plotting parameter values against error, identifying the global minima where error is optimized.

2. Gradient Descent Update Rule
• Studied the core parameter updating equation:
  $$\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta_j)$$

3. Role of Slope and Directional Movement
• Negative Slope (Angle > 90°): Subtracting a negative derivative increases $\theta$, driving the weight rightward toward the minimum.
• Positive Slope (Angle < 90°): Subtracting a positive derivative decreases $\theta$, driving the weight leftward toward the minimum.

4. Impact of Learning Rate ($\alpha$)
• Standard Default: Typically initialized at $\alpha = 0.01$.
• Small $\alpha$: Guaranteed but extremely slow convergence.
• Large $\alpha$: Causes wild oscillations and overshoot across the global minima.

🧠 Gradient Descent Direction Matrix

| Initial Position | Derivative / Slope Sign | Update Equation | Movement Direction |
| :--- | :--- | :--- | :--- |
| **Left of Minima** | Negative ($-$) | $\theta_{\text{new}} = \theta_{\text{old}} - \alpha(-\text{slope})$ | Increases $\theta \rightarrow$ Rightward |
| **Right of Minima** | Positive ($+$) | $\theta_{\text{new}} = \theta_{\text{old}} - \alpha(+\text{slope})$ | Decreases $\theta \leftarrow$ Leftward |

🎯 Key Takeaway
Mastered the mathematical mechanics of Gradient Descent, weight update equations, derivative slopes, and the role of learning rate tuning.

🔗 Quick Links
• Day 73 Module Folder: https://github.com/Gaurav45-mani/365DaysOfAI/tree/main/Day73
• Day 73 Notes: https://github.com/Gaurav45-mani/365DaysOfAI/blob/main/Day73/Day73_Notes.pdf

#365DaysOfAI #MachineLearning #DataScience #GradientDescent #Mathematics #AI
