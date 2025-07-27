import hmac
import hashlib
import secrets

class HMACGenerator:
    def __init__(self, message: bytes, key: bytes):
        self.message = message
        self.key = key

    def compute_hmac(self):
        return hmac.new(self.key, self.message, hashlib.sha3_256).hexdigest()

    @staticmethod
    def generate_key():
        return secrets.token_bytes(32)