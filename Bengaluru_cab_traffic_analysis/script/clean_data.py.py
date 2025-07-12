

import pandas as pd

# Load raw CSV from data folder
df = pd.read_csv(r"D:\DATA ANALYTICS PREPARATIONS\PIPELINE PROJECT\Bengaluru_cab_traffic_analysis\data\bengaluru_cab_data_raw.csv")

# Convert pickup and drop times to datetime
df['pickup_time'] = pd.to_datetime(df['pickup_time'])
df['drop_time'] = pd.to_datetime(df['drop_time'])

# Create trip duration column
df['trip_duration_mins'] = (df['drop_time'] - df['pickup_time']).dt.total_seconds() / 60

# Extract hour and weekday
df['hour'] = df['pickup_time'].dt.hour
df['weekday'] = df['pickup_time'].dt.day_name()

# Flag peak hours (7–10 AM and 5–8 PM)
df['is_peak'] = df['hour'].apply(lambda x: 1 if x in [7,8,9,17,18,19] else 0)

# Save cleaned data
df.to_csv("../data/bengaluru_cab_data_cleaned.csv", index=False)

print("✅ Cleaning complete. Saved as bengaluru_cab_data_cleaned.csv")
