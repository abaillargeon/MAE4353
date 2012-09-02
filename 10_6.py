import numpy as np
from spring_class import *

d = 4.0 #mm
C = 10.0
G = 77.2e9 #Pa
alpha = 0.5
L_free = 80.0 #mm
F_test = 50.0 #N
d_test = 15.0 #mm

b = spring()
b.G = G
b._init_material(1855,0.187)

k = F_test/d_test*1000
D = d*C
D_hole = D + d
Nt = ((d/1000)**4*G)/(8*(D/1000)**3*k)

L_solid = d*(Nt+1)/1000
F_solid = k*(L_free/1000 - L_solid)
N_safety = 0.50*b.stress_ultimate(d)/b.corrected_shear_stress(F_solid, d, D)


print 'Spring rate: ' + str(k) + ' N/m'
print 'Hole diameter: ' + str(D_hole) + ' mm'
print 'Number of coils: ' + str(Nt) + ''
print 'Solid length: ' + str(L_solid) + ' m'
print 'Safety factor: ' + str(N_safety) + ' '