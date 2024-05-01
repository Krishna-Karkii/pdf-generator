from fpdf import FPDF

pdf = FPDF(orientation='p', unit="mm", format="A4")
pdf.add_page()

pdf.set_font(family="Helvetica", style="B", size=12)
pdf.cell(w=0, h=13, txt="Uno Reverse", ln=1, align='T')

pdf.set_font(family="Helvetica", style="I", size=12)
pdf.cell(w=0, h=13, txt="Wanna play uno reverse", ln=1, align="L")

pdf.add_page()

pdf.set_font(family="Helvetica", style="B", size=12)
pdf.cell(w=0, h=13, txt="Uno Reverse", ln=1, align='T')

pdf.set_font(family="Helvetica", style="I", size=12)
pdf.cell(w=0, h=13, txt="Wanna play uno reverse", ln=1, align="L")

pdf.output('uno.pdf')


