# oauth_handler.py

class OAuthHandler:
    def authenticate(self, token: str) -> bool:
        return token == "valid_token"