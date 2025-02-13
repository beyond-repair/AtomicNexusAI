secure_comms.py

class SecureCommunications:
    def encrypt(self, data):
        return f"encrypted({data})"

    def decrypt(self, data):
        if data.startswith("encrypted(") and data.endswith(")"):
            return data[len("encrypted("):-1]
        return data