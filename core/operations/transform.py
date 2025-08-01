from ..abstract.operation import Operation
from ..helper import register
from .calculation import *
import numpy as np

"""
    IMAGE TRANSFORM AREA
"""
@register("flip")
class FlipImage(Operation):
    def apply(self, image, params):
        mode = params["mode"].lower()
        
        match mode:
            case "horizontal":
                return image[:,::-1]
            case "vertical":
                return image[::-1,:]
            case "both":
                return image[::-1,::-1]
            case _:
                print("There is an error while flipping the image")
                return image

@register("resize")
class ResizeImage(Operation):
    def apply(self, image, params):
        new_w = params["width"]
        new_h = params["height"]
        h, w = image.shape[:2]

        if image.ndim == 3:
            out = np.zeros((new_h, new_w, 3), dtype=np.uint8)
            bilinear_interpolate_rgb(image, out, w, h, new_w, new_h)
        else:
            out = np.zeros((new_h, new_w), dtype=np.uint8)
            bilinear_interpolate_grayscale(image, out, w, h, new_w, new_h)

        return out

        