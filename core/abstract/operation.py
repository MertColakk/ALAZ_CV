class Operation:
    def apply(self, image, params):
        if isinstance(image, list):
            return [self.apply_single(frame, params) for frame in image]
        return self.apply_single(image, params)

    def apply_single(self, image, params):
        raise NotImplementedError
