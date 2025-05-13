"""
leclerc_vs_hamilton_all_races.py

Leclerc vs Hamilton histograms across Azerbaijan, Spa, Monza, and Mexico for the year 2019
"""



import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define rounds for high-speed tracks
high_speed_tracks = {
    'Baku': 4,
    'Spa': 13,
    'Monza': 14,
    'Mexico': 18
}

# Drivers and colors
drivers = {
    'LEC': 'red',
    'VET': 'darkred',
    'HAM': 'silver',
    'BOT': 'gray'
}

# Initialize DataFrame to hold results
data = {'Grand Prix': list(high_speed_tracks.keys())}

# Extract and store top speeds
for driver in drivers:
    avg_speeds = []

    for track, round_no in high_speed_tracks.items():
        session = fastf1.get_session(2019, round_no, 'R')
        session.load()

        laps = session.laps.pick_driver(driver).pick_accurate()
        speeds = []

        for _, lap in laps.iterrows():
            tel = lap.get_telemetry()
            if not tel.empty:
                speeds.append(tel['Speed'].max())

        avg_top = sum(speeds) / len(speeds) if speeds else 0
        avg_speeds.append(avg_top)

    data[driver] = avg_speeds

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('avg_top_speeds_2019.csv', index=False)
print("Data saved to avg_top_speeds_2019.csv")

# Plotting: grouped histogram
x = np.arange(len(df['Grand Prix']))  # label positions
width = 0.2  # bar width
offsets = np.linspace(-1.5, 1.5, len(drivers)) * width

plt.figure(figsize=(10, 6))

for i, (driver, color) in enumerate(drivers.items()):
    plt.bar(x + offsets[i], df[driver], width=width, label=driver, color=color)

plt.xticks(x, df['Grand Prix'])
plt.title("Ferrari vs Mercedes - Average Top Speeds at Fastest Tracks (2019)")
plt.xlabel("Grand Prix")
plt.ylabel("Avg. Top Speed per Lap (km/h)")
plt.grid(True, axis='y')
plt.legend()
plt.tight_layout()
plt.show()
