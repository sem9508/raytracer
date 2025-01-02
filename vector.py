import math

class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vec3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, scalar):
        return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        length = self.length()
        return self / length

    def __repr__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"