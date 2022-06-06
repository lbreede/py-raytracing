class HitRecord:
    def set_face_normal(self, r, outward_normal):
        front_face = r.direction.dot(outward_normal) < 0
        self.normal = outward_normal if front_face else -outward_normal
