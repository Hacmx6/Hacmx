import socket

COMMON_SUBS = ["www", "mail", "api", "dev", "admin", "test"]


def subdomain_enum(domain):
    found = []

    for sub in COMMON_SUBS:
        subdomain = f"{sub}.{domain}"
        try:
            socket.gethostbyname(subdomain)
            found.append(subdomain)
        except:
            pass

    return found
