from ..abstract.operation import Operation
from .calculation import _rgb_to_gray_numba
import numpy as np
from ..helper import register

"""
    IMAGE COLOR AREA
"""
@register("to_gray")
class ConvertToGray(Operation):
    def apply_single(self, image, params):
        if image.ndim != 3 or image.shape[2] != 3:
            return image  # Already grayscale
        return _rgb_to_gray_numba(image)

"""
    IMAGE THRESHOLD AREA
"""
@register("threshold")
class ThresholdImage(Operation):
    def apply_single(self, image, params):
        threshold = params.get("value", 127)
        mode = params["mode"].lower()

        # if rgb convert to gray
        if image.ndim == 3 and image.shape[2] == 3:
            image = _rgb_to_gray_numba(image)

        # threshold modes
        if mode == "binary": # threshold → 255, <= threshold → 0
            return np.where(image > threshold, 255, 0).astype('uint8')
        elif mode == "reverse": # threshold → 0, <= threshold → 255
            return np.where(image > threshold, 0, 255).astype('uint8')
        elif mode == "truncate": # threshold → threshold, <= threshold → pixel
            return np.where(image > threshold, threshold, image).astype('uint8')
        elif mode == "tozero": # threshold → pixel, <= threshold → 0
            return np.where(image > threshold, image, 0).astype('uint8')
        elif mode == "tozero_inv": # threshold → 0, <= threshold → pixel
            return np.where(image > threshold, 0, image).astype('uint8')
        else:
            print(f"[✗] Unknown threshold mode: {mode}")
            return image