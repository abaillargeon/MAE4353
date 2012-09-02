import math
import numpy as np
from fatigue_class import *
from scipy.optimize import newton
import matplotlib.pyplot as plt

def f(t,x,y):
    return np.exp(-t) * np.cos(2*np.pi*t)


#print f(10)   
    
t1 = np.arange(0.0, 5.0, .01)
a = 1
b = 1
#print t1**2

plt.plot(t1, f(t1,a,b), 'bo')


plt.show()












