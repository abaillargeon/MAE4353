import numpy as np
from spring_class import *

d = 0.080 #in
OD = 0.880
G = 11.5e6 #Pa
alpha = 0.5
Nt = 8

Na = Nt - 1
L_solid = d*Nt
D = OD - d
b = spring()
b.G = G
b._init_material(140,0.190)

F_solid = b.find_F(d,D)
k = b.scale(d,D,Na)
L_free = L_solid + F_solid/k

pitch = L_free / (Na+1)

print 'Solid-safe length: ' + str(L_free) + ' in'
print 'Pitch: ' + str(pitch) + ' in'
print 'Force to solid: ' + str(F_solid) + ' lbf'
print 'Spring rate: ' + str(k) + ' lbf/in'
print 'Critical length (buckling) ' + str(2.63*(D)/alpha) + ' in'