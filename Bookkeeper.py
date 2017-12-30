# -*- coding: utf-8 -*-
from datetime import datetime
from DataBaseController import DataBaseController
from PriceList import PriceList
import time


class Bookkeeper:
    def __init__(self):
        self.entriesList = []
        self.people_onBoard = {}
        self.money_from_hours = 0
        self.money_from_boots = 0
        self.price_list = PriceList()

    def save_entry_to_data_base(self, customer_id, hours_count, were_boots):
        database_controller = DataBaseController("test.db")
        date = time.strftime("%Y-%m-%d")
        ticket_type = self.people_onBoard[customer_id]
        ticket_cost = self.price_list.getTicketPriceByName(ticket_type)
        boots_cost = 0
        if were_boots and not ticket_cost == 0:
            boots_cost = self.price_list.boots

        hours_cost = hours_count * ticket_cost

        database_controller.insertEntry(date=date, customer_id=customer_id, bought_hours=hours_count,
            hours_cost=hours_cost, boots_cost=boots_cost)
        del self.people_onBoard[customer_id] # it will generate troubles when same person is inserted few times



    # TODO temporary solutiion to be reworked for better design
    def register_entry_on_board(self, client_id, ticket_type):
        self.people_onBoard[client_id] = ticket_type

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
        # print "ENTRY_ID = ", row[0]
        # print "DATE = ", row[1]
        # print "CUSTOMER_ID = ", row[2]
        # print "BOUGHT_HOURS = ", row[3]
        # print "HOURS_COST = ", row[4]
        # print "BOOTS_COST = ", row[5], "\n"
        database_controller = DataBaseController("test.db")
        cursor = database_controller.getAllEntries()

        money_from_boots = 0
        money_from_hours = 0

        pdfWriter.cell(0, 10, '''nr             data        id        ilosc_godzin        wartosc_godzin
                lyzwy''', border=0, ln=1)

        nr = 1
        for raport_entry in cursor:
            pdfWriter.cell(0, 10, "%s        %s        %s        %s                   %s                    %s" % (nr, raport_entry[1],
                raport_entry[2], raport_entry[3], raport_entry[4], raport_entry[5]), border=0, ln=1)
            money_from_hours += int(raport_entry[4])
            money_from_boots += int(raport_entry[5])
            nr += 1

        added_money = money_from_boots + money_from_hours

        pdfWriter.cell(0, 10, "Zysk za wypozyczenia: %s zlotch" % money_from_boots, border=0, ln=1)
        pdfWriter.cell(0, 10, "Zysk za godziny: %s zlotych" % money_from_hours, border=0, ln=1)
        pdfWriter.cell(0, 10, "Razem: %s zlotych" % added_money, border=0, ln=1)

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
