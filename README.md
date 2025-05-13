# Phys381-final-project-Polo-Munoz
This project investigates whether Ferrari may have had an engine performance advantage by potentially bypassing fuel flow regulations — a controversy that arose during the 2019 Formula 1 season. Using telemetry data accessed through the FastF1 Python library, the analysis focuses on:
- Acceleration and speed profiles  
- Braking and throttle traces  
- Kinematic comparisons with other teams  
- Signs of anomalous fuel delivery behavior

The goal is to determine whether on-track telemetry supports suspicions of noncompliant fuel flow manipulation.

Plots and data outputs are generated automatically when the code is run. See plt.savefig() and df.to_csv() lines in each script.
## Files
- `temp.py`: Python script for loading, processing, and plotting telemetry data
- `figure.png`: Placeholder for output figure
- `README.md`: Project documentation
## Output

Each script is set up to generate and save outputs automatically:
- Plots are saved using `plt.savefig(...)`
- Data tables are saved using `df.to_csv(...)`

These files will be created when the code is run locally. See each script for details.
  

## Requirements
- Python 3.9.13
- fastf1
- matplotlib
- numpy

## How to Run
1. Install dependencies:  
   `pip install fastf1 matplotlib numpy`

2. Run the script:  
   `python temp.py
