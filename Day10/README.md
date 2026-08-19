📊 Day 10 – Estimation, Hypothesis Testing & P-Values

📅 Date

19 August 2026

📚 Topics Covered

1. Statistical Estimation (Point & Interval)
Estimation is the process of using observed sample data to determine unknown population parameters. 
• Point Estimate: A single numerical value calculated from sample data (like the sample mean or sample proportion) that serves as the best guess for the true population parameter.
• Interval Estimate: A range or bracket of values within which the population parameter is expected to fall, incorporating uncertainty and a specific confidence level.

2. Inferential Statistics & Hypothesis Testing Mechanism
Inferential statistics allows us to draw reliable conclusions and make inferences about a large population based purely on evidence from a smaller sample. The hypothesis testing framework follows a four-step mechanism:
• Null Hypothesis (H0): The initial default baseline assumption you begin with, stating that there is no effect, no difference, or that the system/test is completely fair (e.g., Coin is fair, P(Head) = 0.5).
• Alternative Hypothesis (H1): The exact opposite of the null hypothesis representing the claim or difference you want to prove (e.g., Coin is biased/not fair, P(Head) ≠ 0.5).
• Experiments & Evidence Collection: Running the statistical experiment (e.g., 100 coin tosses) and gathering empirical proof.
• Decision: Deciding whether to reject H0 or fail to reject H0 based on the evidence.

3. P-Value, Significance Level (α) & Rejection Regions
• P-Value: A probability value between 0 and 1 calculated from the statistical test. It measures how likely you are to observe data as extreme as your experiment results assuming the Null Hypothesis (H0) is true.
• Significance Level (α): The threshold probability for making a decision, commonly set to α = 0.05.
• Confidence Interval (CI): The complement of the significance level, CI = 1 - α (for α = 0.05, CI = 0.95 or 95%).
• Two-Tailed Distribution Split: For a 95% Confidence Interval, the error margin is divided equally into both rejection tails (α / 2 = 0.025 on each side).
• Decision Rule:
  - If P-value < α (Low P-value) → Reject the Null Hypothesis (H0) (The result is statistically significant).
  - If P-value ≥ α (High P-value) → Fail to reject the Null Hypothesis (H0) (The result falls inside the acceptance region).

🧠 Theoretical Deep Dive & Examples

• Coin Toss Experiment (100 Tosses):
  - H0: Coin is fair (Expected P(Head) = 0.5, P(Tail) = 0.5).
  - H1: Coin is not fair (P(Head) ≠ 0.5).
  - Results around the center (e.g., 40 to 60 heads) fall in the non-rejection zone ("Fail to reject H0").
  - Extreme outcomes falling into the far tails (e.g., < 30 or > 70 heads) fall into the rejection region ("Reject H0").

• P-Value Decision Example:
  - Setting α = 0.05 (95% CI).
  - If an experiment yields a P-value = 0.01:
  - Since 0.01 < 0.05 (P < α), the result is highly unlikely under H0, leading to the rejection of the null hypothesis.

💻 Core Learnings

✔ Differentiated between single-value Point Estimates and range-based Interval Estimates.
✔ Formulated standard pairs of Null (H0) and Alternative (H1) hypotheses.
✔ Mapped standard normal bell curves into Acceptance vs. Rejection Regions.
✔ Divided two-tailed significance levels into left and right tail critical values (α/2 = 0.025).
✔ Applied the fundamental rule: "Low P-value (< α), Reject the Null Hypothesis."

🎯 Key Takeaway

Learned the foundational structure of Inferential Statistics: framing testable hypotheses (H0 vs H1), establishing significance thresholds (α = 0.05), and using P-values to objectively decide whether sample evidence justifies rejecting the null assumption.

#365DaysOfAI #Statistics #InferentialStatistics #HypothesisTesting #DataScience #MachineLearning #Mathematics
