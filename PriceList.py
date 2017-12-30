# -*- coding: utf-8 -*-

class PriceList:
    # _________________________________________________
    def __init__(self):
        # cena ulgowego biletu
        self.half_ticket = 5

        # cena normalnego bietu
        self.normal_ticket = 10

        # cena promocyjnego bietu
        self.promotion_ticket = 0

        # cena za łyżwy
        self.boots = 7

        # nazwa biletu tańszego
        self.half_ticket_name = "ulgowy"

        # nazwa biletu droższego
        self.normal_ticket_name = "normalny"

        # nazwa biletu droższego
        self.promotion_ticket_name = "promocja"
    # _________________________________________________

    def getTicketPriceByName(self, name):
        if name == self.half_ticket_name:
            return self.half_ticket
        elif name == self.normal_ticket_name:
            return self.normal_ticket
        elif name == self.promotion_ticket_name:
            return self.promotion_ticket
        else:
            return "Nie ma takiej nazwy"

