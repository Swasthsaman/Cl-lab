import numpy as np
import matplotlib.pyplot as plt

# Input characteristics parameters
V_BEON = 0.7  # Base-emitter turn-on voltage
R_BE = 1000   # Base-emitter resistance (just for illustration)
V_BE = np.linspace(0.7, 1.2, 100)  # Base-emitter voltage range

# Calculate base current (IB)
I_B = (V_BE - V_BEON) / R_BE

# Plot input characteristics
plt.figure(figsize=(8, 6))
plt.plot(V_BE, I_B, label='Input Characteristics')
plt.xlabel('Base-Emitter Voltage (V_BE)')
plt.ylabel('Base Current (I_B)')
plt.title('Input Characteristics of Common Emitter BJT')
plt.grid(True)
plt.legend()
plt.show()

# Output characteristics parameters
V_CC = 5     # Collector supply voltage
R_C = 1000   # Collector load resistance (just for illustration)
V_CE = np.linspace(0, 5, 100)  # Collector-emitter voltage range

# Calculate collector current (IC) for common emitter configuration
I_C = (V_CC - V_CE) / R_C

# Plot output characteristics
plt.figure(figsize=(8, 6))
plt.plot(V_CE, I_C, label='Output Characteristics')
plt.xlabel('Collector-Emitter Voltage (V_CE)')
plt.ylabel('Collector Current (I_C)')
plt.title('Output Characteristics of Common Emitter BJT')
plt.grid(True)
plt.legend()
plt.show()

