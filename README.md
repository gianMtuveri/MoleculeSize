# MoleculeSize

### Overview

This script simulates the interaction between circular molecules and a circular pore. It uses a truncated normal distribution to generate molecule radii and evaluates which molecules fit inside the pore based on their position and size. The script visualizes accepted configurations and their probability distribution, allowing for comparison between simulated and theoretical results.

### Features

- **Generates molecule radii** using a truncated normal distribution.
- **Simulates random placement** of molecules and evaluates whether they fit inside a circular pore.
- **Visualizes the accepted configurations** and their probability distribution.
- **Compares simulation results to theoretical acceptance probabilities**.

### How It Works

1. **Initialization**:  
   - A circular pore is created with a specified radius.
   - Molecule radii are generated from a truncated normal distribution (parameters `mu` and `sigma`).
2. **Simulation**:  
   - For a specified number of molecules (`N`), each molecule is randomly placed within the pore.
   - The script checks if the molecule fits (is fully inside the pore) based on its center and radius.
   - Accepted radii are stored for further analysis.
3. **Visualization**:  
   - Plots the truncated normal distribution of radii.
   - Shows a histogram of accepted molecule radii, normalized and with error bars.
   - Plots the theoretical acceptance probability for comparison.

### Usage

1. **Dependencies**:  
   Ensure you have the following Python packages installed:
   - numpy
   - matplotlib
   - scipy

   You can install them using pip:
   ```bash
   pip install numpy matplotlib scipy
   ```

2. **Run the Script**:  
   ```bash
   python circ-circRT_wDistNormTrunc.py
   ```

3. **Configurable Parameters**:  
   - `N`: Number of molecules to simulate (default: 1000).
   - `mu`: Mean of the truncated normal distribution for molecule radius (default: 6).
   - `sigma`: Standard deviation of the truncated normal distribution (default: 1.5).
   - `poro.radius`: Radius of the circular pore (default: 10).

4. **Outputs**:  
   - `MCintegr.png`: Plot of the truncated normal radius distribution.
   - Probability histogram and theoretical curve displayed using matplotlib.

### Code Structure

- **Classes**:  
  - `Circonf`: Represents the circular pore.
  - `Circ`: Represents a circular molecule; handles random placement and radius assignment.
- **Functions**:  
  - `Distrib_r(t)`: Truncated normal PDF for molecule radii.
  - `Alt(x)`: Finds the maximum value of the distribution for plotting.
  - `gen_and_interaction(N, por)`: Simulates molecule placement and checks for acceptance.
  - `F(t)`: Computes theoretical acceptance probability.

### Example Plots

- Truncated normal distribution for molecule radii.
- Histogram of accepted molecule radii with error bars.
- Theoretical acceptance probability curve.

### Notes

- The simulation assumes uniform distribution of molecule centers within the pore, corrected for polar coordinates.
- Error bars are computed using Poisson statistics.

---

Let me know if you’d like this tailored further, or if you want it as a `README.md` file!
