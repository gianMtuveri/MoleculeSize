# This script simulates the interaction between circular molecules (class Circ) and 
# a circular pore (class Circonf), using a truncated normal distribution to generate
# molecule radii. It evaluates which molecules fit inside the pore based on their
# position and size, then visualizes the accepted configurations and their probability 
# distribution. The probability function is compared with the analytical function F.

from scipy.stats import truncnorm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
import random,math

# Definition of the class for the rectangular pore; parameters: height and width
class Circonf:
    def __init__(self,radius):
        self.radius=radius        

# Definition of the class for circular molecules; parameters: radius and coordinates of the center
class Circ:
    def __init__(self):
        j=0
        while j==0:
            x=random.uniform(0,A)
            y=random.uniform(0,B)
            if (y<=Distrib_r(x)):
                self.radius=x
                plt.plot(x,y,'bo')
                j=1
            else:
                plt.plot(x,y,'ro')
        '''Note: I use polar coordinates, I modify the distribution of rho to make the distribution
        of centers uniform. I use the distribution of q as a support'''
        q=random.uniform(0,poro.radius**2/2)
        self.rho=math.sqrt(2*q)
        self.theta=random.uniform(0,2*math.pi)
        


# Truncated normal distribution
def Distrib_r(t):
    return truncnorm.pdf(t,a=-mu/sigma,b=-mu/sigma+poro.radius,loc=mu,scale=sigma)
    

# Height of the truncated normal distribution
def Alt(x):
    y_max=0
    for i in range(len(x)):
        if y_max<Distrib_r(x[i]): y_max=Distrib_r(x[i])
    return y_max
    
# Pore-molecule interaction (contact evaluation)
def gen_and_interaction(N,por):
    acc=[]
    for i in range (N):
        if (i==N/4):print("25%")
        elif (i==N/2):print("50%")
        elif (i==N/4*3):print("75%")
        mol=Circ()
        if (mol.rho+mol.radius<por.radius):
            acc.append(mol.radius)
            #plt.plot(mol.rho*math.cos(mol.theta*180/math.pi), mol.rho*math.sin(mol.theta*180/math.pi),'bo')
            '''circ=Circle((mol.radius,mol.value), 0.1, edgecolor='blue',facecolor='none')
            ax.add_patch(circ)'''
        else:
            #plt.plot(mol.rho*math.cos(mol.theta*180/math.pi), mol.rho*math.sin(mol.theta*180/math.pi),'bo')
            '''circ=Circle((mol.radius,mol.value), 0.1, edgecolor='red',facecolor='none')
            ax.add_patch(circ)'''
    return acc

# Theoretical function representing the probability of accepting a certain configuration (see last lines)
def F(t):
    Deltar=Distrib_r(t)  # Probability of having a certain radius within the distribution
    P=(poro.radius-t)**2/poro.radius**2  # Probability that a molecule with radius t is accepted
    return P * Deltar 



N=1000 # number of configurations tested    
nbins=50 # number of bins for the representation of c[] in a histogram



poro=Circonf(10) # Initialization of the circular pore


# The distribution of radii ###########################################
# Data for the radius distribution, as input only mu and sigma of the normal
# Data 1 and 2 for semiaxes 1 and 2 
mu=    6
sigma= 1.5



A=mu+5*sigma   # width of the integration rectangle (5 sigma, probability of a value greater > 1%)
sup=math.floor(A)+1 # used as upper limit for the definition of the distribution and 
                        # for integration along x

x_range = np.linspace(-2,sup,10000)  # Domain of the distribution
B=Alt(x_range)*4/3     # Maximum value of y in the integration
######################################################################


##### Plot truncated distribution ##############################
fig, ax = plt.subplots(figsize=(10,10))

#axes range and labels
#plt.xlim([-1, sup])
#plt.ylim([-0.02, B+0.02])

#add rectangle to plot##########
rect = Rectangle((0,0),A,B,linewidth=2,edgecolor='black',facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect)

plt.plot(x_range,Distrib_r(x_range),color='black')
plt.grid(axis='both')
#plt.savefig('Distr_truncnorm_st.png')





'''#define Matplotlib figure and axis######
fig, ax = plt.subplots(figsize=(10,10))

#axes range and labels
plt.xlim([-poro.radius-2, poro.radius+2])
plt.ylim([-poro.radius-2, poro.radius+2])
plt.gca().set_aspect('equal', adjustable='box')
ax.set_ylabel('pore height (direction y)')
ax.set_xlabel('pore width (direction x)')



#add rectangle to plot##########
cir = Circle((0,0),poro.radius,linewidth=1,
edgecolor='black',facecolor='none')

# Add the patch to the Axes
ax.add_patch(cir)
########################################'''



c=gen_and_interaction(N,poro) # List of radii of accepted configurations
plt.savefig('MCintegr.png')
plt.show()
######################################################################
# weights, the number of configurations contained in c is rescaled in a histogram 
# by the total number of configurations N
c1=np.ones(len(c))/N/(poro.radius/nbins) 

# I plot the next histogram, whose counts for each bin are renormalized by N
fig, ax = plt.subplots(figsize=(10,10))
'''
counts  = numpy.ndarray of count of data points for each bin/column in the histogram
bins    = numpy.ndarray of bin edge/range values
patches = a list of Patch objects.
        each Patch object contains a Rectangle object. 
        e.g. Rectangle(xy=(-2.51953, 0), width=0.501013, height=3, angle=0)

The histogram must be normalized by N, and each bar represents the available area for each radius,
multiplied by the probability of having that radius (extracted from uniform distribution).
Experimental error of the method: 1*counts**(-0.5) (Poissonian)
'''
counts, bins, patches= ax.hist(c,bins=nbins,range=(0,poro.radius),weights=c1,facecolor='none', edgecolor='gray') 

# Calculate the center of each bin to then plot the error bars
# each center is half the width of a bin plus the widths of the previous bins
bin_x_centers = 0.5 * np.diff(bins) + bins[:-1]
#print(bin_x_centers)

# Calculate the error of the method, then plot with errorbar
error=np.zeros(nbins)

# Absolute error: relative error for normalized counts of each column
# Relative error: Poissonian type, 1/(number of unnormalized counts^(-1))
for i in range(nbins): error[i]=math.sqrt(counts[i]/N)
plt.errorbar(x=bin_x_centers, y=counts, yerr=error, fmt='none') # plot error bars

# Plot details
#plt.title('Probability function', fontsize=20)
plt.ylabel('F(r)[A$^{-1}$]', fontsize=15)
plt.xlabel('r[A]', fontsize=15)

ra=np.arange(0,poro.radius+0.2,0.1)
plt.plot(ra,F(ra)) 
# I calculate and plot the probability function which is the product of:
# available area for each radius
# probability of obtaining a radius from the distribution
#plt.savefig('Funzione_prob.png')
plt.show()
