import requests


def detect_technology(domain):
    tech = []

    try:
        r = requests.get(f"http://{domain}", timeout=5)
        server = r.headers.get("Server", "")

        if "Apache" in server:
            tech.append("Apache")
        if "nginx" in server:
            tech.append("Nginx")
        if "cloudflare" in server.lower():
            tech.append("Cloudflare")

    except:
        pass

    return tech if tech else ["Não identificado"]
