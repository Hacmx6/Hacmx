import socket


def grab_banner(ip, ports):
    banners = {}

    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(2)
            sock.connect((ip, port))
            sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
            banner = sock.recv(1024).decode(errors="ignore")
            banners[port] = banner.strip()
            sock.close()
        except:
            banners[port] = "Não capturado"

    return banners
