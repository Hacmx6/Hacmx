import ssl
import socket


def check_ssl(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

                return {
                    "TLS": ssock.version(),
                    "Valido ate": cert.get("notAfter"),
                    "Emissor": cert.get("issuer")
                }

    except:
        return {"SSL": "Indisponível"}
