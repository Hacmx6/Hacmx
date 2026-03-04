import argparse
import os
import json
import time

from hacmx import __version__

from hacmx.modules.resolver import resolve_domain, reverse_dns
from hacmx.modules.dns_enum import subdomain_enum
from hacmx.modules.portscan import scan_ports
from hacmx.modules.banner import grab_banner
from hacmx.modules.headers import check_security_headers
from hacmx.modules.ssl_check import check_ssl
from hacmx.modules.geoip import get_geoip
from hacmx.modules.score import calculate_score
from hacmx.modules.tech_detect import detect_technology
from hacmx.modules.report import save_csv
from hacmx.modules.report_pdf import save_pdf
from hacmx.modules.ui import banner, info, success, warning

def main():
    parser = argparse.ArgumentParser(
        description="HACMX v4.0 - Advanced Recon Tool"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"HACMX v{__version__}"
    )

    parser.add_argument(
        "-d", "--domain",
        required=True,
        help="Target domain (example.com)"
    )

    parser.add_argument(
        "--mode",
        choices=["quick", "full"],
        default="quick",
        help="Scan mode"
    )

    parser.add_argument(
        "--no-pdf",
        action="store_true",
        help="Disable PDF report generation"
    )

    args = parser.parse_args()
    domain = args.domain
    mode = args.mode
    start_time = time.time()

    banner()
    info(f"Iniciando análise em: {domain}")
    info(f"Modo selecionado: {mode}")

    try:
        # =========================
        # RESOLUÇÃO DNS
        # =========================
        ip = resolve_domain(domain)
        success(f"IP resolvido: {ip}")

        rdns = reverse_dns(ip)
        info(f"Reverse DNS: {rdns}")

        # =========================
        # ENUMERAÇÃO DNS
        # =========================
        subdomains = subdomain_enum(domain)
        success(f"Subdomínios encontrados: {len(subdomains)}")

        # =========================
        # PORTSCAN
        # =========================
        open_ports = scan_ports(ip, mode)
        success(f"Portas abertas: {open_ports}")

        # =========================
        # BANNER GRABBING
        # =========================
        banners = grab_banner(ip, open_ports)

        # =========================
        # HEADERS
        # =========================
        headers = check_security_headers(domain)

        # =========================
        # SSL
        # =========================
        ssl_info = check_ssl(domain)

        # =========================
        # GEOLOCALIZAÇÃO
        # =========================
        geo_info = get_geoip(ip)

        # =========================
        # TECNOLOGIA WEB
        # =========================
        tech = detect_technology(domain)
        success(f"Tecnologias detectadas: {tech}")

        # =========================
        # SCORE
        # =========================
        score, issues = calculate_score(open_ports, headers, ssl_info)

        print("\n================ RESULTADO FINAL ================")
        success(f"Score de Segurança: {score}/100")
        if issues:
            warning("Problemas encontrados:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            success("Nenhum problema crítico identificado.")

        # =========================
        # OUTPUT (Termux) com histórico
        # =========================
        output_dir = "/data/data/com.termux/files/home/storage/downloads/Hacmx"
        os.makedirs(output_dir, exist_ok=True)
        json_path = os.path.join(output_dir, "scans.json")

        report_data = {
            "Dominio": domain,
            "IP": ip,
            "Reverse DNS": rdns,
            "Subdominios": [str(s) for s in subdomains],
            "Portas Abertas": [str(p) for p in open_ports],
            "Tecnologias": tech,
            "Headers": headers,
            "SSL": ssl_info,
            "GeoIP": geo_info,
            "Score": score,
            "Problemas": issues,
            "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        # Carrega histórico
        if os.path.exists(json_path):
            with open(json_path, "r") as f:
                all_scans = json.load(f)
        else:
            all_scans = []

        # Adiciona novo scan
        all_scans.append(report_data)

        # Salva novamente
        with open(json_path, "w") as f:
            json.dump(all_scans, f, indent=4)

        # CSV
        save_csv(
            domain, ip, rdns,
            subdomains, open_ports,
            banners, headers,
            ssl_info, geo_info,
            output_dir=output_dir
        )

        # PDF
        if not args.no_pdf:
            save_pdf(domain, report_data, output_dir=output_dir)

        success(f"Relatórios salvos em {output_dir}")

    except Exception as e:
        warning(f"Erro durante execução: {e}")

    total_time = round(time.time() - start_time, 2)
    print("=================================================")
    info(f"Tempo total: {total_time}s\n")


if __name__ == "__main__":
    main()
