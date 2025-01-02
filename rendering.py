import random

from vector import *
from sphere import *
from light import *
from utils import *
from floor import *
from raycasting import *

def render(width, height):
    width, height = width, height
    aspect_ratio = width / height
    fov = math.pi / 3.0
    samples = 4
    depth = 20
    camera_origin = Vec3(0, 0, 0)

    spheres = [
        Sphere(Vec3(0, -1.5, -10), 2.5, Vec3(100, 100, 255), 80),
        Sphere(Vec3(-4, -1, -12), 1.5, Vec3(255, 0, 0), 20),
        Sphere(Vec3(3, 0, -8), 1, Vec3(0, 255, 0), 30),
        Sphere(Vec3(-1.5, 1, -6), 0.75, Vec3(255, 255, 0), 50),
        Sphere(Vec3(1.5, 1.5, -9), 1.25, Vec3(255, 165, 0), 40),
        Sphere(Vec3(-3, -0.5, -7), 1, Vec3(75, 0, 130), 10),
        Sphere(Vec3(0, -0.3, -4), 0.4, Vec3(0, 255, 255), 5),
        Sphere(Vec3(2.5, -1.2, -9), 0.5, Vec3(255, 20, 147), 60),
    ]

    lights = [
        Light(Vec3(0, 10, -5), 1.2, Vec3(255, 250, 240)),
        Light(Vec3(-10, 5, -10), 0.8, Vec3(255, 200, 150)),
        Light(Vec3(10, 10, -15), 1, Vec3(150, 200, 255)),
    ]

    
    image = [[Vec3() for _ in range(width)] for _ in range(height)]
    last_percentage = 0

    for y in range(height):
        for x in range(width):
            color = Vec3(0, 0, 0)

            for _ in range(samples):
                dx = random.uniform(-0.5, 0.5)
                dy = random.uniform(-0.5, 0.5)
                px = (2 * (x + 0.5 + dx) / width - 1) * math.tan(fov / 2) * aspect_ratio
                py = (1 - 2 * (y + 0.5 + dy) / height) * math.tan(fov / 2)
                
                ray_direction = Vec3(px, py, -1).normalize()
                color += cast_ray2(camera_origin, ray_direction, spheres, lights, depth)

            color /= samples
            image[y][x] = color
        if round(y*100/height) > last_percentage:
            last_percentage = round(y*100/height)
            print(f'{round(y*100/height)}%')
    return image
