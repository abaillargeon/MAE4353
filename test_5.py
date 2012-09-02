import numpy as np
from spring_class import *

d = [0.063, 0.067, 0.071, 0.075, 0.080, 0.085, 0.090, 0.095] #in
G = 11.75e6 #psi
Ne = 2
F_min = 10 #lbf

L_free = 1.5 + 3.0/8 #in


b = spring()
b.G = G
b._init_material(201,0.145)

for i in range(len(d)):
    D = 7.0/16 + 0.05 + d[i] #in
    k = F_min / (3.0/8)
    Na = b.find_active_turns(d[i], D, k)
    Nt = Na + Ne
    L_solid = d[i]*Nt
    F_solid = k * (L_free - L_solid)

    #k = b.scale(d,D,Na)
    
    N_safety = 0.50*b.stress_ultimate(d[i])*1000/b.corrected_shear_stress(F_min, d[i], D)
    N_service = 0.50*b.stress_ultimate(d[i])*1000/b.corrected_shear_stress(F_solid, d[i], D)
    Vol = b.material_volume(d[i], D, Nt)
    print '------- d: ' + str(d[i]) + ' -------'
    print 'D: ' + str(D)
    print 'C: ' + str(D/d[i]) + ''
    print 'k: ' + str(k)
    print 'L solid: ' + str(L_solid)
    print 'Na: ' + str(Na) + ' '
    print 'Nt: ' + str(Nt) + ' '
    print 'Solid safety factor: ' + str(N_safety) + ' '
    print 'Service safety factor: ' + str(N_service) + ' '
    print 'Volume: ' + str(Vol)
    print 'Pitch: ' + str((L_free - 2*d[i])/Na)
