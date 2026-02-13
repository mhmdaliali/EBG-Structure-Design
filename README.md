# Electromagnetic Band Gap (EBG) Structure Design

## Overview

This Python script designs electromagnetic band gap (EBG) structures in the form of mushroom square patches. EBG structures are periodic metallic patterns that suppress surface waves and electromagnetic interference in high-speed PCB designs.

## Theory

The mushroom EBG structure consists of square metallic patches connected to a ground plane through vias. The capacitance between adjacent patches is given by:

```
C = (W * ε₀ * (εᵣ + 1) / π) * acosh(a / g)
```

Where:
- `W` = width of the square patch (m)
- `g` = gap between adjacent patches (m)
- `a = W + g` = center-to-center spacing (m)
- `ε₀` = permittivity of free space = 8.854 × 10⁻¹² F/m
- `εᵣ` = relative permittivity of the substrate

## Design Variables

### Primary Variables (to be optimized)
- **W**: Width of the square patches (mm)
- **g**: Separation gap between patches (mm)

### Input Parameters (PCB stack-up specific)
- **Substrate thickness (h)**: For example: 0.5 - 2.0 mm
- **Dielectric constant (εᵣ)**: Common values:
  - FR-4: 4.2 - 4.4
  - Rogers RO4003C: 3.38
  - Rogers RO4350B: 3.48
- **Target Capacitance (C)**: Determines the gap for a given patch width

## Installation

### Requirements

```bash
pip install numpy matplotlib
```

## Usage

### Basic Usage

Run the script directly:

```bash
python ebg_design.py
```

### Customization

Modify the input parameters at the top of the script:

```python
# For different PCB materials
epsilon_r = 4.4  # FR-4
epsilon_r = 3.38 # Rogers RO4003C
epsilon_r = 3.48 # Rogers RO4350B

# Adjust target capacitance
C = 2.0824328e-13  # Farads

# Change design range
W_range = np.linspace(1e-3, 10e-3, 100)  # 1mm to 10mm patches
```

## Output

The script generates:

1. **Console Table**: Lists W and g values in millimeters
   ```
   W (mm)    g (mm)
   1.00      0.42
   1.09      0.46
   ...
   ```

2. **Plot**: Graphical visualization of the W vs g relationship

## Design Guidelines

### Typical Design Constraints

- **Minimum gap (g)**: Limited by PCB manufacturing capability (typically ≥ 0.1mm for standard processes)
- **Patch width (W)**: Should be smaller than λ/4 at the frequency of interest
- **Via diameter**: Typically 0.2 - 0.5 mm
- **Via spacing**: Should equal patch periodicity (a = W + g)

### Bandwidth Considerations

The fractional bandwidth of an EBG structure is approximated by:

```
BW ≈ (1/π) * sqrt(L/C) / sqrt(LC)
```

Where L is the inductance of the via connections.

## Applications

- **High-speed digital PCBs**: Suppression of simultaneous switching noise (SSN)
- **Antenna design**: Ground plane for low-profile antennas
- **EMI/EMC**: Reduction of electromagnetic interference
- **Power integrity**: Noise suppression in power distribution networks

## Example Results

For typical FR-4 substrate (εᵣ = 4.4) and C = 0.208 pF:
- W = 5 mm → g ≈ 0.21 mm
- W = 8 mm → g ≈ 0.34 mm
- W = 10 mm → g ≈ 0.42 mm

## References

1. Sievenpiper, D., et al. "High-impedance electromagnetic surfaces with a forbidden frequency band." IEEE Transactions on Microwave Theory and Techniques (1999).
2. Yang, F., and Y. Rahmat-Samii. "Electromagnetic band gap structures in antenna engineering." Cambridge University Press (2009).

## License

MIT License - Feel free to use and modify for your projects.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

M. Ali

## Acknowledgments

This code is based on the theoretical framework for mushroom-type EBG structures developed by Sievenpiper et al.
