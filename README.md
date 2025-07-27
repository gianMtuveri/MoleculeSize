# MoleculeSize

# Circular Molecule Acceptance Simulation in a Circular Pore

This project simulates the probability of accepting circular molecules (with a random radius) inside a circular pore. The code generates random molecular configurations, checks if they fit within the pore, and compares the experimental acceptance probability (from normalized histograms) with the theoretical prediction. Visualization is provided using Matplotlib.

## Features

- Uniform random generation of molecule radii and positions
- Acceptance test based on molecule-pore geometry
- Experimental histogram of accepted radii, normalized by number of configurations
- Error bars calculated using Poisson statistics
- Analytical probability function for comparison

## Usage

1. Ensure you have Python 3, numpy, and matplotlib installed.
2. Run the script:
   ```bash
   python circular_molecule_simulation.py
   ```
3. The script will output:
   - A visualization of all generated molecule centers in the pore
   - The normalized histogram of accepted radii with error bars
   - Theoretical probability curve for comparison

## Parameters

- `a`, `b`: Minimum and maximum molecule radius for the uniform distribution
- `N`: Number of configurations (samples)
- `nbins`: Number of bins in the histogram
- `pore.radius`: Radius of the circular pore

## Output

- `Distr_rt_uni.png`: Visualization of molecule centers within the pore
- Probability histogram and theoretical curve (displayed with matplotlib)
