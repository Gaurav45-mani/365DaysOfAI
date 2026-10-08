📊 Day 58 – Feature Engineering Pipeline: Flight Price Prediction Dataset

📅 Date

08 October 2026

📚 Topics Covered

1. Temporal String Extraction & Type Conversion
• Extracted day, month, and year integers from raw `'Date_of_Journey'` strings via `.str.split('/')` and `.astype(int)`.
• Parsed `'Arrival_Time'` by stripping dates and splitting hour-minute strings into independent numerical features.

2. Ordinal Mapping & Mode Imputation
• Standardized `'Total_Stops'` text levels (`non-stop` through `4 stops`) into numerical integers (`0` to `4`).
• Imputed missing `NaN` values using the calculated mode (`1 stop`).

3. Nominal Vectorization using One-Hot Encoding
• Applied Scikit-Learn's `OneHotEncoder` across `'Airline'`, `'Source'`, and `'Destination'`.
• Extracted clean column headers via `get_feature_names_out()` and combined them with `pd.concat(axis=1)`.

🧠 Feature Engineering Execution Matrix

| Raw Feature | Issue / Format | Transformation Applied | Output Type |
| :--- | :--- | :--- | :--- |
| **`Date_of_Journey`** | String (`'24/03/2019'`) | `.str.split('/')` & `.astype(int)` | 3 Numeric Columns (`Date`, `Month`, `Year`) |
| **`Arrival_Time`** | Strings with dates | `.str.split(' ')` then `.str.split(':')` | 2 Numeric Columns (`Arrival_hours`, `Arrival_min`) |
| **`Total_Stops`** | Text with `NaN` | Ordinal dictionary mapping + Mode Imputation | Integer Column (`0` to `4`) |
| **`Airline` / `Source`**| Nominal text | `OneHotEncoder().fit_transform()` | Binary Feature Matrix |
