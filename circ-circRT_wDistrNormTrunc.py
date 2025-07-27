from scipy.stats import truncnorm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
import random,math

# Definizione della classe per il poro rettangolare; parametri altezza e larghezza
class Circonf:
    def __init__(self,radius):
        self.radius=radius        

# Definizione della classe per le molecole circlari; parametri raggio e coordinate del centro
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
        '''Nota: uso coordinate polari, modifico la distribuzione di rho per rendere la distrib
        dei centri uniforme. Uso distribuzione di q per appoggiarmi'''
        q=random.uniform(0,poro.radius**2/2)
        self.rho=math.sqrt(2*q)
        self.theta=random.uniform(0,2*math.pi)
        


# Distribuzione normale troncata
def Distrib_r(t):
    return truncnorm.pdf(t,a=-mu/sigma,b=-mu/sigma+poro.radius,loc=mu,scale=sigma)
    

# Altezza della distribuzione normale troncata
def Alt(x):
    y_max=0
    for i in range(len(x)):
        if y_max<Distrib_r(x[i]): y_max=Distrib_r(x[i])
    return y_max
    
# Interazione poro-molecola (valutazione del contatto)
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

# Funzione teorica rappresentante probabilità di accettare una certa configurazione (vedi ultime righe)
def F(t):
    Deltar=Distrib_r(t)  # Probabilità di avere un certo raggio dentro la distribuzione
    P=(poro.radius-t)**2/poro.radius**2  # Probabilità molecola accettata con raggio t
    return P * Deltar 



N=1000 # numero di configurazioni testate    
nbins=50 # numero di bin per la rappresentazione di c[] in un istogramma



poro=Circonf(10) # Inizializzazione del poro circolare


# La distribuzione dei raggi ###########################################
# Dati della distribuzione sui raggi, in input solo mu e sigma della normale
# Dati 1 e 2 per semiassi 1 e 2 
mu=    6
sigma= 1.5



A=mu+5*sigma   # larghezza del rettangolo di integrazione (5 sigma, probabilità valore maggiore > 1%)
sup=math.floor(A)+1 # uso come estremo superiore di definizione della distribuzione e 
                        # di integrazione lungo x

x_range = np.linspace(-2,sup,10000)  # Dominio della distribuzione
B=Alt(x_range)*4/3     # Valore massimo di y massimo nell'integrazione
######################################################################


##### Plot distribuzione troncata ##############################
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



c=gen_and_interaction(N,poro) # Lista dei raggi delle configurazioni accettate
plt.savefig('MCintegr.png')
plt.show()
######################################################################
# weights, il numero di configurazioni contanute in c è riscalato in un istogramma 
# per il numero totale di configurazioni N
c1=np.ones(len(c))/N/(poro.radius/nbins) 

# Plotto il prossimo istogramma, i cui conteggi per ciascun bin sono rinormalizzati per N
fig, ax = plt.subplots(figsize=(10,10))
'''
counts  = numpy.ndarray of count of data ponts for each bin/column in the histogram
bins    = numpy.ndarray of bin edge/range values
patches = a list of Patch objects.
        each Patch object contains a Rectnagle object. 
        e.g. Rectangle(xy=(-2.51953, 0), width=0.501013, height=3, angle=0)

L'istogramma è da normalizzare per N, e ciascuna barra rappresenta l'area disponibile per ogni raggio,
moltiplicato per la probabilità di avere quel raggio (estratto da distribuzione uniforme).
Errore sperimentale del metodo: 1*counts**(-0.5) (poissoniano)
'''
counts, bins, patches= ax.hist(c,bins=nbins,range=(0,poro.radius),weights=c1,facecolor='none', edgecolor='gray') 

# Calcolo il centro di ogni bin per poi plottare le barre d'errore
# ogni centro è la metà larghezza di un bin più le larghezze dei bin precedenti
bin_x_centers = 0.5 * np.diff(bins) + bins[:-1]
#print(bin_x_centers)

# Calcolo l'errore del metodo, poi plotto con errorbar
error=np.zeros(nbins)

# Errore assoluto: errore relativo per conteggi normalizzati di ogni colonna
# Errore relativo: di tipo poissoniano, 1/(numero di conteggi non normalizzati^(-1))
for i in range(nbins): error[i]=math.sqrt(counts[i]/N)
plt.errorbar(x=bin_x_centers, y=counts, yerr=error, fmt='none') # plot barre d'errore

# Dettagli del plot
#plt.title('Probability function', fontsize=20)
plt.ylabel('F(r)[A$^{-1}$]', fontsize=15)
plt.xlabel('r[A]', fontsize=15)

ra=np.arange(0,poro.radius+0.2,0.1)
plt.plot(ra,F(ra)) 
# Calcolo e plotto la funzione di probabilità prodotto di:
# area disponibile per ogni raggio
# probabilità di ottenere un raggio dalla distribuzione
#plt.savefig('Funzione_prob.png')
plt.show()
