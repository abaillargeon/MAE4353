import numpy as np
from spring_class import *

d = 2.5 #mm
OD = 31 #mm
G = 81e9 #GPa
Nt = 14
alpha = 0.5

Na = Nt - 1
D = OD - d
b = spring()
b.G = G
b._init_material(2211,0.145)

F_solid = b.find_F(d,D)
k = b.scale(d/1000,D/1000,Na)
l_min = F_solid/k + d/1000*Nt

print 'Free length: ' + str(l_min) + ' m'

print 'Force to compress: ' + str(F_solid) + ' N'

print 'Spring rate: ' + str(k) + ' N/m'

print 'Critical length (buckling) ' + str(2.63*(D/1000)/alpha) + ' m'

#D = b.find_D(0.071, 20*1.15)
#b.find_active_turns(0.071, D, 10)
