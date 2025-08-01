from ..abstract.operation import Operation
from ..helper import register
from imageio.v3 import imread, imwrite # Image
from imageio import get_reader, get_writer # Video
import pygame
import numpy as np

"""
    IMAGE I/O AREA
"""
@register("read")
class ReadImage(Operation):
    def apply(self, image, params):
        image = None
        path = params["path"]
        try:
            image = imread(params["path"])
            print(f"[✓] Image successfully read from: {path}")
        except Exception as e:
            print(f"[✗] Error while reading the image from {path}: {e}")
            
        return image

@register("show")
class ShowImage(Operation):
    def apply(self, image, params):
        if image is None:
            print("[✗] No image to show")
            return image

        title = params.get("title", "Image")
        pygame.init()

        h, w = image.shape[:2]
        screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(title)

        if image.ndim == 2:
            image = np.stack([image]*3, axis=-1)

        surface = pygame.surfarray.make_surface(np.transpose(image, (1, 0, 2)))

        running = True
        while running:
            screen.blit(surface, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    running = False

        pygame.quit()
        return image

@register("save")  
class SaveImage(Operation):
    def apply(self, image, params):
        path = params["path"]
        try:
            if image.dtype != np.uint8:
                image = np.clip(image, 0, 255).astype(np.uint8)

            imwrite(path, image)
            print(f"[✓] Image successfully saved to: {path}")
        except Exception as e:
            print(f"[✗] Error while saving the image to {path}: {e}")
        return image 
    
"""
    VIDEO I/O AREA
"""
@register("read_video")  
class ReadVideo(Operation):
    def apply(self, image, params):
        path = params["path"]

        try:
            reader = get_reader(path)
            frames = []
            for i, frame in enumerate(reader):
                frames.append(frame)
                if (i + 1) % 50 == 0:
                    print(f"[•] {i + 1} frames read...")

            reader.close()
            print(f"[✓] Video successfully read from: {path} | Total frames: {len(frames)}")
            return frames

        except Exception as e:
            print(f"[✗] Error reading video from {path}: {e}")
            return []

@register("show_video")   
class ShowVideo(Operation):
    def apply(self, frames, params):
        if not frames:
            print("[✗] No video frames to display")
            return frames

        delay = 1000 // params.get("fps", 30)
        title = params.get("title", "Video")

        pygame.init()
        h, w = frames[0].shape[:2]
        screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(title)

        clock = pygame.time.Clock()
        running = True
        frame_idx = 0

        while running and frame_idx < len(frames):
            frame = frames[frame_idx]

            if frame.ndim == 2:
                frame = np.stack([frame]*3, axis=-1)

            surface = pygame.surfarray.make_surface(np.transpose(frame, (1, 0, 2)))
            screen.blit(surface, (0, 0))
            pygame.display.flip()
            clock.tick(1000 // delay)

            frame_idx += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    running = False

        pygame.quit()
        return frames

@register("save_video")  
class SaveVideo(Operation):
    def apply(self, frames, params):
        path = params["path"]
        fps = params.get("fps", 30)

        try:
            with get_writer(path, fps=fps, codec='libx264', bitrate='8000k') as writer:
                for i, frame in enumerate(frames):
                    if frame.dtype != np.uint8:
                        frame = np.clip(frame, 0, 255).astype(np.uint8)

                    # if gray convert to 3 channels type
                    if frame.ndim == 2:
                        frame = np.stack([frame]*3, axis=-1)

                    writer.append_data(frame)
                    
                    if (i + 1) % 50 == 0:
                        print(f"[•] {i + 1} frames written...")
            print(f"[✓] Video successfully saved to: {path}")
        except Exception as e:
            print(f"[✗] Error saving video to {path}: {e}")
        return frames
