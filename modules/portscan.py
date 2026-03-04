import socket
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm


def check_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return port
    except:
        pass
    return None


def scan_ports(ip, mode="quick"):
    ports = range(1, 1025) if mode == "full" else [21,22,25,53,80,110,143,443,3306,8080]

    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = list(tqdm(executor.map(lambda p: check_port(ip, p), ports),
                            total=len(ports),
                            desc="Scanning Ports"))

    for r in results:
        if r:
            open_ports.append(r)

    return sorted(open_ports)
