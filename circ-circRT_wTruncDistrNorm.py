# This script simulates the interaction between circular molecules (class Circ) and 
# a circular pore (class Circonf), using a truncated normal distribution to generate
# molecule radii. It evaluates which molecules fit inside the pore based on their
# position and size, then visualizes the accepted configurations and their probability 
# distribution. The probability function is compared with the analytical function F.

from scipy.stats import truncnorm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import random, math

# Class for the circular pore
class Pore:
    def __init__(self, radius):
        self.radius = radius        

# Class for circular molecules; radius and center coordinates
class Molecule:
    def __init__(self):
        j = 0
        while j == 0:
            x = random.uniform(0, A)
            y = random.uniform(0, B)
            if y <= radius_distribution(x):
                self.radius = x
                plt.plot(x, y, 'bo')
                j = 1
            else:
                plt.plot(x, y, 'ro')
        # Generate random polar center coordinates, uniform in the pore area
        q = random.uniform(0, pore.radius ** 2 / 2)
        self.rho = math.sqrt(2 * q)
        self.theta = random.uniform(0, 2 * math.pi)

# Truncated normal PDF for radius
def radius_distribution(t):
    return truncnorm.pdf(t, a=-mu/sigma, b=(pore.radius-mu)/sigma, loc=mu, scale=sigma)

# Maximum height of the radius distribution
def max_height(x):
    y_max = 0
    for xi in x:
        y = radius_distribution(xi)
        if y_max < y:
            y_max = y
    return y_max

# Generate molecules and check pore-molecule interaction (contact)
def generate_and_check(N, pore):
    accepted_radii = []
    for i in range(N):
        if i == N // 4: print("25%")
        elif i == N // 2: print("50%")
        elif i == (N * 3) // 4: print("75%")
        mol = Molecule()
        if mol.rho + mol.radius < pore.radius:
            accepted_radii.append(mol.radius)
            # To plot accepted positions on circular pore, use:
            # plt.plot(mol.rho * math.cos(mol.theta), mol.rho * math.sin(mol.theta), 'bo')
        else:
            # To plot rejected positions on circular pore, use:
            # plt.plot(mol.rho * math.cos(mol.theta), mol.rho * math.sin(mol.theta), 'ro')
            pass
    return accepted_radii

# Theoretical function: probability of acceptance for a given radius
def F(t):
    Deltar = radius_distribution(t)
    P = (pore.radius - t) ** 2 / (pore.radius ** 2)
    return P * Deltar

N = 1000            # Number of configurations tested    
nbins = 50          # Number of bins for the histogram

pore = Pore(10)     # Initialize the circular pore

# Set up parameters for the truncated normal
mu = 6
sigma = 1.5

A = mu + 5 * sigma   # Width of the rectangle for the radius range (covering >99% of prob.)
sup = math.floor(A) + 1
x_range = np.linspace(-2, sup, 10000)
B = max_height(x_range) * 4 / 3  # Max y value for the rectangle

##### Plot truncated normal distribution ##############################
fig, ax = plt.subplots(figsize=(10, 10))
rect = Rectangle((0, 0), A, B, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(rect)
plt.plot(x_range, radius_distribution(x_range), color='black')
plt.grid(axis='both')
plt.savefig('Distr_truncnorm_st.png')
plt.show()
######################################################################

# Generate and check molecules in pore
accepted_radii = generate_and_check(N, pore)  # List of radii of accepted configurations

# Histogram weights
c1 = np.ones(len(accepted_radii)) / N / (pore.radius / nbins) 

# Plot histogram of accepted radii
fig, ax = plt.subplots(figsize=(10, 10))
counts, bins, patches = ax.hist(
    accepted_radii, bins=nbins, range=(0, pore.radius), weights=c1,
    facecolor='none', edgecolor='gray'
)

# Compute bin centers and Poissonian error bars
bin_x_centers = 0.5 * np.diff(bins) + bins[:-1]
error = np.zeros(nbins)
for i in range(nbins):
    error[i] = math.sqrt(counts[i] / N)
plt.errorbar(x=bin_x_centers, y=counts, yerr=error, fmt='none')

# Plot details
plt.ylabel('F(r) [A$^{-1}$]', fontsize=15)
plt.xlabel('r [A]', fontsize=15)

ra = np.arange(0, pore.radius + 0.2, 0.1)
plt.plot(ra, F(ra), label='Theory')
plt.legend()
plt.show()
