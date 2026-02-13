import numpy as np
import matplotlib.pyplot as plt

# Constants in MKS units
epsilon_0 = 8.854e-12  # Permittivity of free space (F/m)
epsilon_r = 4.4        # Relative permittivity (example value, adjust as needed)
C = 2.0824328e-13      # Capacitance in Farads (example value, adjust as needed)

# Define the equation: C = (W * epsilon_0 * (epsilon_r + 1) / pi) * acosh(a / g)
# Where a = W + g
def calculate_g(W, C, epsilon_0, epsilon_r):
    pi = np.pi
    numerator = C * pi / (epsilon_0 * (epsilon_r + 1))
    # Solve for g using acosh: g = a / cosh(numerator / W)
    # Since a = W + g, we use a numerical approach
    g = W / (np.cosh(numerator / W) - 1)
    return g

# Range of W in meters
W_range = np.linspace(1e-3, 10e-3, 100)  # 1mm to 10mm

# Calculate corresponding g values
g_values = [calculate_g(W, C, epsilon_0, epsilon_r) for W in W_range]

# Convert to mm for plotting and table
W_mm = W_range * 1000
g_mm = np.array(g_values) * 1000

# Print table
print("W (mm)    g (mm)")
for w, g in zip(W_mm, g_mm):
    print(f"{w:.2f}    {g:.2f}")

# Plot
plt.plot(W_mm, g_mm)
plt.xlabel('W (mm)')
plt.ylabel('g (mm)')
plt.title('Relationship between W and g')
plt.grid(True)
plt.show()