import hashlib
import base58
from bip32utils import BIP32Key
from typing import Dict

class HdWalletManager:
    HARDENED = 0x80000000  # Manually defined hardened constant
    
    def __init__(self, seed: bytes = None):
        if not seed:
            seed = hashlib.sha256(b'default-edu-seed').digest()
            
        if len(seed) < 16:
            raise ValueError("Seed must be at least 16 bytes")
            
        self.root_key = BIP32Key.fromEntropy(seed)
        
    def derive_account(self, path: str) -> Dict:
        key = self.root_key
        for index in path.split('/')[1:]:
            if index.endswith("'"):
                idx = int(index[:-1]) | self.HARDENED
            else:
                idx = int(index)
            key = key.ChildKey(idx)
            
        return {
            'path': path,
            'private_key': key.WalletImportFormat(),
            'public_key': key.PublicKey().hex(),
            'address': self._generate_address(key.PublicKey())
        }
    
    def _generate_address(self, public_key: bytes) -> str:
        sha = hashlib.sha256(public_key).digest()
        ripemd = hashlib.new('ripemd160', sha).digest()
        return base58.b58encode_check(ripemd).decode()
