reg_table = {}

def register(name):
    def wrapper(cls):
        reg_table[name] = cls
        return cls
    return wrapper