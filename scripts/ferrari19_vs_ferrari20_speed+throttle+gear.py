"""
leclerc_vs_hamilton_all_races.py

Compares average speed and throttle  of Charles Leclerc across all 2019 and 2020 races using telemetry data. 
"""


import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt
import pandas as pd

# Set up plotting and enable cache
plotting.setup_mpl()

# Load qualifying sessions
spa19 = fastf1.get_session(2019, 'Belgium', 'Q')
spa19.load()

spa20 = fastf1.get_session(2020, 'Belgium', 'Q')
spa20.load()

# Get Leclerc's fastest laps
lec_2019 = spa19.laps.pick_driver('LEC').pick_fastest()
lec_2020 = spa20.laps.pick_driver('LEC').pick_fastest()

# Get telemetry data with distance
tel_2019 = lec_2019.get_car_data().add_distance()
tel_2020 = lec_2020.get_car_data().add_distance()

# === Save data to CSV ===
df = pd.DataFrame({
    'Distance (m)': tel_2019['Distance'],
    'Speed 2019 (km/h)': tel_2019['Speed'],
    'Speed 2020 (km/h)': tel_2020['Speed'],
    'Throttle 2019 (%)': tel_2019['Throttle'],
    'Throttle 2020 (%)': tel_2020['Throttle'],
    'Gear 2019': tel_2019['nGear'],
    'Gear 2020': tel_2020['nGear']
})
df.to_csv('leclerc_spa_telemetry_comparison_2019_vs_2020.csv', index=False)
print("Saved data to leclerc_spa_telemetry_comparison_2019_vs_2020.csv")

# === Plot 1: Speed ===
plt.figure(figsize=(12, 6))
plt.plot(tel_2019['Distance'], tel_2019['Speed'], label='Speed 2019', color='red')
plt.plot(tel_2020['Distance'], tel_2020['Speed'], label='Speed 2020', color='darkred')
plt.title('Speed Comparison - Spa Q Leclerc 2019 vs 2020')
plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.tight_layout_
