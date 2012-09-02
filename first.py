from bolt_group_class import *
import numpy as np


a = bolt_group()

a.add_bolt([-75,60],  144)
a.add_bolt([-75,-60], 144)
a.add_bolt([75,60],   144)
a.add_bolt([75,-60], 144)

a.add_force([0,-16],[425,60])
T = a.torque()

print a.total_shear_forces(T)
#b=np.array(a.bolts)
#print b[0]+b[0]
