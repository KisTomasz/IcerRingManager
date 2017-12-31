from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def print_data_to_pdf(file_name, m_data, summary_matrix):
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    # container for the 'Flowable' objects
    elements = []
    rows = len(m_data)
    columns = 5  # (6 - 1 exactly)

    t = Table(m_data, rowHeights=rows*[0.5*inch])
    t.setStyle(TableStyle([('FONTSIZE',(0,0),(columns,rows -1), 14),
                       ('ALIGN',(0,0),(columns, rows - 1),'CENTER'),
                       ('VALIGN',(0,0),(columns, rows -1),'MIDDLE'),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))
    t2 = Table(summary_matrix, rowHeights=3*[0.5*inch])
    t2.setStyle(TableStyle([('FONTSIZE',(0,0),(1,2), 14),
                       ('ALIGN',(0,0),(1, 2),'CENTER'),
                       ('VALIGN',(0,0),(1, 2),'MIDDLE'),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1, -1), 0.25, colors.black),
                       ]))

    elements.append(t)
    elements.append(t2)

# write the document to disk
    doc.build(elements)
