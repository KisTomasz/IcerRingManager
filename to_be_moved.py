# -*- coding: utf-8 -*-

# board manager
from DataBaseController import DataBaseController
import time
import wx
from datetime import datetime
from datetime import timedelta


def updateTimesOnParticipantList(listCtrl):
    itemCount = listCtrl.GetItemCount()
    index = 0
    for item in range(0, itemCount, 1):
        entryTimeStr = listCtrl.GetItem(index, 3).GetText()
        entryTimeDate = datetime.strptime(entryTimeStr, '%H:%M:%S')
        # print entryTimeDate
        boughtHoursStr = listCtrl.GetItem(index, 4).GetText()
        currentDate = datetime.strptime(time.strftime("%H:%M:%S"), '%H:%M:%S')
        # print currentDate
        timeDiff = entryTimeDate + timedelta(hours=int(boughtHoursStr)) - currentDate
        # print str(timeDiff)
        listCtrl.SetStringItem(index, 5, str(timeDiff))
        index += 1

# ______________________________________________________________________________________________________________________
# obsluga timerow

def getCurrentTime():
    # return time.localtime(time.time())
    return time.strftime("%H:%M:%S")

# ______________________________________________________________________________________________________________________
# dialog

class MyDialog1(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        m_choice1Choices = [u"ulgowy", u"normalny", u"promocja"]
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        bSizer5.Add(self.m_choice1, 0, wx.ALL, 5)

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer1.AddButton(self.m_sdbSizer1OK)
        self.m_sdbSizer1Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer1.AddButton(self.m_sdbSizer1Cancel)
        m_sdbSizer1.Realize();

        bSizer5.Add(m_sdbSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer5)
        self.Layout()
        bSizer5.Fit(self)

        self.Centre(wx.BOTH)
        # Connect Events
        self.m_sdbSizer1OK.Bind(wx.EVT_BUTTON, self.onAddingCustomerAccepted)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onAddingCustomerAccepted(self, event):
        name = self.m_textCtrl5.GetValue()
        surname = self.m_textCtrl4.GetValue()
        ticketType = self.m_choice1.GetString(self.m_choice1.GetCurrentSelection())
        dataBaseConroller = DataBaseController("test.db")
        dataBaseConroller.insertCustomer(name, surname, ticketType)
        self.Destroy()
