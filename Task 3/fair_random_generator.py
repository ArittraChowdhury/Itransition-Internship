import secrets
import hmac
import hashlib

class FairRandomGenerator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.key = secrets.token_bytes(32)
        self.computer_number = secrets.randbelow(max_value + 1)
        self.hmac = hmac.new(self.key, str(self.computer_number).encode(), hashlib.sha3_256).hexdigest()

    def get_hmac(self):
        return self.hmac

    def get_result(self, user_number):
        if not (0 <= user_number <= self.max_value):
            raise ValueError("Invalid number")
        modular_result = (user_number - self.computer_number) % (self.max_value + 1)
        return {
            'modular_result': modular_result,
            'computer_number': self.computer_number,
            'key': self.key.hex()
        }
