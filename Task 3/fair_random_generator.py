import secrets
from hmac_generator import HMACGenerator

class FairRandomGenerator:
    def __init__(self, upper_bound):
        self.upper_bound = upper_bound
        self.secret_key = HMACGenerator.generate_key()
        self.computer_number = self._secure_random()

        message = self.computer_number.to_bytes(2, 'big')
        self.hmac = HMACGenerator(message, self.secret_key).compute_hmac()

    def _secure_random(self):
        while True:
            rand = secrets.randbits(32)
            if rand <= (2**32 // (self.upper_bound + 1)) * (self.upper_bound + 1) - 1:
                return rand % (self.upper_bound + 1)

    def get_hmac(self):
        return self.hmac

    def get_result(self, user_number):
        result = (self.computer_number + user_number) % (self.upper_bound + 1)
        return {
            "user_number": user_number,
            "computer_number": self.computer_number,
            "modular_result": result,
            "key": self.secret_key.hex()
        }