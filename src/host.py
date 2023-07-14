from enum import Enum
from typing import Optional, List


class PacketPriority(Enum):
    pass


class Packet:
    priority: PacketPriority
    dropped: bool
    execution_end_time: float
    execution_start_time: float
