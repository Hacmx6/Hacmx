# ~/Hacmx/hacmx/modules/report_pdf.py
from fpdf import FPDF
import os
import json
import time

def save_pdf(domain, report_data, output_dir=None):
    if output_dir is None:
        output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"HACMX - Relatório de {domain}", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    for key, value in report_data.items():
        if isinstance(value, list):
            value = ", ".join([str(v) for v in value])
        elif isinstance(value, dict):
            value = "; ".join([f"{k}: {v}" for k, v in value.items()])
        pdf.multi_cell(0, 8, f"{key}: {value}")
        pdf.ln(2)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"{domain}_{timestamp}.pdf")
    pdf.output(filename)
