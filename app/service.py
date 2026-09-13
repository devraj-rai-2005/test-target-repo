import threading
from typing import Set

class BlacklistService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(BlacklistService, cls).__new__(cls)
                cls._instance._blacklist: Set[str] = set()
        return cls._instance

    def add_token(self, token: str) -> None:
        with self._lock:
            self._blacklist.add(token)

    def is_blacklisted(self, token: str) -> bool:
        with self._lock:
            return token in self._blacklist