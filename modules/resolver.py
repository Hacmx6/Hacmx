import socket


def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return "Não resolvido"


def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Sem reverse DNS"
