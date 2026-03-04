import requests


def check_security_headers(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        headers = response.headers

        security_headers = [
            "Strict-Transport-Security",
            "X-Frame-Options",
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "Referrer-Policy"
        ]

        return {h: headers.get(h, "Ausente") for h in security_headers}

    except:
        return {"Erro": "Falha ao analisar headers"}

