from nacl.signing import SigningKey
from nacl.exceptions import BadSignatureError
import base58

class TransactionSigner:
    def __init__(self, private_key: str):
        self.signer = SigningKey(base58.b58decode(private_key))
        
    def sign_transaction(self, tx_data: bytes) -> dict:
        try:
            signed = self.signer.sign(tx_data)
            return {
                'signature': base58.b58encode(signed.signature).decode(),
                'public_key': base58.b58encode(bytes(self.signer.verify_key)).decode()
            }
        except BadSignatureError:
            raise ValueError("Invalid transaction data for signing")

    @staticmethod
    def verify_signature(public_key: str, signature: str, message: bytes) -> bool:
        try:
            vk = base58.b58decode(public_key)
            sig = base58.b58decode(signature)
            return SigningKey(verify_key=vk).verify(message, sig)
        except:
            return False
