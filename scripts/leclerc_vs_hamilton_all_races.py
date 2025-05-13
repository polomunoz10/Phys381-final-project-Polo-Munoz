"""
leclerc_vs_hamilton_all_races.py

Compares average speeds of Charles Leclerc and Lewis Hamilton across all 2019 races using telemetry data. Simply replace session information in line 12 to render desired race.
"""

import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt
import pandas as pd

# Load the session
session = fastf1.get_session(2019, 'Australia', 'R')
session.load()

# Get accurate laps
laps_ham = session.laps.pick_driver('HAM').pick_accurate()
laps_lec = session.laps.pick_driver('LEC').pick_accurate()

# Get top speeds from telemetry
ham_top_speeds = [lap.get_telemetry()['Speed'].max() for _, lap in laps_ham.iterlaps()]
lec_top_speeds = [lap.get_telemetry()['Speed'].max() for _, lap in laps_lec.iterlaps()]

# Calculate max speed
max_speed_ham = max(ham_top_speeds)
max_speed_lec = max(lec_top_speeds)

# Save data to CSV
df = pd.DataFrame({
    'Driver': ['Hamilton', 'Leclerc'],
    'Top Speed (km/h)': [max_speed_ham, max_speed_lec]
})
df.to_csv('australia_2019_top_speeds.csv', index=False)
print("Saved data to australia_2019_top_speeds.csv")

# Plotting
drivers = ['Hamilton', 'Leclerc']
top_speeds = [max_speed_ham, max_speed_lec]
colors = ['blue', 'red']

plt.figure(figsize=(8, 6))
plt.bar(drivers, top_speeds, color=colors, edgecolor='black')
plt.title('Top Speed Comparison - Australian GP 2019')
plt.ylabel('Top Speed (km/h)')
plt.ylim(300, max(top_speeds) + 10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add speed labels above bars
for i, v in enumerate(top_speeds):
    plt.text(i, v + 1, f"{v:.1f} km/h", ha='center', fontweight='bold')

# Save the figure
plt.tight_layout()
plt.savefig('australia_2019_top_speeds.png', dpi=300)
print("Saved figure to australia_2019_top_speeds.png")

# Show the plot
plt.show()
