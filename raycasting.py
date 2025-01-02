from vector import *
from sphere import *
from light import *
from utils import *
from floor import *

def cast_ray(ray_origin, ray_direction, spheres, lights, depth):
    if depth <= 0:
        return Vec3(0, 0, 0)
    
    
    closest_t = float('inf')
    hit_sphere = None

    for sphere in spheres:
        hit, t = sphere.intersect(ray_origin, ray_direction)
        if hit and t < closest_t:
            closest_t = t
            hit_sphere = sphere

    if hit_sphere is None:
        if ray_direction.y < 0:
            return calc_floor(ray_origin, ray_direction)
        return Vec3(50, 70, 180)

    hit_point = ray_origin + ray_direction * closest_t
    normal = (hit_point - hit_sphere.center).normalize()

    ambient = 0.1
    final_color = hit_sphere.color * ambient

    for light in lights:
        light_distance = (light.position - hit_point).length()
        in_shadow = False
        light_dir = (light.position - hit_point).normalize()
        for sphere in spheres:
            blocked, t = sphere.intersect(hit_point, light_dir)
            if blocked and 0 < t < light_distance:
                in_shadow = True

        if in_shadow:
            light_intensity = 0
        else:
            light_intensity = max(0, normal * light_dir) * light.intensity

        final_color += hit_sphere.color * light_intensity

    reflection_direction = calc_reflection(normal, ray_direction)
    reflection_color = cast_ray(hit_point, reflection_direction, spheres, lights, depth-1)
    final_color += reflection_color
    
    return final_color

def cast_ray2(ray_origin, ray_direction, spheres, lights, depth):
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
    reflection_color = cast_ray2(closest_intersection, reflection_direction, spheres, lights, depth - 1) * (closest_sphere.shininess / 100)

    color += reflection_color * 0.5

    return color
