from typing import List

from src.host import Packet, PacketPriority


def average_queue_length(packets: List[Packet], simulation_time: float) -> float:
    result: float = 0
    change_times = []
    for packet in packets:
        if packet.dropped:
            continue
        elif not packet.service_time:
            change_times.append(packet.entry_time)
        else:
            change_times.append(packet.entry_time)
            change_times.append(packet.execution_start_time)
    change_times.append(simulation_time)
    change_times.sort()
    for i in range(0, len(change_times) - 1):
        count = 0
        for packet in packets:
            if packet.dropped:
                continue
            elif not packet.service_time and change_times[i] >= packet.entry_time:
                count += 1
            elif change_times[i] >= packet.entry_time and change_times[i + 1] < packet.execution_start_time:
                count += 1
        result += count * (change_times[i + 1] - change_times[i])
    return result / simulation_time


def average_length_of_all_queue(packets: List[Packet], simulation_time: float, policy) -> float:
    if policy == 'WRR':
        result = 0
        for e in PacketPriority:
            packets_e = []
            for packet in packets:
                if packet.priority.name == e.name:
                    packets_e.append(packet)
            result += average_queue_length(packets, simulation_time)
        return result / (len(PacketPriority))
    else:
        return average_queue_length(packets, simulation_time)


