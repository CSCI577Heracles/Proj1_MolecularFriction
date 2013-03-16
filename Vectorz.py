import math
import numpy as np


class Vector_3D:

    def __class__(self):
        return Vector_3D

    def __init__(self, initial_x, initial_y, initial_z):
        self.x = initial_x
        self.y = initial_y
        self.z = initial_z

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z) + " | "

    def __mul__(self, other):
        if isinstance(other, Vector_3D):
            x_product = self.x * other.x
            y_product = self.y * other.y
            z_product = self.z * other.z
            return Vector_3D(x_product, y_product, z_product)
        elif isinstance(other, int) or isinstance(other, float):
        #else:
            x_product = self.x*other
            y_product = self.y*other
            z_product = self.z*other
            return Vector_3D(x_product, y_product, z_product)

    def __floordiv__(self, other):   # overload // operator to return sum of squares of (Vector1 - Vector2)
    #power = vector_tuple[1]
        #vector = vector_tuple[0]
        #return self.magnitude_of_dist(self-vector, power)
        #return self.magnitude_of_dist(self-other)
        return self.magnitude_of_dist(self-other)

    def __mod__(self, other):
        if other.x == 0:
            x_mod = self.x
        else:
            x_mod = self.x % other.x

        if other.y == 0:
            y_mod = self.y
        else:
            y_mod = self.y % other.y

        if other.z == 0:
            z_mod = self.z
        else:
            z_mod = self.z % other.z
        return Vector_3D(x_mod, y_mod, z_mod)

    def __add__(self, other):
        if isinstance(other, Vector_3D):
            return Vector_3D(self.x+other.x, self.y+other.y, self.z+other.z)
        else:
            return Vector_3D(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if isinstance(other, Vector_3D):
            x_sub = self.x - other.x
            y_sub = self.y - other.y
            z_sub = self.z - other.z
            return Vector_3D(x_sub, y_sub, z_sub)
        else:
            return Vector_3D(self.x - other, self.y - other, self.z - other)

    def __neg__(self):
        return Vector_3D(-self.x, -self.y, -self.z)

    def __div__(self, other):
        if isinstance(other, Vector_3D):
            x_div = float(self.x) / other.x
            y_div = float(self.y) / other.y
            z_div = float(self.z) / other.z
            return Vector_3D(x_div, y_div, z_div)
        #elif isinstance(other, int) or isinstance(other, float):
        else:
            x_div = np.float64(self.x) / other
            y_div = np.float64(self.y) / other
            z_div = np.float64(self.z) / other
            return Vector_3D(x_div, y_div, z_div)

    def __pow__(self, power):
        pow_x = self.x ** power
        pow_y = self.y ** power
        pow_z = self.z ** power
        return Vector_3D(pow_x, pow_y, pow_z)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def raw_mag(self, r):
        return r.x ** 2 + r.y ** 2 + r.z ** 2

