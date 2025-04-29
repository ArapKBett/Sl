import hmac
import hashlib
from Crypto.Protocol.KDF import HKDF

class KeyDerivator:
    def __init__(self, salt: bytes = b'edu_sim_salt'):
        self.salt = salt
        
    def derive_from_mnemonic(self, mnemonic: str, path: str) -> bytes:
        seed = hmac.new(
            self.salt,
            mnemonic.encode(),
            hashlib.sha512
        ).digest()
        
        return HKDF(
            seed,
            64,
            self.salt,
            hashmod=hashlib.sha512,
            num_keys=1
        )
