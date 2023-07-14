from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional, Type

from src.host import Packet, PacketPriority


class Queue(ABC):
    @abstractmethod
    def __init__(self, length_limit: int):
        pass

    @abstractmethod
    def push(self, packet: Packet):
        pass

    @abstractmethod
    def pop(self) -> Optional[Packet]:
        pass




