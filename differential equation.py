import numpy as np
import matplotlib.pyplot as plt

# Diode parameters
I_S = 1e-12  # Reverse saturation current
V_T = 0.025  # Thermal voltage (approximately 25 mV at room temperature)
V_D_forward = np.linspace(0, 1, 400)  # Forward bias diode voltage range
V_D_reverse = np.linspace(-5, 0, 400)  # Reverse bias diode voltage range

# Calculate diode currents
I_D_forward = I_S * (np.exp(V_D_forward / V_T) - 1)
I_D_reverse = -I_S * (np.exp(-V_D_reverse / V_T))

# Plot the I-V characteristic curve
plt.figure(figsize=(8, 6))
plt.plot(V_D_forward, I_D_forward, label='Forward Bias Diode I-V Characteristic')
plt.plot(V_D_reverse, I_D_reverse, label='Reverse Bias Diode I-V Characteristic')
plt.xlabel('Diode Voltage (V_D) [V]')
plt.ylabel('Diode Current (I_D) [A]')
plt.title('PN Junction Diode I-V Characteristic')
plt.grid(True)
plt.legend()
plt.show()

