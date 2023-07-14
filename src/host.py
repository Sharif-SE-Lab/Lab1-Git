from enum import Enum
from typing import Optional


class PacketPriority(Enum):
    HIGH = 2
    MEDIUM = 3
    LOW = 5


class Packet:

    def __init__(self, entry_time: float, priority: PacketPriority):
        self.entry_time: float = entry_time
        self.execution_start_time: Optional[float] = None
        self.service_time: Optional[float] = None
        self.priority = priority
        self.executed_by = None
        self.dropped = False

    @property
    def execution_end_time(self) -> Optional[float]:
        return self.execution_start_time + self.service_time

    def get_entry_time(self):
        return self.entry_time
