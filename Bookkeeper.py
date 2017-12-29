# -*- coding: utf-8 -*-
from datetime import datetime


class Bookkeeper:
    def __init__(self):
        self.entriesList = []
        self.money_from_hours = 0
        self.money_from_boots = 0
        self.boots_price = 8
        self.hours_price = 10

    def saveEntry(self, client_id, client_name, client_surname, hoursCount, wereBoots):
        self.entriesList.append(RaportEntry(client_id, client_name, client_surname, hoursCount, wereBoots))
        if wereBoots == 'Tak':
            self.money_from_boots += self.boots_price

        self.money_from_hours = int(hoursCount) * self.hours_price


    def printAll(self):
        # for raport_entry in self.entriesList:
        #     print (raport_entry.client_id, raport_entry.client_name, raport_entry.client_surname,
        #         raport_entry.hours_count, raport_entry.were_boots)
        self.save_session_to_pdf()

    def save_session_to_pdf(self):
        pdfWriter = PdfWriter()
        pdfWriter.alias_nb_pages()
        pdfWriter.set_font("Times", size=12)
        pdfWriter.add_page()

        nr = 1
        for raport_entry in self.entriesList:
            pdfWriter.cell(0, 10, "%s %s %s %s %s" % (nr, raport_entry.client_name,
                raport_entry.client_surname, raport_entry.hours_count, raport_entry.were_boots), border=0, ln=1)
            nr += 1

        pdfWriter.cell(0, 10, "Kasa za buty: %s zlotch" % self.money_from_boots, border=0, ln=1)
        pdfWriter.cell(0, 10, "Kasa za godziny: %s zlotych" % self.money_from_hours, border=0, ln=1)

        pdfWriter.output("raport.pdf")

class RaportEntry:
    def __init__(self, client_id, client_name, client_surname, hours_count, were_boots):
        self.client_id = client_id
        self.client_name = client_name
        self.client_surname = client_surname
        self.hours_count = hours_count
        self.were_boots = were_boots



from fpdf import FPDF
class PdfWriter(FPDF):
    def header(self):
        """
        Header on each page
        """

        # position logo on the right
        self.cell(w=80)

        # set the font for the header, B=Bold
        self.set_font("Arial", style="B", size=15)
        # page title
        current_date = datetime.now().strftime('%Y-%m-%d')
        self.cell(40, 10, str(current_date), border=1, ln=0, align="C")
        # insert a line break of 20 pixels
        self.ln(20)

    # ----------------------------------------------------------------------
    def footer(self):
        """
        Footer on each page
        """
        # position footer at 15mm from the bottom
        self.set_y(-15)

        # set the font, I=italic
        self.set_font("Arial", style="I", size=8)

        # display the page number and center it
        pageNum = "Strona %s/{nb}" % self.page_no()
        self.cell(0, 10, pageNum, align="C")

    def write_entry_to_pdf(entry):
        pass
