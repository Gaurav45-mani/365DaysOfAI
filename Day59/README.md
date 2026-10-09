📊 Day 59 – Advanced String Cleaning & EDA: Google Play Store Dataset

📅 Date

09 October 2026

📚 Topics Covered

1. Unit Standardization & Non-Numeric Placeholder Handling
• Standardized mixed units in `'Size'` by replacing `'M'` (Megabytes) with `'000'` scale, stripping `'k'`, and coercing `'Varies with device'` text to `np.nan`.
• Cast cleaned entries to `float` for numerical aggregation.

2. Outlier Row Removal
• Identified corrupted index row `10472` containing shifted categorical values and removed it via `df_copy.drop(df_copy.index[10472])`.

3. Multi-Column Special Character Stripping
• Cleared symbols (`'+'`, `','`, `'$'`) across `'Installs'` and `'Price'` via nested iteration loops using `.str.replace()`.
• Converted string amounts into quantitative integers and floating-point variables.

4. Temporal Component Extraction
• Parsed text dates (`'January 7, 2018'`) using `pd.to_datetime()`.
• Derived explicit `'Day'`, `'Month'`, and `'Year'` numerical features via `.dt` property accessors.

5. Automated Seaborn Grid Visualization
• Programmatically plotted Kernel Density Estimation (`sns.kdeplot(shade=True)`) graphs for all numerical attributes inside a dynamic 5x3 subplot grid.

🧠 Cleaning Operations Summary Matrix

| Feature | Raw Format | Noise Removed | Transformation Applied |
| :--- | :--- | :--- | :--- |
| **`Size`** | `'19M'`, `'10k'`, `'Varies with device'` | `'M'`, `'k'`, `'Varies...'` | Unit replacement $\rightarrow$ `np.nan` $\rightarrow$ `float` |
| **`Installs`** | `'10,000,000+'` | `','`, `'+'` | Nested `.str.replace()` $\rightarrow$ `int` |
| **`Price`** | `'$2.48'` | `'$'` | `.str.replace('$','')` $\rightarrow$ `float` |
| **`Last Updated`**| `'January 7, 2018'` | String month/day format | `pd.to_datetime()` $\rightarrow$ `.dt.day/month/year` |
