import numpy as np
from Vectorz import Vector_3D
from math import sqrt


class Container(object):

    def __init__(self):
        self._p = np.array([])  # these are the particle locations
        self.v = np.array([])   # particle velocities
        self.a = np.array([])   # particle accelerations
        self.m = np.array([])   # particle masses
        self.L = Vector_3D(0., 0., 0.)
        self.vBounds = np.vectorize(self.enforceBoundary)
        self.vRmNan = np.vectorize(self.rmNan)
        self.vR_mag_calc = np.vectorize(self.r_mag_calc)

    def enforceBoundary(self, vector3d):
        if vector3d.x > self.L.x / 2.:
            vector3d.x -= self.L.x
        elif vector3d.x < - self.L.x / 2.:
            vector3d.x += self.L.x

        if vector3d.y > self.L.y / 2.:
            vector3d.y -= self.L.y
        elif vector3d.y < - self.L.y / 2.:
            vector3d.y += self.L.y

        if vector3d.z > self.L.z / 2.:
            vector3d.z -= self.L.z
        elif vector3d.z < - self.L.z / 2.:
            vector3d.z += self.L.z
        return vector3d

    def rmNan(self, vector3d):
        vector3d.x = np.nan_to_num(vector3d.x)
        vector3d.y = np.nan_to_num(vector3d.y)
        vector3d.z = np.nan_to_num(vector3d.z)
        return vector3d

    def r_mag_calc(self, vector3d):
        return sqrt(vector3d.x ** 2 + vector3d.y ** 2 + vector3d.z ** 2)


    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, p):
        self._p = p % self.L

    def add_particle(self, p, v, m):
        self.p = np.hstack((self.p, p))
        self.v = np.hstack((self.v, v))
        self.m = np.hstack((self.m, m))

    def d(self):  # return distance matrix
        ptemp = np.tile(self.p, (self.p.size, 1))
        return self.vBounds(ptemp - ptemp.T)

    def dr2(self):
        r_mag = self.dx() ** 2 + self.dy() ** 2 + self.dz() ** 2
        return np.nan_to_num(r_mag)

    def dr(self):
        return self.vR_mag_calc(self.d())
