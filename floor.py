from vector import *

def calc_floor(ray_origin, ray_direction, lights):
    t = (-10 - ray_origin.y) / ray_direction.y
    if t <= 0:
        return Vec3(0, 0, 0)
    
    x = ray_origin.x + ray_direction.x * t
    y = 0
    z = ray_origin.z + ray_direction.z * t
    square_size = 6

    if (int(x / square_size) + int(z / square_size)) % 2 == 0:
        if x < 0:
            base_color = Vec3(255, 255, 255)
        else:
            base_color = Vec3(0, 0, 0)

    else:
        if x < 0:
            base_color = Vec3(0, 0, 0)
        else:
            base_color = Vec3(255, 255, 255)
    # Ambient light
    ambient_intensity = 0.2
    color = base_color * ambient_intensity

    # Calculate light interaction
    for light in lights:
        light_direction = (light.position - Vec3(x, y, z)).normalize()
        floor_normal = Vec3(0, 1, 0)
        light_intensity = max(0, floor_normal * light_direction) * light.intensity

        color += base_color * light_intensity

    return color
