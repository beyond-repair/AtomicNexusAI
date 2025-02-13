# api_key_mgr.py

class APIKeyManager:
    def __init__(self) -> None:
        self.api_keys = {}

    def generate_key(self, user: str) -> str:
        key = f"key_{user}"
        self.api_keys[user] = key
        return key

    def validate_key(self, user: str, key: str) -> bool:
        return self.api_keys.get(user) == key