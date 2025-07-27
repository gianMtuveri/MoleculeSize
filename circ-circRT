import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random, math

# Class for the circular pore
class Pore:
    def __init__(self, radius):
        self.radius = radius

# Class for the circular molecule
class Molecule:
    def __init__(self, r_min, r_max, pore_radius):
        self.radius = random.uniform(r_min, r_max)
        # Use polar coordinates, modify rho distribution for uniform center distribution
        q = random.uniform(0, pore_radius**2 / 2)
        self.rho = math.sqrt(2 * q)
        self.theta = random.uniform(0, 2 * math.pi)

# Generate molecules and check molecule-pore interaction (contact)
def generate_and_check(N, pore, r_min, r_max, ax=None):
    accepted_radii = []
    for i in range(N):
        if i == N // 4: print("25%")
        elif i == N // 2: print("50%")
        elif i == (N * 3) // 4: print("75%")
        mol = Molecule(r_min, r_max, pore.radius)
        x = mol.rho * math.cos(mol.theta)
        y = mol.rho * math.sin(mol.theta)
        color = 'blue' if (mol.rho + mol.radius < pore.radius) else 'red'
        if ax is not None:
            ax.plot(x, y, 'o', color=color, markersize=2)
            # To see the actual molecule circles, uncomment:
            # circ = Circle((x, y), mol.radius, edgecolor=color, facecolor='none', linewidth=0.5, alpha=0.4)
            # ax.add_patch(circ)
        if mol.rho + mol.radius < pore.radius:
            accepted_radii.append(mol.radius)
    return accepted_radii

# Theoretical function representing the probability of accepting a given configuration
def theoretical_probability(t, pore_radius, a, b, nbins):
    bin_width = (b - a) / nbins
    prob_r = 1 / (b - a)
    return ((pore_radius - t) ** 2) / (pore_radius ** 2) * prob_r * bin_width

a = 8                # Minimum radius for molecule
b = 12               # Maximum radius for molecule
N = 10000            # Number of tested configurations
nbins = 20           # Number of bins for the histogram

pore = Pore(10)      # Initialize the circular pore

# Plot the pore and molecules
fig, ax = plt.subplots(figsize=(8, 8))
plt.gca().set_aspect('equal', adjustable='box')
pore_circle = Circle((0, 0), pore.radius, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(pore_circle)

accepted_radii = generate_and_check(N, pore, a, b, ax=ax)
plt.axis("off")
plt.savefig('Distr_rt_uni.png')
plt.show()

# Histogram is normalized by the total number of configurations
weights = np.ones(len(accepted_radii)) / N
fig, ax = plt.subplots(figsize=(8, 8))
counts, bins, patches = ax.hist(accepted_radii, bins=nbins, range=(a, b), weights=weights, facecolor='none', edgecolor='gray')

# Calculate bin centers for error bars
bin_centers = 0.5 * np.diff(bins) + bins[:-1]
# Experimental error (Poissonian): sqrt(normalized count / N)
error = np.sqrt(counts / N)
plt.errorbar(x=bin_centers, y=counts, yerr=error, fmt='none', color='black')

plt.title('Probability Function', fontsize=20)
plt.ylabel('P', fontsize=15)
plt.xlabel('r [A]', fontsize=15)

ra = np.arange(a, b + 0.1, 0.1)
plt.plot(ra, theoretical_probability(ra, pore.radius, a, b, nbins), label='Theory')
plt.legend()
plt.show()
