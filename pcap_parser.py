from scapy.all import rdpcap

def parse_pcap(file_path):
    packets = rdpcap(file_path)
    logs = []

    for packet in packets:
        log = {}
        if packet.haslayer('IP'):
            log['src'] = packet['IP'].src
            log['dst'] = packet['IP'].dst
            log['protocol'] = packet['IP'].proto

        if packet.haslayer('TCP'):
            log['src_port'] = packet['TCP'].sport
            log['dst_port'] = packet['TCP'].dport

        if log:
            logs.append(log)

    aggregated_logs = aggregate_logs(logs)
    return aggregated_logs

def aggregate_logs(logs):
    aggregated = {}
    for log in logs:
        key = f"{log.get('src', 'unknown')}:{log.get('src_port', 'unknown')} -> {log.get('dst', 'unknown')}:{log.get('dst_port', 'unknown')}"
        if key not in aggregated:
            aggregated[key] = 1
        else:
            aggregated[key] += 1
    return aggregated
