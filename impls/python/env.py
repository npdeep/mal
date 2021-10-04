
class Env:
    def __init__(self, outer=None, binds = [], exprs = []):
        self.outer = outer
        self.data = {}
        for bind, expr in zip(binds, exprs):
            self.set(bind, expr)

    def set(self, key, value):
        # TODO: make value be fixed to a mal-type
        self.data[key] = value

    def find(self, key):
        if key in self.data:
            return self
        elif self.outer is not None:
            return self.outer.find(key)
        else:
            return None
    
    def get(self, key):
        env = self.find(key)
        if env is not None:
            return env.data[key]
        else:
            raise KeyError(f"{key} not found")