
"""
leclerc_vs_hamilton_all_races.py

Compares average acceleration of Charles Leclerc across all 2019 and 2020 races using telemetry data. 
"""



import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Setup and load sessions
plotting.setup_mpl()

spa19 = fastf1.get_session(2019, 'Belgium', 'Q')
spa19.load()

spa20 = fastf1.get_session(2020, 'Belgium', 'Q')
spa20.load()

# Get Leclerc's fastest laps
lec_2019 = spa19.laps.pick_driver('LEC').pick_fastest()
lec_2020 = spa20.laps.pick_driver('LEC').pick_fastest()

# Get telemetry with distance
tel_2019 = lec_2019.get_car_data().add_distance()
tel_2020 = lec_2020.get_car_data().add_distance()

# Convert speed to m/s for acceleration
speed_2019_ms = tel_2019['Speed'] * (1000 / 3600)
speed_2020_ms = tel_2020['Speed'] * (1000 / 3600)

# Compute acceleration (a = dv/dx)
acc_2019 = np.gradient(speed_2019_ms, tel_2019['Distance'])
acc_2020 = np.gradient(speed_2020_ms, tel_2020['Distance'])

# Save to CSV
df = pd.DataFrame({
    'Distance (m)': tel_2019['Distance'],
    'Acceleration 2019 (m/s²)': acc_2019,
    'Acceleration 2020 (m/s²)': acc_2020
})
df.to_csv('leclerc_spa_acceleration_2019_vs_2020.csv', index=False)
print("Saved data to leclerc_spa_acceleration_2019_vs_2020.csv")

# Plot acceleration
plt.figure(figsize=(12, 6))
plt.plot(tel_2019['Distance'], acc_2019, label='Acceleration 2019', color='yellow')
plt.plot(tel_2020['Distance'], acc_2020, label='Acceleration 2020', color='red')
plt.title('Acceleration Comparison - Spa Q Leclerc 2019 vs 2020')
plt.xlabel('Distance (m)')
plt.ylabel('Acceleration (m/s²)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save figure
plt.savefig('leclerc_spa_acceleration_2019_vs_2020.png', dpi=300)
print("Saved figure to leclerc_spa_acceleration_2019_vs_2020.png")

plt.show()
