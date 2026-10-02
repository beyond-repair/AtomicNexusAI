# secure_comms.py — optional AES helper (requires cryptography)
try:
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    _HAS_CRYPTO = True
except ImportError:  # Claim-0 default path does not require cryptography
    Cipher = algorithms = modes = default_backend = None  # type: ignore
    _HAS_CRYPTO = False

import os


class SecureCommunications:
    def __init__(self, key=None):
        if not _HAS_CRYPTO:
            raise RuntimeError(
                "cryptography is not installed; pip install cryptography to use SecureCommunications"
            )
        self.key = key or os.urandom(32)
        self.backend = default_backend()

    def encrypt(self, data: bytes) -> bytes:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        encrypted = encryptor.update(data) + encryptor.finalize()
        return iv + encrypted

    def decrypt(self, data: bytes) -> bytes:
        iv = data[:16]
        ciphertext = data[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()
