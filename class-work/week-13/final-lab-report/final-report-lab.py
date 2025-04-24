import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv("clean_data_single_filter.csv", delimiter=",")

m = 0.00087  # Mass of one filter (kg)
m_uncertainty = 0.00001
m_run1 = 0.0087 # Mass at run 1 (kg)
A = 0.01916  # Cross-sectional area (m²)
d = 2 * np.sqrt(A / np.pi)
relative_uncertainty_d = 0.001 / d
relative_uncertainty_A = 2 * relative_uncertainty_d
A_uncertainty = round((A * relative_uncertainty_A), 8) # Uncertainty of A, 0.00025 m²
p = 1.204 # Air density (kg/m³)
p_uncertainty = 0.001
g = 9.81  # Gravity (m/s²)
g_uncertainty = 0.005

v_values = [-0.97035897, -1.02553846, -1.0791453, -0.99586325, 
            -0.98684615, -1.02413675, -0.97470085, -0.82321368, 
            -0.98632479, -0.95158974]
v_magnitudes = [abs(v) for v in v_values]
v_term = np.mean(v_magnitudes)
v_term_uncertainty = (max(v_magnitudes) - min(v_magnitudes)) / 2

C = (2 * m * g) / (p * A * (v_term ** 2))

print(C)

relative_uncertainty_C = (
    m_uncertainty / m +
    g_uncertainty / g +
    p_uncertainty / p +
    A_uncertainty / A +
    2 * (v_term_uncertainty / v_term)
)
C_uncertainty = C * relative_uncertainty_C

print(C_uncertainty)


def Acceleration(v):
    return -g + ((C * p * A * (v ** 2)) / (2 * m_run1))

initial_position = 0.73
initial_velocity = 0.0   
dt = 0.001  

time = [0.1]
position = [initial_position]
velocity = [initial_velocity]

while initial_position > 0:
    ay = Acceleration(initial_velocity)  
    new_velocity = initial_velocity + ay * dt  
    new_position = initial_position + new_velocity * dt

    if new_position < 0:
        new_position = 0  

    initial_position = new_position
    initial_velocity = new_velocity

    time.append(time[-1] + dt)
    position.append(new_position)
    velocity.append(new_velocity)

plt.figure(figsize=(8, 6)) 

plt.plot(time, position, label="Euler Method (Simulation)", linewidth=2, color='blue')

time_column = df["Time (s) Run #1"]
position_column = df["Position (m) Run #1"]

valid_indices = position_column > 0
last_valid_index = valid_indices[valid_indices].index[-1] 

plt.scatter(time_column[:last_valid_index], position_column[:last_valid_index], s=10, label="Run 1", alpha=0.7, c="red")

plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Euler Simulation vs. Experimental Data")
plt.legend()  
plt.grid(True)  
plt.show()