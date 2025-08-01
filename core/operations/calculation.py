from numba import njit
import numpy as np

@njit
def bilinear_interpolate_grayscale(image, out, w, h, new_w, new_h):
    ratio_w = w / new_w
    ratio_h = h / new_h
    for i in range(new_h):
        for j in range(new_w):
            x = j * ratio_w
            y = i * ratio_h
            x0 = int(x)
            y0 = int(y)
            x1 = min(x0 + 1, w - 1)
            y1 = min(y0 + 1, h - 1)
            dx = x - x0
            dy = y - y0

            a = image[y0, x0]
            b = image[y0, x1]
            c = image[y1, x0]
            d = image[y1, x1]

            value = (
                a * (1 - dx) * (1 - dy) +
                b * dx * (1 - dy) +
                c * (1 - dx) * dy +
                d * dx * dy
            )
            out[i, j] = int(value)

@njit
def bilinear_interpolate_rgb(image, out, w, h, new_w, new_h):
    ratio_w = w / new_w
    ratio_h = h / new_h
    for i in range(new_h):
        for j in range(new_w):
            x = j * ratio_w
            y = i * ratio_h
            x0 = int(x)
            y0 = int(y)
            x1 = min(x0 + 1, w - 1)
            y1 = min(y0 + 1, h - 1)
            dx = x - x0
            dy = y - y0
            for c in range(3):
                a = image[y0, x0, c]
                b = image[y0, x1, c]
                c_ = image[y1, x0, c]
                d = image[y1, x1, c]

                value = (
                    a * (1 - dx) * (1 - dy) +
                    b * dx * (1 - dy) +
                    c_ * (1 - dx) * dy +
                    d * dx * dy
                )
                out[i, j, c] = int(value)
                
@njit
def _rgb_to_gray_numba(image):
    h, w, _ = image.shape
    gray = np.empty((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            r, g, b = image[i, j]
            gray[i, j] = int(0.299 * r + 0.587 * g + 0.114 * b)
    return gray