def write_color(pixel_color, samples_per_pixel):
    r = pixel_color.x
    g = pixel_color.y
    b = pixel_color.z

    scale = 1.0 / samples_per_pixel

    r *= scale
    g *= scale
    b *= scale

    ir = 256 * clamp(r, 0.0, 0.999)
    ig = 256 * clamp(g, 0.0, 0.999)
    ib = 256 * clamp(b, 0.0, 0.999)
    return f"{ir} {ig} {ib}\n"


def clamp(val, minval, maxval):
    return max(minval, min(val, maxval))
