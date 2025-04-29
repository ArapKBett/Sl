import hmac
import hashlib
from bip32utils import BIP32Key
from typing import List, Dict

class HdWalletManager:
    def __init__(self, seed: bytes = None):
        # Generate proper 256-bit entropy if no seed provided
        if not seed:
            seed = hmac.new(
                b'edu-sim-seed',
                b'initial-seed', 
                hashlib.sha512
            ).digest()
            
        if len(seed) < 16:  # 128 bits minimum
            raise ValueError("Seed must be at least 16 bytes (128 bits)")
            
        self.root_key = BIP32Key.fromEntropy(seed)
        
    def derive_account(self, path: str) -> Dict:
        key = self.root_key
        for index in path.split('/')[1:]:
            if index.endswith("'"):
                key = key.ChildKey(int(index[:-1]) | BIP32Key.HARDEN)
            else:
                key = key.ChildKey(int(index))
        return {
            'path': path,
            'private_key': key.WalletImportFormat(),
            'public_key': key.PublicKey().hex(),
            'address': self._generate_address(key.PublicKey())
        }
    
    def _generate_address(self, public_key: bytes) -> str:
        sha = hashlib.sha256(public_key).digest()
        ripemd = hashlib.new('ripemd160')
        ripemd.update(sha)
        return base58.b58encode_check(ripemd.digest()).decode()
