# -*- coding: utf-8 -*-

from config_reader import read_prices_from_config_file


class PriceList:
    # _________________________________________________
    def __init__(self):
        self.prices_dict = read_prices_from_config_file()

        # cena ulgowego biletu
        self.half_ticket = self.prices_dict['ulgowy']

        # cena normalnego bietu
        self.normal_ticket = self.prices_dict['normalny']

        # cena promocyjnego bietu
        self.promotion_ticket = 0

        # cena za łyżwy
        self.boots = self.prices_dict['boots']

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
