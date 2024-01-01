from fpdf import FPDF

pdf = FPDF(orientation = 'P',unit = 'pt', format = 'A4')

pdf.add_page()

pdf.image('/config/workspace/Automate_pdf/Copy of Yoga Classes Event Flyer Template - Made with PosterMyWall.jpg',w = 100,h=150)

pdf.set_font(family = "Times",style = 'B', size = 24)
pdf.cell(w=0,h=50,txt="Yoga Poster",align="C", border = 1)

pdf.cell(w=0,h=50,txt = '',ln=1,align='C')

pdf.set_font(family = 'Times',style = 'I', size = 14)
pdf.cell(w=0,h=50,txt = 'Description',ln=1,align='C')
txt = """The yoga sutras of Pantajali are a set of 196 aphorisms that guide yoga practice. They are one of the most important texts in yoga and offer a comprehensive view of the philosophy and practice of yoga. 
Patanjali compiled the classic sutras around 200 CE for an in-depth look at the nature of mind, consciousness, and liberation. The timeless teachings work as practical advice rooted in the yoga tradition."""

pdf.set_font(family='Times',size = 12)

pdf.multi_cell(w=0,h=50,txt = txt)

pdf.output('output.pdf')
