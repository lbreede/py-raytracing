# from abc import ABC, abstractmethod
from vec3 import Point3, Vec3


class HitRecord:
    def set_face_normal(self, r, outward_normal):
        front_face = r.direction.dot(outward_normal) < 0
        self.normal = outward_normal if front_face else -outward_normal


# class Hittable(ABC):
#     @abstractmethod
#     def hit(self, ray, t_min, t_max, hit_record):
#         pass
