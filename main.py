import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoice/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath)

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    filename = Path(filepath).stem
    filepath = filename.split("-")
    i =  filename.split("-")[0]
    d =  filename.split("-")[1]
    pdf.cell(w=0, h=8, txt=f"Invoice No. = {i}")
    pdf.cell(w=8, h=0,txt=f"date= {d}")
    pdf.output(f"PDFs/{filepath}.pdf")


