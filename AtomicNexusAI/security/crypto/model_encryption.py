# model_encryption.py

class ModelEncryption:
    def encrypt_model(self, model: str) -> str:
        return f"encrypted_model({model})"

    def decrypt_model(self, encrypted_model: str) -> str:
        if encrypted_model.startswith("encrypted_model(") and encrypted_model.endswith(")"):
            return encrypted_model[len("encrypted_model("):-1]
        return encrypted_model