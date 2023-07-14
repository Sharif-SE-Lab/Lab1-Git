from typing import List, Optional

from src.generator import generate_exponential_variable
from src.host import Packet


class Core:
    def __init__(self, id: int, exponential_parameter: float):
        self.id = id
        self.exponential_parameter = exponential_parameter
        self.packet: Optional[Packet] = None

    def __str__(self) -> str:
        return f"Core {self.id}"

    def get_release_time(self, time) -> float:
        if self.packet:
            return max(self.packet.execution_end_time, time)
        return time

    def release(self):
        self.packet = None

    def is_free(self) -> bool:
        return self.packet is None

    def execute(self, packet):
        self.packet = packet
        self.packet.executed_by = self
        self.packet.service_time = generate_exponential_variable(
            self.exponential_parameter, 1
        )
