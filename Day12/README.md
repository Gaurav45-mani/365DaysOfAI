📊 Day 12 – Student's T-Distribution, Test Selection & Bayes' Theorem

📅 Date

21 August 2026

📚 Topics Covered

1. Student's T-Distribution & Unknown Population Variance
A probability distribution used for hypothesis testing when the population standard deviation (σ) is unknown and estimated using sample standard deviation (s). It features heavier tails than the standard normal distribution to account for additional uncertainty in smaller samples.
• Formula: t = (x̄ - μ) / (s / √n)
• Degrees of Freedom: df = n - 1

2. Decision Framework: T-Test vs. Z-Test
A systematic decision path to select the appropriate statistical test:
• Do you know the population standard deviation (σ)?
  - Yes → Check sample size: If n ≥ 30 → Use Z-Test; If n < 30 → Use T-Test.
  - No → Use T-Test (substituting σ with sample standard deviation s).

3. Bayesian Statistics & Bayes' Theorem
A statistical framework that updates the prior probability of an event based on new evidence or conditional data.
• Independent Events: The occurrence of one event does not impact another (e.g., consecutive dice rolls).
• Dependent Events: The occurrence of one event alters the probability of subsequent events (e.g., drawing marbles without replacement).
• Conditional Probability & Joint Rule: P(A ∩ B) = P(B) * P(A|B) = P(A) * P(B|A)
• Bayes' Formula:
  P(A|B) = [P(A) * P(B|A)] / P(B)

4. Bayes' Theorem in Machine Learning (Supervised Learning Context)
Formulating predictive modeling problems using Bayesian inference:
• Target variable y (e.g., House Price) given feature vectors x1, x2, x3 (Size, Rooms, Location):
  P(y | x1, x2, x3) = [P(y) * P(x1, x2, x3 | y)] / P(x1, x2, x3)
• Forms the direct mathematical foundation for Naive Bayes classification and probabilistic modeling.

🧠 Core Mathematical & Conceptual Framework

• T-Test vs. Z-Test Selection Rules:
  - σ known + n ≥ 30 → Z-Distribution
  - σ unknown (any n) OR σ known + n < 30 → Student's T-Distribution

• Dependent Probability Breakdown:
  - Example: Bag with 3 blue and 2 red balls (Total = 5).
  - P(Red) = 2/5
  - P(Blue | Red removed) = 3/4
  - Joint Probability P(Red and Blue) = (2/5) * (3/4) = 6/20 = 0.30

• Bayesian Inference Terms:
  - P(A): Prior Probability
  - P(B|A): Likelihood
  - P(B): Marginal Probability / Evidence
  - P(A|B): Posterior Probability

💻 Core Learnings

✔ Identified the exact criteria to choose between a Z-Test and a T-Test.
✔ Calculated degrees of freedom (df = n - 1) and standard error using sample standard deviation.
✔ Distinguished mathematically between independent and dependent probability events.
✔ Derived Bayes' Theorem from fundamental conditional probability rules.
✔ Represented multi-feature dataset predictions (features → target) in probabilistic Bayesian notation.

🎯 Key Takeaway

Mastered statistical test selection criteria (Z-Test vs. T-Test) and bridged classical inferential statistics with modern machine learning foundations by learning Bayes' Theorem and posterior probability modeling.

#365DaysOfAI #Statistics #BayesTheorem #Probability #HypothesisTesting #DataScience #MachineLearning #Python
