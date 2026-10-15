📊 Day 65 – Geospatial Feature Engineering & Haversine Distance: California Housing

📅 Date
15 October 2026

📚 Topics Covered

1. Vectorized Haversine Distance Calculation
• Implemented the Haversine formula to compute great-circle kilometer distances between property coordinates and major economic hubs (San Francisco and Los Angeles).

2. Spatial Reference Feature Extraction
• Engineered `dist_to_sf` and `dist_to_la` to capture target housing price variations linked to proximity to primary employment centers.

3. Structural Housing Density Metrics
• Derived `rooms_per_household` and `bedrooms_per_room` to measure property capacity and room layout distributions.

🧠 Feature Extraction Execution Matrix

| Feature / Input | Formula / Method | Derived Column | Objective |
| :--- | :--- | :--- | :--- |
| **`latitude` / `longitude`** | Haversine Formula (SF Coords) | `dist_to_sf` | Measure distance to San Francisco (km) |
| **`latitude` / `longitude`** | Haversine Formula (LA Coords) | `dist_to_la` | Measure distance to Los Angeles (km) |
| **`total_rooms` / `households`** | `total_rooms / households` | `rooms_per_household` | Capture housing size density |
| **`total_bedrooms` / `total_rooms`** | `total_bedrooms / total_rooms` | `bedrooms_per_room` | Capture room layout ratio |

