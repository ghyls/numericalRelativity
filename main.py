
import numpy as np
from numpy import pi, sin
import sympy as sp

# PROBLEMA UNIDIMENSIONAL

class StellarObject:
    def __init__(self, mass):
        self.mass = mass
    

Sun = StellarObject(2 * 10**33) #g
BH = StellarObject(30*Sun.mass)
G = 6.67408e-11
c = 3e8

# =============================================================================
# MALLADO ESPACIOTEMPORAL
# =============================================================================
t0 = 0
tf = 10 
r0 = 0
rf = tf

npasos = 10000

r = np.linspace(r0, rf, npasos)
theta = 0
t = np.linspace(t0, tf, npasos)


# =============================================================================
# VAIABLES GLOBALES
# =============================================================================

# ENERGÍA
# =============================================================================

Delta = 0   #cte cosmologica
d = 4       #num. dimensiones
R = 10e4    #traza del tensor de Ricci
M = BH.mass

gSh = [[-(1-2*G*M/(r*c**2)), 0, 0, 0], [0, 1./(1-2*G*M/(r*c**2)), 0, 0], \
        [0, 0, r**2, 0], [0, 0, 0, r**2*sin(theta**2)]]
gamma_ij = gSh[1:][1:]     #la métrica espacial


lapse = 1
shift = gSh[0][1:]  


#K_ij = 1./(2*lapse)*(\partial_t(gamma_ij) + D_i(shift_j) + D_j(shift_i))

R = 8 * pi * BH.mass
Chi = np.linalg.det(gamma_ij)**(-1./(d-1)) #TODO: define el determinante!


A = K_ij-1./(d-1)*gamma_ij*np.trace(K)
Asim = Chi*A

#H =  R + (d-2)/(d-1)*tr(K)**2 - Asim_[m][n] * Asim^[m][n] - 16 * pi * rho - 2 * Delta

# MOMENTO
# =============================================================================
gammaSim_mn = Chi*gamma_ij

#P_i = gammaSim_mn * 

