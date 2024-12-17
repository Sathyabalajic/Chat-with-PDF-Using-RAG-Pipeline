from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Sample PDF Document', align='C', ln=1)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=1, align='L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Add content
pdf.chapter_title("Unemployment Rates by Degree Type")
pdf.chapter_body("""
Bachelor's Degree: 3.5%
Master's Degree: 2.8%
PhD: 2.0%
No Degree: 6.7%
""")

pdf.chapter_title("Comparison of Employment Data")
pdf.chapter_body("""
The following table summarizes the employment and unemployment rates:
Degree Type   | Employment (%) | Unemployment (%)
Bachelor's    | 96.5           | 3.5
Master's      | 97.2           | 2.8
PhD           | 98.0           | 2.0
No Degree     | 93.3           | 6.7
""")

pdf.chapter_title("Additional Notes")
pdf.chapter_body("""
This data is collected from a recent survey conducted in 2024. 
The figures represent the national average for the respective degree types.
""")

# Save PDF
pdf.output("sample.pdf")
print("Sample PDF created: sample.pdf")
