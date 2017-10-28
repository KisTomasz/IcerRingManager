#!/usr/bin/python
import sqlite3


class DataBaseController:

    def __init__(self, dataBaseName):
        self.dataBaseName = dataBaseName

    def createCustomersTable(self):
        conn = sqlite3.connect(self.dataBaseName)
        print "Opened database successfully";

        conn.execute('''create table CUSTOMERS
                 (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
                 NAME           TEXT     NOT NULL,
                 SURNAME        TEXT     NOT NULL,
                 TICKET_TYPE    TEXT     NOT NULL)''')
        print "Table created customers successfully";
        conn.close()

    def printAllCustomers(self):
        conn = sqlite3.connect(self.dataBaseName)
        cursor = conn.execute("SELECT id, name, surname, ticket_type FROM CUSTOMERS")
        for row in cursor:
            print "ID = ", row[0]
            print "imie = ", row[1]
            print "nazwisko = ", row[2]
            print "typ biletu = ", row[3], "\n"

        print "Operation done successfully";
        conn.close()

    def insertCustomer(self, name, surname, ticketType):
        conn = sqlite3.connect(self.dataBaseName)
        conn.execute("INSERT INTO customers \
              VALUES (NULL, ?, ?, ?)", (name, surname, ticketType));
        conn.commit()

    def findByName(self, name):
        conn = sqlite3.connect(self.dataBaseName)
        name = "%" + name + "%"

        cursor = conn.execute("SELECT * FROM customers WHERE name LIKE ?", (name,))
        # for row in cursor:
        #     print "ID = ", row[0]
        #     print "imie = ", row[1]
        #     print "nazwisko = ", row[2]
        #     print "typ biletu = ", row[3], "\n"
        return cursor

    def findBySurname(self, surname):
        surname = "%" + surname + "%"
        conn = sqlite3.connect(self.dataBaseName)
        cursor = conn.execute("SELECT * FROM customers WHERE surname LIKE ?", (surname,))
        for row in cursor:
            print "ID = ", row[0]
            print "imie = ", row[1]
            print "nazwisko = ", row[2]
            print "typ bileu = ", row[3], "\n"

    def __exit__(self, exc_type, exc_val, exc_tb):
        conn.close()