#!/usr/bin/python
import time
import datetime
from Tkinter import *
from Customer import Customer
from DataBaseController import DataBaseController


def updateSummary():
    # godzina 15 lyzwy 8zl
    moneyString = summaryField.cget("text")
    print str.split(moneyString)

    count, lyzwy, czas, razem = str.split(moneyString)

    count = int(count) +1
    lyzwy = int(lyzwy) + 8
    czas = int(czas) + 15
    razem = czas + lyzwy
    summaryField.configure(text =  str(count) + "\t\t " + str(lyzwy) + "\t\t " + str(czas) + "\t\t " + str(razem))

def update_clock():
    now = time.strftime("%H:%M:%S")
    clock.configure(text=now)
    root.after(1000, update_clock)

def getLocalTime():
    return time.localtime(time.time())

def getTimeAfterMinutes(minutes = 60):
    return time.localtime(time.time() + minutes * 60)

def update2ndList():
    for i, entity in enumerate(lbIceRingMembers.get(0, END)):
        newEntity = list(entity)

        dateString = newEntity[2]
        parsedTime = time.strptime(dateString, '%a %b %d %H:%M:%S %Y')
        time.mktime(parsedTime)

        timeDiff = time.mktime(parsedTime) - time.mktime(getLocalTime())
        m, s = divmod(timeDiff, 60)
        timeToInsert = '%02d:%02d' % (m, s)
        newEntity.pop(3)
        newEntity.insert(3, timeToInsert)

        lbIceRingMembers.delete(i)
        lbIceRingMembers.insert(i, tuple(newEntity))
        if timeDiff < 3595:
            lbIceRingMembers.itemconfig(i, {'fg': 'red'})
    root.after(1000, update2ndList)

def get_list(event):

    # get selected line index
    index = listbox.curselection()[0]
    # get the line's text
    seltext = [listbox.get(index)]
    seltext += [time.asctime(getLocalTime()), time.asctime(getTimeAfterMinutes())]
    start_dt = getLocalTime()
    end_dt = getTimeAfterMinutes()
    print time.mktime(end_dt) - time.mktime(start_dt)
    seltext += [time.mktime(end_dt) - time.mktime(start_dt)]
    enter1.delete(0, 50)
    updateSummary()
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
def displayMatchingPeopleByName(event):
    listbox.delete(0, END)
    dataBaseConroller = DataBaseController("test.db")
    pattern = enter1.get()
    foundCursor = dataBaseConroller.findByName(pattern)
    for entity in foundCursor:
        listbox.insert(0, entity)
        pass
enter1.bind('<Return>', displayMatchingPeopleByName)
enter1.pack(fill=X)

clock = Label(root, text="")
update_clock()
clock.pack()

label2 = Label(root, text = "Ilosc_osob \t hajs_za_lyzwy \t hajs_za_godziny \t razem")
label2.pack(fill=X)

summaryField = Label(root, text = "0 \t\t 0 \t\t  0  \t\t 0")
print summaryField.cget("text")
summaryField.pack(fill=X)
mainloop()
