from hittable_list import HittableList
from vec3 import Point3, Vec3, Color, random_in_unit_sphere
from ray import Ray
from hittable import HitRecord

from color import write_color

from sphere import Sphere
from camera import Camera
from random import random
from tqdm import trange


def ray_color(r, world, depth):
    rec = HitRecord()

    if depth <= 0:
        return Color(0, 0, 0)

    if world.hit(r, 0, float("inf"), rec):
        target = rec.p + rec.normal + random_in_unit_sphere()
        return 0.5 * ray_color(Ray(rec.p, target - rec.p), world, depth - 1)
    unit_direction = r.direction.unit_vector()
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)


def main():

    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 25
    max_depth = 12

    # World
    objects = []
    objects.append(Sphere(Point3(0, 0, -1), 0.5))
    objects.append(Sphere(Point3(0, -100.5, -1), 100))
    world = HittableList(objects)

    # Camera
    cam = Camera()

    # Render
    image = f"P3\n{image_width} {image_height}\n255\n"

    for j in trange(image_height):
        # print(f"Scanlines remaining: {image_height-j}")
        for i in range(image_width):

            pixel_color = Color(0, 0, 0)

            for s in range(samples_per_pixel):

                u = (i + random()) / (image_width - 1)
                v = 1 - (j + random()) / (image_height - 1)

                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, world, max_depth)

            image += write_color(pixel_color, samples_per_pixel)

    with open("image.ppm", "w") as f:
        f.write(image)

    print(f"\nDone.\n{image_width}x{image_height}\n")


if __name__ == "__main__":
    main()
