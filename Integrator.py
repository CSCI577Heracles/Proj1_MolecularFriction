import numpy as np


class Integrator(object):

    def __init__(self, dt, f):
        self.dt = dt
        self.f = f
        self.f.c.a = f.a()
        #self.f.c.ax = f.ax()
        #self.f.c.ay = f.ay()
        #self.f.c.az = f.az()

    def integrate(self):
        #print "vx"
        #print self.f.c.vx

        #print "vy"
        #print self.f.c.vy

        #print "vz"
        #print self.f.c.vz
        self.f.c.p = self.f.c.p + self.f.c.v * self.dt + self.f.c.a * 0.5 * self.dt ** 2

        a_n = self.f.c.a.copy()
        #ax_n = self.f.c.ax
        #ay_n = self.f.c.ay
        #az_n = self.f.c.az

        self.f.c.a = self.f.a()
        #self.f.c.ax = self.f.ax()
        #self.f.c.ay = self.f.ay()
        #self.f.c.az = self.f.az()

        self.f.c.v += (a_n + self.f.c.a) * self.dt * 0.5
        #self.f.c.vx += 0.5 * (ax_n + self.f.c.ax) * self.dt
        #self.f.c.vy += 0.5 * (ay_n + self.f.c.ay) * self.dt
        #self.f.c.vz += 0.5 * (az_n + self.f.c.az) * self.dt

