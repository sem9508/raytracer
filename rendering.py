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
        Sphere(Vec3(0, 0, -5), 1, Vec3(0, 0, 0), 100),

        Sphere(Vec3(0, 1.3, -5), 0.5, Vec3(255, 255, 255), 10),
        Sphere(Vec3(1, -0.7, -4.35), 0.5, Vec3(255, 255, 255), 10),
        Sphere(Vec3(-1, -0.7, -4.35), 0.5, Vec3(255, 255, 255), 10),
        Sphere(Vec3(0, -0.7, -5.65), 0.5, Vec3(255, 255, 255), 10),
    ]




    lights = [
        Light(Vec3(0, 10, -5), 1.2, Vec3(255, 250, 240)),
        Light(Vec3(-5, 5, -10), 0.8, Vec3(255, 200, 150)),
        Light(Vec3(5, 5, -10), 1, Vec3(150, 200, 255)),
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
                color += cast_ray(camera_origin, ray_direction, spheres, lights, depth)

            color /= samples
            image[y][x] = color
        if round(y*100/height) > last_percentage:
            last_percentage = round(y*100/height)
            print(f'{round(y*100/height)}%')
    return image
