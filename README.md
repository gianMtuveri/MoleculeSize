# MoleculeSize: Circular Molecules in a Circular Pore with Truncated Normal Radii

This project simulates the interaction between circular molecules and a circular pore, using a **Monte Carlo** approach. The radii of the molecules are drawn from a truncated normal distribution. The simulation evaluates which molecules fit inside the pore based on their position and size, then visualizes the accepted configurations and their probability distribution. The experimental probability is compared with the analytical function.

---

## Features

- **Truncated Normal Distribution:** Molecule radii are generated from a truncated normal distribution with user-defined mean and standard deviation.
- **Monte Carlo Sampling:** Randomly generates molecule positions and sizes, tests for acceptance in a circular pore.
- **Visualizations:**  
  - The distribution of generated radii  
  - Molecules sampled and accepted  
  - Histogram of accepted radii (normalized), with Poisson error bars  
  - Theoretical acceptance probability for comparison
- **Statistical Analysis:** Probability of acceptance is measured and compared against theoretical predictions.

---

## How It Works

1. **Molecule Generation:**  
   - Each molecule is assigned a radius from a truncated normal distribution.
   - The center of each molecule is uniformly distributed within the pore by using polar coordinates.

2. **Acceptance Test:**  
   - A molecule is accepted if it fits entirely inside the pore (its center plus radius does not exceed the pore radius).

3. **Visualization:**  
   - The simulation visualizes both the distribution of radii and the spatial distribution of molecules.
   - Accepted radii are binned and plotted in a normalized histogram with error bars.
   - The theoretical probability function is plotted for reference.

---

## Usage

### Requirements

- Python 3
- numpy
- scipy
- matplotlib

### Running the Simulation

1. Clone or download this repository.
2. Install dependencies if needed:
   ```bash
   pip install numpy scipy matplotlib
   ```
3. Run the main script:
   ```bash
   python truncated_normal_circular_pore.py
   ```
4. Outputs:
   - `Distr_truncnorm_st.png`: The truncated normal distribution used for molecule radii
   - Histogram and comparison plot (displayed at runtime)

---

## Parameters

- `mu`, `sigma`: Mean and standard deviation for the normal distribution of radii
- `N`: Number of Monte Carlo samples
- `nbins`: Number of bins for the histogram
- `pore.radius`: Radius of the circular pore

You can modify these parameters at the top of the script.

---

## Output

- Visualization of the truncated normal distribution for radii
- Visualization of accepted molecule radii in histogram form, with error bars
- Comparison with theoretical acceptance probability

---

## References

- Monte Carlo methods for physical simulations
- Probability theory for truncated normal distributions

---

## License

This project is licensed under the [GNU General Public License (GPL)](https://www.gnu.org/licenses/gpl-3.0.html).
