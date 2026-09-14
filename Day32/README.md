📊 Day 32 – Data Interpolation Techniques: Linear, Cubic & Polynomial

14 September 2026

📚 Topics Covered

1. What is Data Interpolation?
The mathematical and statistical process of estimating unknown intermediate values located within the range of a discrete set of known data points. Widely used in feature engineering, signal processing, and handling missing time-series observations.

2. Linear Interpolation
• Computes unknown values assuming a constant straight-line rate of change between two adjacent known points.
• Mathematical Formulation:
  y = y₁ + [(y₂ - y₁) / (x₂ - x₁)] * (x - x₁)
• Programmatic Implementation: Executed using `np.interp(x_new, x, y)`.

3. Cubic Interpolation (SciPy)
• Fits piecewise third-degree polynomials (cubic splines) across data points to ensure continuous, smooth curves without abrupt angular transitions.
• Ideal for non-linear progressions (e.g., cubic relationships where y = x³).
• Programmatic Implementation: Configured using `scipy.interpolate.interp1d(x, y, kind='cubic')`.

4. Polynomial Interpolation (NumPy)
• Fits a single polynomial curve of a chosen degree (n) across the entire dataset to capture non-linear trends.
• Higher degrees allow the curve to bend more to fit non-linear patterns (e.g., quadratic growth y = x²).
• Programmatic Implementation: Uses `np.polyfit(x, y, deg)` to determine polynomial coefficients and `np.polyval(p, x_new)` to evaluate interpolated estimates.

🧠 Interpolation Comparison Matrix

| Technique | Mathematical Nature | Best Suited For | Tool / Function |
| :--- | :--- | :--- | :--- |
| **Linear** | 1st-degree piecewise lines | Flat, constant-rate trends | `np.interp` |
| **Cubic Spline** | 3rd-degree piecewise curves | Smooth, non-linear curves | `scipy.interpolate.interp1d` |
| **Polynomial** | n-th degree global polynomial | Curved trends with known degrees | `np.polyfit` & `np.polyval` |

