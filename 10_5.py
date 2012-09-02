import numpy as np
from spring_class import *

d = 0.2 #in
D = 2.0 #in
G = 11.2e6 #GPa
Nt = 12
alpha = 0.5
L_free = 5 #in

Na = Nt - 2

b = spring()
b.G = G
b._init_material(147,0.187)

L_solid = d*(Nt+1)
k = b.scale(d,D,Na)
F_solid = k * (L_free - L_solid)
N_safety = 0.50*b.stress_ultimate(d)*1000/b.corrected_shear_stress(F_solid, d, D)

print 'Solid length: ' + str(L_solid) + ' in'

print 'Force to compress: ' + str(F_solid) + ' lbf'

print 'Safety factor at solid length: ' + str(N_safety) + ' '
