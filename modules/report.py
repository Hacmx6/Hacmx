# ~/Hacmx/hacmx/modules/report.py
import csv
import os

def save_csv(domain, ip, rdns, subdomains, open_ports, banners, headers, ssl_info, geo_info, output_dir=None):
    if output_dir is None:
        output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.join(output_dir, f"{domain}.csv")
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Campo", "Valor"])
        writer.writerow(["Domínio", domain])
        writer.writerow(["IP", ip])
        writer.writerow(["Reverse DNS", rdns])
        writer.writerow(["Subdomínios", ", ".join([str(s) for s in subdomains])])
        writer.writerow(["Portas Abertas", ", ".join([str(p) for p in open_ports])])
        writer.writerow(["Banners", ", ".join([str(b) for b in banners])])
        writer.writerow(["Headers", json_to_str(headers)])
        writer.writerow(["SSL", json_to_str(ssl_info)])
        writer.writerow(["GeoIP", json_to_str(geo_info)])

def json_to_str(data):
    """Converte dict em string legível para CSV"""
    if not data:
        return ""
    return "; ".join([f"{k}: {v}" for k, v in data.items()])
