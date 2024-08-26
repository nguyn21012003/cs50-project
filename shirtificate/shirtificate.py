from textwrap import fill
from turtle import color
from fpdf import FPDF


class PDF(FPDF):
    def header(self):

        self.set_font("helvetica", "B", 40)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(0)


name = input("Name: ")


# Instantiation of inherited class
pdf = PDF(orientation="P", unit="mm", format="A4")


pdf.add_page()
pdf.image("shirtificate.png", x="C")
pdf.set_font("Times", size=30)
pdf.set_text_color(00, 00, 00)
pdf.text(x=52, y=100, text=f"{name} took CS50")
pdf.output("shirtificate.pdf")
