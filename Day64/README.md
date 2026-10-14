📊 Day 64 – Text & Unstructured String Feature Extraction: E-Commerce Reviews

📅 Date
14 October 2026

📚 Topics Covered

1. Structural Text Metrics
• Calculated total character count (`.str.len()`) and word count (`.split()`) to measure review detail and customer engagement levels.

2. Derived Linguistic Ratios
• Engineered `avg_word_length` (`review_char_len / review_word_count`) to assess vocabulary complexity across reviews.

3. Punctuation Sentiment Markers
• Extracted structural punctuation markers (`!` and `?`) to quantify customer emotional intensity and inquiry frequency.

4. Title Signal Extraction
• Extracted title character lengths (`title_char_len`) after replacing missing text values.

🧠 Feature Extraction Execution Matrix

| Raw Field | Transformation | Derived Feature | Objective |
| :--- | :--- | :--- | :--- |
| **`Review Text`** | `.str.len()` | `review_char_len` | Quantify total review length |
| **`Review Text`** | `.apply(lambda x: len(x.split()))` | `review_word_count` | Quantify total word volume |
| **`Review Text`** | `char_len / word_count` | `avg_word_length` | Measure vocabulary complexity |
| **`Review Text`** | `.apply(lambda x: x.count('!'))` | `exclamation_count` | Isolate emotional sentiment intensity |
