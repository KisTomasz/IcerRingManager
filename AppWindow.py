#!/usr/bin/python
import time
import datetime
from Tkinter import *
from Customer import Customer
from DataBaseController import DataBaseController


def update_clock():
    now = time.strftime("%H:%M:%S")
    label.configure(text=now)
    updateList()
    root.after(1000, update_clock)

def updateList():
     # for entry in lbIceRingMembers:
        # listbox.delete(entry)
        # print entry
    pass

def getLocalTime():
    # return time.asctime(time.localtime(time.time()))
    return time.localtime(time.time())

def getTimeAfterHour():
    return time.localtime(time.time() + 3600)

def set_list(event):
    listbox.delete(0, END)
    dataBaseConroller = DataBaseController("test.db")
    pattern = enter1.get()
    foundCursor = dataBaseConroller.findByName(pattern)
    for entity in foundCursor:
        listbox.insert(0, entity)
        pass

def update2ndList():
    for i, entity in enumerate(lbIceRingMembers.get(0, END)):
        newEntity = list(entity)
        # newEntity.pop(1)
        # newEntity.insert(1, time.asctime(getLocalTime()))

        # seltext += [time.mktime(end_dt) - time.mktime(start_dt)]
        dateString = newEntity[2]
        parsedTime = time.strptime(dateString, '%a %b %d %H:%M:%S %Y')
        time.mktime(parsedTime)

        timeDiff = time.mktime(parsedTime) - time.mktime(getLocalTime())
        m, s = divmod(timeDiff, 60)
        timeToInsert = '%02d:%02d' % (m, s)
        newEntity.pop(3)
        newEntity.insert(3, timeToInsert)
        # print newEntity

        lbIceRingMembers.delete(i)
        lbIceRingMembers.insert(i, tuple(newEntity))
    root.after(1000, update2ndList)

def get_list(event):
    """
    function to read the listbox selection
    and put the result in an entry widget
    """
    # get selected line index
    index = listbox.curselection()[0]
    # get the line's text
    seltext = [listbox.get(index)]
    seltext += [time.asctime(getLocalTime()), time.asctime(getTimeAfterHour())]
    start_dt = getLocalTime()
    end_dt = getTimeAfterHour()
    print time.mktime(end_dt) - time.mktime(start_dt)
    seltext += [time.mktime(end_dt) - time.mktime(start_dt)]
    # delete previous text in enter1
    enter1.delete(0, 50)
    # now display the selected text
    lbIceRingMembers.insert(0, tuple(seltext))
    update2ndList()

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

label = Label(root, text="")
update_clock()
label.pack()

mainloop()
