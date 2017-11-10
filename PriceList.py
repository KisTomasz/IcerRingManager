class PriceList:
    # _________________________________________________
    def __init__(self):
        # cena ulgowego biletu
        self.half_ticket = 5

        # cena normalnego bietu
        self.normal_ticket = 10

        # cena za łyżwy
        self.boots = 7

        # nazwa biletu tańszego
        self.half_ticket_name = "ulgowy"

        # nazwa biletu droższego
        self.normal_ticket_name = "normalny"
    # _________________________________________________

    def getTicketPriceByName(self, name):
        if name == self.half_ticket_name:
            return self.half_ticket
        elif name == self.normal_ticket_name:
            return self.normal_ticket
        else:
            return "Nie ma takiej nazwy"

