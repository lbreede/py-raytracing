from tqdm import tqdm
from random import random

from utils.settings import ASPECT_RATIO
from utils.sphere import Sphere
from utils.vec3 import Point3
from utils.vec3 import Color
from utils.vec3 import random_in_hemisphere
from utils.hittable_list import HittableList
from utils.camera import Camera
from utils.hittable import HitRecord
from utils.color import write_color
from utils.ray import Ray


def ray_color(r, world, depth):
    rec = HitRecord()

    if depth <= 0:
        return Color(0, 0, 0)

    if world.hit(r, 0.001, float("inf"), rec):
        target = rec.p + random_in_hemisphere(rec.normal)
        return 0.5 * ray_color(Ray(rec.p, target - rec.p), world, depth - 1)

    unit_direction = r.direction.unit_vector()
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)


def main():

    # Image
    image_width = 480
    image_height = int(image_width / ASPECT_RATIO)
    samples_per_pixel = 4
    max_depth = 2

    # World
    objects = []
    objects.append(Sphere(Point3(0, 0, -1), 0.5))
    objects.append(Sphere(Point3(0, -100.5, -1), 100))
    world = HittableList(objects)

    # Camera
    cam = Camera()

    # Render
    image = f"P3\n{image_width} {image_height}\n255\n"

    for j in tqdm(range(image_height), desc="Scanlines"):
        for i in range(image_width):

            pixel_color = Color(0, 0, 0)

            for s in range(samples_per_pixel):

                u = (i + random()) / (image_width - 1)
                v = 1 - (j + random()) / (image_height - 1)

                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, world, max_depth)

            image += write_color(pixel_color, samples_per_pixel)

    with open(f"image.ppm", "w") as f:
        f.write(image)

    print(f"\nDone.\n{image_width}x{image_height}\n")


if __name__ == "__main__":
    main()
