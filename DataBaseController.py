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

    def createEntriesTable(self):
        print "Opened database successfully";

        self.conn.execute('''CREATE TABLE entries
            (ENTRY_ID     INTEGER     PRIMARY KEY  AUTOINCREMENT,
            DATE          DATE        NOT NULL,
            CUSTOMER_ID   INTEGER     NOT NULL,
            BOUGHT_HOURS  INTEGER     NOT NULL,
            HOURS_COST    INTEGER     NOT NULL,
            BOOTS_COST    INTEGER     NOT NULL)''')
        self.conn.commit()
        print "Table entries created successfully";

    def insertEntry(self, date, customer_id, bought_hours, hours_cost, boots_cost):
        self.conn.execute('''INSERT INTO entries
            VALUES (NULL
                , ?
                , ?
                , ?
                , ?
                , ?)''', (date, customer_id, bought_hours, hours_cost, boots_cost))
        self.conn.commit()

    def getAllEntries(self):
        cursor = self.conn.execute("SELECT * FROM entries")
        return cursor

    def printAllEntries(self):
        cursor = self.conn.execute("SELECT * FROM entries")
        for row in cursor:
            print "ENTRY_ID = ", row[0]
            print "DATE = ", row[1]
            print "CUSTOMER_ID = ", row[2]
            print "BOUGHT_HOURS = ", row[3]
            print "HOURS_COST = ", row[4]
            print "BOOTS_COST = ", row[5], "\n"

    def getEntriesByDate(self):
        cursor = self.conn.execute("SELECT * FROM entries")

    def dropEntriesTable(self):
        # TODO implement this type of table
        print "Opened database successfully";

        self.conn.execute('DROP TABLE ENTRIES')
        self.conn.commit()
        print "Table entries dropped successfully";

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


    def modifyCustomerName(self, id, name):
        self.conn.execute("UPDATE customers SET name = ? WHERE ID = ?",  (name, id))
        self.conn.commit()
        print "Total number of rows updated :", self.conn.total_changes
        cursor = self.conn.execute("SELECT id, name, surname, ticket_type FROM CUSTOMERS WHERE ID = ?", (id,))
        for row in cursor:
            print "ID = ", row[0]
            print "imie = ", row[1]
            print "nazwisko = ", row[2]
            print "typ biletu = ", row[3], "\n"

    def modifyCustomerSurname(self, id, surname):
        self.conn.execute("UPDATE customers SET surname = ? WHERE ID = ?", (surname, id))
        self.conn.commit()

    def modifyCustomerTicketType(self, id, ticket_type):
        self.conn.execute("UPDATE customers SET ticket_type = ? WHERE ID = ?", (ticket_type, id))
        self.conn.commit()

    def findByName(self, name):
        name = name + "%"
        cursor = self.conn.execute("SELECT * FROM customers WHERE name LIKE ?", (name,))
        return cursor

    def findBySurname(self, surname):
        surname = surname + "%"
        conn = sqlite3.connect(self.dataBaseName)
        cursor = conn.execute("SELECT * FROM customers WHERE surname LIKE ?", (surname,))
        return cursor

    def __del__(self):
        self.conn.close()
        print " deletion of database controller"