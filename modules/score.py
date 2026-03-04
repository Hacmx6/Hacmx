def calculate_score(open_ports, headers, ssl_info):
    score = 100
    issues = []

    # Portas sensíveis
    risky_ports = [21, 22, 23, 3306]
    for port in open_ports:
        if port in risky_ports:
            score -= 10
            issues.append(f"Porta sensível aberta: {port}")

    # Headers ausentes
    for h, v in headers.items():
        if v == "Ausente":
            score -= 5
            issues.append(f"Header ausente: {h}")

    # SSL
    if "SSL" in ssl_info:
        score -= 15
        issues.append("SSL não configurado")

    if score < 0:
        score = 0

    return score, issues
