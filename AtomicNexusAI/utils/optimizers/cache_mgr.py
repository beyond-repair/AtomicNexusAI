# cache_mgr.py

class CacheManager:
    def __init__(self) -> None:
        self.cache = {}

    def set(self, key: str, value: any) -> None:
        self.cache[key] = value

    def get(self, key: str) -> any:
        return self.cache.get(key)