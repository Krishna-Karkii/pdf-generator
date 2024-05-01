import pandas
from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p', unit="mm", format="A4")

dv = pd.read_csv("topics.csv")

for index, rows in dv.iterrows():
    pdf.add_page()

    pdf.set_fill_color(254, 0, 0)
    pdf.set_font(family="Helvetica", style="B", size=25)
    pdf.cell(w=0, h=13, txt=rows["Topic"], ln=1, align='L')

    # Giving the co-ordinates of the line
    pdf.line(10,23,200,23)
    for i in range(rows['Pages'] - 1):
        pdf.add_page()


pdf.output('output.pdf')


