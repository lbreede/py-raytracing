from math import sqrt
from random import uniform


class Vec3:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (float, int)):
            return self.__class__(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if isinstance(other, type(self)):
            return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (float, int)):
            return self.__class__(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if isinstance(other, type(self)):
            return self.__class__(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (float, int)):
            return self.__class__(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        if isinstance(other, type(self)):
            return self.__class__(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (float, int)):
            return self.__class__(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            return self * (1 / other)

    def length(self):
        return sqrt(self.length_squared())

    def length_squared(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vec3(x, y, z)

    def unit_vector(self):
        return self / self.length()


def random_in_unit_sphere():
    while True:
        p = Vec3(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1))
        if p.length_squared() >= 1:
            continue
        return p


Point3 = Vec3
Color = Vec3
