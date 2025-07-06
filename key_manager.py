from cryptography.fernet import Fernet
import uuid
import os
from typing import Dict

class KeyManager:
    """
    A simple in-memory cryptographic key management system.
    For production, replace in-memory storage with secure persistent storage.
    """
    def __init__(self):
        self.keys: Dict[str, bytes] = {}

    def generate_key(self) -> str:
        key = Fernet.generate_key()
        key_id = str(uuid.uuid4())
        self.keys[key_id] = key
        return key_id

    def get_key(self, key_id: str) -> bytes:
        return self.keys.get(key_id)

    def rotate_key(self, key_id: str) -> bool:
        if key_id in self.keys:
            self.keys[key_id] = Fernet.generate_key()
            return True
        return False

    def delete_key(self, key_id: str) -> bool:
        return self.keys.pop(key_id, None) is not None

    def list_keys(self):
        return list(self.keys.keys())
