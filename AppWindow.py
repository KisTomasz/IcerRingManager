#!/usr/bin/python
import time
from Tkinter import *
from Customer import Customer
from DataBaseController import DataBaseController


def getLocalTime():
    return time.asctime(time.localtime(time.time()))
   # ? print "Local current time :", localtime

def set_list(event):
    listbox.delete(0, END)
    dataBaseConroller = DataBaseController("test.db")
    pattern = enter1.get()
    foundCursor = dataBaseConroller.findByName(pattern)
    for entity in foundCursor:
        listbox.insert(0, entity)
        pass

def get_list(event):
    """
    function to read the listbox selection
    and put the result in an entry widget
    """
    # get selected line index
    index = listbox.curselection()[0]
    # get the line's text
    seltext = [listbox.get(index)]
    seltext += [getLocalTime()]
    # delete previous text in enter1
    enter1.delete(0, 50)
    # now display the selected text
    lbIceRingMembers.insert(0, tuple(seltext))

def onDouble(event):
    widget = event.widget
    selection = widget.curselection()
    value = widget.get(selection[0])
    print "selection:", selection, ": '%s'" % value

root = Tk()

listbox = Listbox(root)
listbox.bind("<Double-Button-1>", get_list)
listbox.pack(fill=X)

lbIceRingMembers = Listbox(root)
lbIceRingMembers.pack(fill=X)

enter1 = Entry(root, width=50, bg='yellow')
# pressing the return key will update edited line
enter1.bind('<Return>', set_list)
enter1.pack(fill=X)
mainloop()
