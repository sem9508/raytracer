import math

class Sphere:
    def __init__(self, center, radius, color, shininess):
        self.center = center
        self.radius = radius
        self.color = color
        self.shininess = shininess

    def intersect(self, ray_origin, ray_direction):
        oc = ray_origin - self.center
        a = ray_direction * ray_direction
        b = 2.0 * (oc * ray_direction)
        c = (oc * oc) - self.radius ** 2
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return False, float('inf')
        else:
            t1 = (-b - math.sqrt(discriminant)) / (2 * a)
            t2 = (-b + math.sqrt(discriminant)) / (2 * a)
            return True, min(t1, t2)