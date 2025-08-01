# 🎯 ALAZ-CV v1: JSON Based Computer Vision Pipeline Framework

**ALAZ-CV** is a lightweight and modular computer vision framework that allows you to perform image and video processing using a simple JSON-based pipeline—no OpenCV required. It leverages core Python tools like `numpy`, `imageio`, `pygame`, and `numba`.

---

## Before Start

### Installation
```bash
pip install -r requirements.txt
```

### Run a Pipeline

```bash
python main.py --path examples/pipeline_example.json
```

---

## Pipeline Structure

Each pipeline is defined using a JSON file:

```json
{
  "pipeline": [
    { "operation": "operation_name", "params": { "key": "value" } }
  ]
}
```

* `operation`: The name of the operation to execute.
* `params`: (Optional) Parameters specific to the operation.

---

## 🧪 Example Pipelines

### 1. Convert Video to Grayscale, Display, and Save

```json
{
  "pipeline": [
    { "operation": "read_video", "params": { "path" : "test_video.mp4" } },
    { "operation": "to_gray" },
    { "operation": "show_video", "params": { "title" : "Thomas Shelby Mafia Sigma" } },
    { "operation": "save_video", "params": { "path" : "test_saved_video.mp4", "fps" : 24 } }
  ]
}
```

---

### 2. Resize Image, Flip Vertically, Show

```json
{
  "pipeline": [
    { "operation": "read", "params": { "path": "test.jpg" } },
    { "operation": "resize", "params": { "width" : 1024 , "height" : 768} },
    { "operation": "flip", "params": { "mode": "vertical" } },
    { "operation": "show", "params": { "title": "Result" } }
  ]
}
```

---

### 3. Read Image, Show, and Save

```json
{
  "pipeline": [
    { "operation": "read", "params": { "path": "test.jpg" } },
    { "operation": "show", "params": { "title": "Result" } },
    { "operation": "save", "params": { "path": "test_saved.jpg" } }
  ]
}
```

---

### 4. Thresholding with `tozero_inv` Mode

```json
{
  "pipeline": [
    { "operation": "read", "params": { "path": "test.jpg" } },
    { "operation": "threshold", "params" : {"value": 127, "mode":"tozero_inv"} },
    { "operation": "show", "params": { "title": "Result" } }
  ]
}
```

---

### 5. Default Binary Thresholding

```json
{
  "pipeline": [
    { "operation": "read", "params": { "path": "test.jpg" } },
    { "operation": "threshold" },
    { "operation": "show", "params": { "title": "Result" } }
  ]
}
```

---

## Supported Operations

| Operation    | Description                                        |
| ------------ | -------------------------------------------------- |
| `read`       | Load an image file                                 |
| `show`       | Display image using a GUI window                   |
| `save`       | Save processed image to disk                       |
| `read_video` | Load video and extract frames                      |
| `show_video` | Play video in real time                            |
| `save_video` | Export frames back into a video file               |
| `to_gray`    | Convert image/video to grayscale                   |
| `resize`     | Resize to given width/height                       |
| `flip`       | Flip image: `"horizontal"`, `"vertical"`, `"both"` |
| `threshold`  | Apply thresholding (5 modes supported)             |

---

## Extending the Framework

To define a new operation, simply subclass `Operation` and register it:

```python
@register("custom_op")
class CustomOp(Operation):
    def apply_single(self, image, params):
        # your logic here
        return image
```

---

## Notes

* All operations are executed sequentially.
* Video pipelines automatically apply frame-by-frame operations.
* Default threshold mode is `"binary"` if not provided.

---

## Dependencies

* Python 3.10+
* numpy
* imageio
* pygame
* numba (optional, for performance optimization)

---

## Future Work

Below are some planned enhancements and ideas for future versions of ALAZ-CV:

- **Real-time video stream support** (e.g. from webcam or RTSP)
- **Asynchronous pipeline execution** for faster video processing
- **Color space conversion** (e.g. HSV, YCbCr)
- **Crop operation** with flexible region selection
- **Rotation & affine transformations**
- **Basic object detection or contour finding**
- **Support for batch image directory processing**
- **Snapshot saving from video**

> 💬 Contributions and feature requests are welcome! Feel free to open an issue or pull request.

---

## Author

Developed by **MertColakk**

---
