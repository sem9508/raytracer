from vector import *
from sphere import *
from light import *
from utils import *
from floor import *

def cast_ray(ray_origin, ray_direction, spheres, lights, depth):
    if depth <= 0:
        return Vec3(0, 0, 0)
    
    closest_sphere = None
    closest_t = float('inf')

    for sphere in spheres:
        hit, t = sphere.intersect(ray_origin, ray_direction)
        if hit:
            if 0 < t < closest_t:
                closest_t = t
                closest_sphere = sphere

    if closest_sphere is None:
        if ray_direction.y < 0:
            return calc_floor(ray_origin, ray_direction, lights)
        return Vec3(0, 0, 0)

    closest_intersection = ray_origin + ray_direction * closest_t
    normal_vector = (closest_intersection - closest_sphere.center).normalize()

    ambient = 0.2
    color = closest_sphere.color * ambient

    for light in lights:
        light_direction = (light.position - closest_intersection).normalize()
        light_distance = (light.position - closest_intersection).length()

        shadow_blocked = False
        for sphere in spheres:
            light_blockage, t = sphere.intersect(closest_intersection, light_direction)
            if light_blockage and 0 < t < light_distance:
                shadow_blocked = True
                break

        if not shadow_blocked:
            light_intensity = max(0, normal_vector * light_direction) * light.intensity
            color += closest_sphere.color * light_intensity

            light_reflection_direction = calc_reflection(normal_vector, light_direction)
            view_direction = ray_direction.normalize()

            specular_intensity = max(0, light_reflection_direction * view_direction) ** closest_sphere.shininess
            color += light.color * specular_intensity * 0.8

    reflection_direction = calc_reflection(normal_vector, ray_direction)
    reflection_color = cast_ray(closest_intersection, reflection_direction, spheres, lights, depth - 1) * (closest_sphere.shininess / 100)

    color += reflection_color * 0.5

    return color
