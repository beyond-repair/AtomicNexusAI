# AtomicNexusAI/security/crypto/secure_comms.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class SecureCommunications:
    def __init__(self, key=None):
        # Use a 256-bit key; if not provided, generate one.
        self.key = key or os.urandom(32)
        self.backend = default_backend()

    def encrypt(self, data: bytes) -> bytes:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        encrypted = encryptor.update(data) + encryptor.finalize()
        return iv + encrypted  # Prepend IV for decryption

    def decrypt(self, data: bytes) -> bytes:
        iv = data[:16]
        ciphertext = data[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()