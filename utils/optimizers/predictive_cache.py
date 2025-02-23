class PredictiveCache:
    def __init__(self) -> None:
        self.cache = {}

    def predict_and_cache(self, key: str, compute_func) -> any:
        if key not in self.cache:
            self.cache[key] = compute_func()
        return self.cache[key]