from utils.vec3 import Point3, Vec3
from utils.ray import Ray


class Camera:
    def get_ray(self, u, v):
        aspect_ratio = 16.0 / 9.0
        viewport_height = 2.0
        viewport_width = aspect_ratio * viewport_height
        focal_length = 1.0
        origin = Point3(0, 0, 0)
        horizontal = Vec3(viewport_width, 0.0, 0.0)
        vertical = Vec3(0.0, viewport_height, 0.0)
        lower_left_corner = (
            origin - horizontal / 2 - vertical / 2 - Vec3(0, 0, focal_length)
        )

        return Ray(origin, lower_left_corner + u * horizontal + v * vertical - origin)
