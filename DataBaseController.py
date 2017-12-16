#!/usr/bin/python
import sqlite3


class DataBaseController:
    def __init__(self, dataBaseName):
        self.dataBaseName = dataBaseName
        self.conn = sqlite3.connect(self.dataBaseName)

    def createCustomersTable(self):
        print "Opened database successfully";

        self.conn.execute('''create table CUSTOMERS
                 (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
                 NAME           TEXT     NOT NULL,
                 SURNAME        TEXT     NOT NULL,
                 TICKET_TYPE    TEXT     NOT NULL)''')
        print "Table created customers successfully";

    def printAllCustomers(self):
        cursor = self.conn.execute("SELECT id, name, surname, ticket_type FROM CUSTOMERS")
        for row in cursor:
            print "ID = ", row[0]
            print "imie = ", row[1]
            print "nazwisko = ", row[2]
            print "typ biletu = ", row[3], "\n"

        print "Operation done successfully";

    def insertCustomer(self, name, surname, ticketType):
        self.conn.execute("INSERT INTO customers \
              VALUES (NULL, ?, ?, ?)", (name, surname, ticketType));
        self.conn.commit()

    def findByName(self, name):
        name = "%" + name + "%"
        cursor = self.conn.execute("SELECT * FROM customers WHERE name LIKE ?", (name,))
        return cursor

    def findBySurname(self, surname):
        surname = "%" + surname + "%"
        conn = sqlite3.connect(self.dataBaseName)
        cursor = conn.execute("SELECT * FROM customers WHERE surname LIKE ?", (surname,))
        return cursor

    def __del__(self):
        self.conn.close()
        print " deletion of database controller"