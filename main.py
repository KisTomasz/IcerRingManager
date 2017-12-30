#!/usr/bin/python
# -*- coding: utf-8 -*-

from DataBaseController import DataBaseController
import sys
import random
import time

dataBaseConroller = DataBaseController("test.db")

def fillDBFromFile():
    file = open("people.txt", "r")
    lista = file.read()
    file.close()
    people = lista.split("\n")
    people.remove("")
    for person in people:
        names = person.split()
        randInt = random.randint(1, 2)
        print names[0] + " ^ " + names[1] + " " + str(random.randint(1, 2))
        if randInt == 1:
            dataBaseConroller.insertCustomer(names[0], names[1], "ulgowy")
        else:
            dataBaseConroller.insertCustomer(names[0], names[1], "normalny")

arg = sys.argv
if arg[1] == "printAll":
    dataBaseConroller.printAllCustomers()
elif arg[1] == "insert":
    dataBaseConroller.insertCustomer(arg[2], arg[3], arg[4])
elif arg[1] == "findName":
    dataBaseConroller.findByName(arg[2])
elif arg[1] == "findSurname":
    dataBaseConroller.findBySurname(arg[2])
elif arg[1] == "time":
    print time.asctime(time.localtime(time.time() + 3600))
elif arg[1] == "createTable":
    dataBaseConroller.createCustomersTable()
elif arg[1] == "createEntries":
    dataBaseConroller.createEntriesTable()
elif arg[1] == "printEntries":
    dataBaseConroller.printAllEntries()
elif arg[1] == "dropEntries":
    dataBaseConroller.dropEntriesTable()
elif arg[1] == "readFile":
    # fillDBFromFile() // commented for safety
    pass
else:
    print "Nie rozpoznalem polecenia"
