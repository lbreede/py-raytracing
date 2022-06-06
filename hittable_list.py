from hittable import HitRecord


class HittableList:
    def __init__(self, objects):
        self.objects = objects

    def hit(self, r, t_min, t_max, rec):
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = t_max

        for obj in self.objects:
            if obj.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t

                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.t = temp_rec.t

        return hit_anything
