# secure_comms.py

class SecureCommunications:
    def encrypt(self, data: str) -> str:
        return f"encrypted({data})"

    def decrypt(self, data: str) -> str:
        if data.startswith("encrypted(") and data.endswith(")"):
            return data[len("encrypted("):-1]
        return data