import numpy as np
import math
from Vectorz import Vector_3D


class Force(object):

    def __init__(self, c):
        self.c = c
        #self.c.springMatrix = self.c.d_sled()
    # TODO: pe calculation
    #def pe(self):
    #    eps = 1.
    #    sig = 1.
    #
    #    dx = self.c.dx()
    #    dy = self.c.dy()
    #    dz = self.c.dz()
    #    dr2 = self.c.dr2()
    #
    #    r_mag = (dx ** 2 + dy ** 2 + dz ** 2)
    #    r_mag = np.nan_to_num(r_mag)
    #
    #    rgBuild = (4 * eps) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
    #    rgBuild = np.nan_to_num(rgBuild)
    #    #print "rgBuild:"
    #    #print np.sum(rgBuild)
    #    #print "-------------------"
    #    return np.sum(rgBuild)

    # TODO: ke calculation
    #def ke(self):
    #    d = 2.
    #    N = np.size(self.c.x)
    #    vx = self.c.vx.copy()
    #    vy = self.c.vy.copy()
    #    vz = self.c.vz.copy()
    #    return 1 / ((N - 1) * d) * sum(vx ** 2 + vy ** 2 + vz ** 2)

    # TODO: pressure calculation
    #def pressure(self):
    #    ps = 1.
    #    sig = 1.
    #    eps = 1.
    #    d = 2.
    #    N = np.size(self.c.x)
    #
    #    dx = self.c.dx()
    #    dy = self.c.dy()
    #    dz = self.c.dz()
    #    dr2 = self.c.dr2()
    #
    #    r_mag = (dx ** 2 + dy ** 2 + dz ** 2)
    #    r_mag = np.nan_to_num(r_mag)
    #
    #    px = dx * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
    #    px = np.nan_to_num(px)
    #    px = np.triu(px)
    #    py = dy * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
    #    py = np.nan_to_num(py)
    #    py = np.triu(py)
    #    pz = dz * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
    #    pz = np.nan_to_num(pz)
    #    pz = np.triu(pz)
    #    pt = px + py + pz
    #    return 1 / (d * N * self.ke()) * np.sum(pt)

	# acceleration due to Lennard-Jones forces
    def aLJ(self, eps=1., sig=1.):

        d = self.c.d()
        m = self.c.m.copy()

        dr = self.c.dr()

        r_hat = d / dr

        f = r_hat * (24 * eps) / dr * (2 * (sig / dr) ** 12 - (sig / dr) ** 6)
        f = self.c.vRmNan(f)

        #print "aLJ: "
        #print np.sum(f, axis=1) / m
        return np.sum(f, axis=1) / m
        
    # acceleration due to pulling force
    # do we need to pass in the time? where is it located?
    # need to keep track of initial position (xInit) somewhere 

    def aX(self, t):
        p = self.c.p[-1]  # only want the cFloorth index :/
        #x = p[cFloor].x

        #print "aX: "
        #print str(Vector_3D(10 * (0.1 * t - (p.x - self.c.xInit)), 0., 0.))
        return Vector_3D(100 * (0.1 * t - (p.x - self.c.xInit)), 0., 0.)
    	
    # acceleration due to dragging force

    def aD(self):
        p = self.c.p[self.c.cFloor] # only want the cFloorth index :/
        x = p.x
        y = p.y
        v = self.c.v[self.c.cFloor]
        dr = p.magnitude()  # TODO I have no idea what this dr is supposed to be

        #print "aD:"
        #print Vector_3D(-10 * (v.x * x + v.y * y) / dr, 0., 0.)
        return Vector_3D(-10 * (v.x * x + v.y * y) / dr, 0., 0.)  # divide by mass as well here

    # acceleration due to spring force
    def aS(self, a=2 ** (1 / 6.)):
        #tempa = (self.c.d_sled() - Vector_3D(2 * a, 2 * a, 0.)) * -500
        tempa = (self.c.d_sled() - self.c.springMatrix) * -500
        tempa = tempa * self.c.sledMatrix
        #print "aS:"
        #print np.sum(tempa, axis=1) / self.c.m[self.c.cFloor:]
        return np.sum(tempa, axis=1) / self.c.m[self.c.cFloor:]

    def a(self, t):
        # TODO: add up all forces and return new accelerations
        a = np.zeros(self.c.cFloor + self.c.cSled)

        a = self.aLJ() + a

        a[self.c.cFloor] += self.aD()

        a[-1] += self.aX(t)

        a[self.c.cFloor:] += self.aS()

        a[:self.c.cFloor] = Vector_3D(0., 0., 0.)
        return a



	

