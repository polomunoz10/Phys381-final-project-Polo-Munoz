# Sample script comapring Ferrari's speed in 2019 and 2020



# Set up plotting 
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

# === Plot 1: Speed ===
plt.figure(figsize=(12, 6))
plt.plot(tel_2019['Distance'], tel_2019['Speed'], label='Speed 2019', color='red')
plt.plot(tel_2020['Distance'], tel_2020['Speed'], label='Speed 2020', color='darkred')
plt.title('Speed Comparison - Spa Q Leclerc 2019 vs 2020')
plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === Plot 2: Throttle ===
plt.figure(figsize=(12, 6))
plt.plot(tel_2019['Distance'], tel_2019['Throttle'], label='Throttle 2019', color='red')
plt.plot(tel_2020['Distance'], tel_2020['Throttle'], label='Throttle 2020', color='darkred')
plt.title('Throttle Comparison - Spa Q Leclerc 2019 vs 2020')
plt.xlabel('Distance (m)')
plt.ylabel('Throttle (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === Plot 3: Gear ===
plt.figure(figsize=(12, 6))
plt.plot(tel_2019['Distance'], tel_2019['nGear'], label='Gear 2019', color='yello')
plt.plot(tel_2020['Distance'], tel_2020['nGear'], label='Gear 2020', color='darkred')
plt.title('Gear Usage - Spa Q Leclerc 2019 vs 2020')
plt.xlabel('Distance (m)')
plt.ylabel('Gear')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
