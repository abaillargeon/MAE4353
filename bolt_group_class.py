import numpy as np
import scipy as sp
class bolt_group:
    bolts = []
    centroid = [0,0]
    forces = []
    def add_bolt(self,coord,area):
        self.bolts.append([coord,area])
        self._eval_centroid()
    def clear_bolts(self):
        self.bolts = []
    def add_force(self,vector,applied):
        self.forces.append([vector,applied])
    def _eval_centroid(self):
        ax = ay = a = 0
        if len(self.bolts) == 0:
            return 0
        for i in range(len(self.bolts)):
            ax += self.bolts[i][0][0]*self.bolts[i][1]
            ay += self.bolts[i][0][1]*self.bolts[i][1]
            a += self.bolts[i][1]
        self.centroid[0] = ax*1.0/a
        self.centroid[1] = ay*1.0/a
    def torque(self):
        force_location = np.array(self.forces[0][1])
        force = np.array(self.forces[0][0])
        centroid = np.array(self.centroid)
        r = force_location - centroid #vector from centroid to force
        return np.cross(r,force) #r x F
    def total_shear_forces(self,torque):
        f_total = np.zeros((len(self.bolts),1))
        f = np.array(self.forces[0][0])/len(self.bolts)#find the force on each bolt
        r_sq = 0
        for i in range(len(self.bolts)):
            r_sq += (self.bolts[i][0][0]-self.centroid[0])**2 + (self.bolts[i][0][1]-self.centroid[1])**2
        if r_sq == 0:
            f_total[0] = np.linalg.norm(f)
            return f_total
        for i in range(len(self.bolts)):
            r = np.sqrt((self.bolts[i][0][0]-self.centroid[0])**2 + (self.bolts[i][0][1]-self.centroid[1])**2)
            f2mag = np.abs(torque*r/r_sq)
            if r > 0 :
                f2prime = f2mag*np.array([-1*(self.centroid[1]-self.bolts[i][0][1]),(self.centroid[0]-self.bolts[i][0][0])])/r
            else:
                f2prime = np.zeros(2)
            f_total[i] = np.linalg.norm(f+f2prime)
        return f_total