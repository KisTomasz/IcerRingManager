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

        if entryTimeDate + timedelta(hours=int(boughtHoursStr)) > currentDate:
            timeDiff = entryTimeDate + timedelta(hours=int(boughtHoursStr)) - currentDate
            listCtrl.SetItemTextColour(index, wx.Colour(0, 0, 0));
        else:
            timeDiff = currentDate - entryTimeDate + timedelta(hours=int(boughtHoursStr))
            listCtrl.SetItemTextColour(index, wx.Colour(255, 0, 0));

        listCtrl.SetStringItem(index, 5, str(timeDiff))
        index += 1


# ______________________________________________________________________________________________________________________
# obsluga timerow

def getCurrentTime():
    # return time.localtime(time.time())
    return time.strftime("%H:%M:%S")

# ______________________________________________________________________________________________________________________
# dialog

class AddNewClientDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        #   nazwisko text label
        self.surnameStaticText = wx.StaticText(self, wx.ID_ANY, u"Nazwisko", wx.DefaultPosition, wx.DefaultSize, 0)
        self.surnameStaticText.Wrap(-1)
        bSizer5.Add(self.surnameStaticText, 0, wx.ALL, 5)

        #   surname text controller
        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_textCtrl4, 0, wx.ALL | wx.EXPAND, 5)

        #   imie textlabel
        self.nameStaticText = wx.StaticText(self, wx.ID_ANY, u"Imie", wx.DefaultPosition, wx.DefaultSize, 0)
        self.nameStaticText.Wrap(-1)
        bSizer5.Add(self.nameStaticText, 0, wx.ALL, 5)

        #   name text controller
        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_textCtrl5, 0, wx.ALL | wx.EXPAND, 5)

        #   ticketType textlabel
        self.ticketTypeStaticText = wx.StaticText(self, wx.ID_ANY, u"Typ biletu:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ticketTypeStaticText.Wrap(-1)
        bSizer5.Add(self.ticketTypeStaticText, 0, wx.ALL, 5)

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
        # bSizer5.Fit(self) # commented to check later what is needed here

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


# _____________________________________________________________________________________________________
class ModifyClientDataDialog(wx.Dialog):
    def __init__(self, parent, searchListCtrl):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
             size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        idx = searchListCtrl.GetNextSelected(-1)
        if idx == -1:
            self.Destroy()

        self.id_obj = searchListCtrl.GetItem(idx, 0)
        self.nameObj = searchListCtrl.GetItem(idx, 1)
        surnameObj = searchListCtrl.GetItem(idx, 2)

        #   nazwisko text label
        self.surnameStaticText = wx.StaticText(self, wx.ID_ANY, u'Nazwisko:    ' + surnameObj.GetText(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.surnameStaticText.Wrap(-1)
        bSizer5.Add(self.surnameStaticText, 0, wx.ALL, 5)

        #   surname text controller
        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, surnameObj.GetText(), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_textCtrl4, 0, wx.ALL | wx.EXPAND, 5)

        #   imie textlabel
        self.nameStaticText = wx.StaticText(self, wx.ID_ANY, u'Imię    ' + self.nameObj.GetText(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.nameStaticText.Wrap(-1)
        bSizer5.Add(self.nameStaticText, 0, wx.ALL, 5)

        #   name text controller
        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, self.nameObj.GetText(), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_textCtrl5, 0, wx.ALL | wx.EXPAND, 5)

        #   ticketType textlabel
        self.ticketTypeStaticText = wx.StaticText(self, wx.ID_ANY, u"Typ biletu:", wx.DefaultPosition, wx.DefaultSize,
                                                  0)
        self.ticketTypeStaticText.Wrap(-1)
        bSizer5.Add(self.ticketTypeStaticText, 0, wx.ALL, 5)

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
        # bSizer5.Fit(self) # commented to check later what is needed here

        self.Centre(wx.BOTH)
        # Connect Events
        self.m_sdbSizer1OK.Bind(wx.EVT_BUTTON, self.onModifyDataAccepted)

    def __del__(self):
        print "del"

    def onModifyDataAccepted(self, evt):
        id = self.id_obj.GetText()
        new_name = self.m_textCtrl5.GetValue()
        new_surname = self.m_textCtrl4.GetValue()
        new_ticket_type = self.m_choice1.GetStringSelection()
        dataBaseConroller = DataBaseController("test.db")
        print id
        dataBaseConroller.modifyCustomerName(id=id, name=new_name)
        dataBaseConroller.modifyCustomerSurname(id=id, surname=new_surname)
        dataBaseConroller.modifyCustomerTicketType(id=id, ticket_type=new_ticket_type)
        print 'accepted'
        self.Destroy()


# _____________________________________________________________________________________________________
class CustomEntryDialog(wx.Dialog):
    def __init__(self, parent, searchListCtrl, iceRingPeopleListCtrl, counterTextCtrl, bookkeper):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
             size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.iceringListCtrl = iceRingPeopleListCtrl
        self.counterTextCtrl = counterTextCtrl
        self.bookkeper = bookkeper

        idx = searchListCtrl.GetNextSelected(-1)
        if idx == -1:
            self.Destroy()

        self.id_obj = searchListCtrl.GetItem(idx, 0)
        self.nameObj = searchListCtrl.GetItem(idx, 1)
        self.surnameObj = searchListCtrl.GetItem(idx, 2)
        self.ticket_type_from_database = searchListCtrl.GetItem(idx, 3).GetText()  # kept as string here

        #   nazwisko text label
        self.surnameStaticText = wx.StaticText(self, wx.ID_ANY, u'Nazwisko:    ' + self.surnameObj.GetText(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.surnameStaticText.Wrap(-1)
        bSizer5.Add(self.surnameStaticText, 0, wx.ALL, 5)

        #   imie textlabel
        self.nameStaticText = wx.StaticText(self, wx.ID_ANY, u'Imię    ' + self.nameObj.GetText(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.nameStaticText.Wrap(-1)
        bSizer5.Add(self.nameStaticText, 0, wx.ALL, 5)

        #   ticketType textlabel
        self.ticketTypeStaticText = wx.StaticText(self, wx.ID_ANY, u"Typ biletu:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ticketTypeStaticText.Wrap(-1)
        bSizer5.Add(self.ticketTypeStaticText, 0, wx.ALL, 5)

        m_choice1Choices = [u"ulgowy", u"normalny", u"promocja"]
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        self.m_choice1.SetSelection(self.m_choice1.FindString(self.ticket_type_from_database))
        bSizer5.Add(self.m_choice1, 0, wx.ALL, 5)

        # hourseCount textlabel
        self.hours_count_StaticText = wx.StaticText(self, wx.ID_ANY, u"Ilość godzin", wx.DefaultPosition, wx.DefaultSize,
            0)
        self.hours_count_StaticText.Wrap(-1)
        bSizer5.Add(self.hours_count_StaticText, 0, wx.ALL, 5)

        # hours count choice
        m_choice_hours = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '12']
        self.m_choice_hours = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_hours, 0)
        self.m_choice_hours.SetSelection(0)
        bSizer5.Add(self.m_choice_hours, 0, wx.ALL, 5)

        # bootsTaken textlabel
        self.boots_taken_StaticText = wx.StaticText(self, wx.ID_ANY, u"Czy łyżwy", wx.DefaultPosition,
                                                    wx.DefaultSize,
                                                    0)
        self.boots_taken_StaticText.Wrap(-1)
        bSizer5.Add(self.boots_taken_StaticText, 0, wx.ALL, 5)

        # boots taken choice
        m_choice_boots = ['Tak', 'Nie']
        self.m_choice_boots = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_boots, 0)
        self.m_choice_boots.SetSelection(0)
        bSizer5.Add(self.m_choice_boots, 0, wx.ALL, 5)

        # summary textlabel
        self.summary_StaticText = wx.StaticText(self, wx.ID_ANY, u"Zrobić podsumowanie ile do zapłacenia",
            wx.DefaultPosition,
            wx.DefaultSize,
            0)

        self.summary_StaticText.Wrap(-1)
        bSizer5.Add(self.summary_StaticText, 0, wx.ALL, 5)

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer1.AddButton(self.m_sdbSizer1OK)
        self.m_sdbSizer1Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer1.AddButton(self.m_sdbSizer1Cancel)
        m_sdbSizer1.Realize();

        bSizer5.Add(m_sdbSizer1, 1, wx.EXPAND, 5)

        self.SetSizerAndFit(bSizer5)
        self.Layout()
        # bSizer5.Fit(self) # commented to check later what is needed here

        self.Centre(wx.BOTH)
        # Connect Events
        self.m_sdbSizer1OK.Bind(wx.EVT_BUTTON, self.onCustomEntryAccepted)

    def __del__(self):
        print "del"

    def onCustomEntryAccepted(self, evt):
        #ściągnąć imię, nazwisko, łyżwy, ilość godzin oraz bilet
        dataBaseConroller = DataBaseController("test.db")

        id = self.id_obj.GetText()
        name = self.nameObj.GetText()
        surname = self.surnameObj.GetText()
        selected_ticket_type =  self.m_choice1.GetStringSelection()
        selected_boots_option = self.m_choice_boots.GetStringSelection()
        seleceted_hours_count = self.m_choice_hours.GetStringSelection()
        print id, name, surname, selected_ticket_type, selected_boots_option, seleceted_hours_count
        self.iceringListCtrl.Append(
            (name, surname, selected_boots_option, getCurrentTime(), seleceted_hours_count, '', id))
        countInt = self.iceringListCtrl.GetItemCount()
        self.counterTextCtrl.SetValue(str(countInt))

        # register_entry_on_board(self, client_id, ticket_type):
        self.bookkeper.register_entry_on_board(int(id), selected_ticket_type)

        self.Destroy()

    def enterRiderToIcering(self):
        pass

# _______________________________________________________________________________________________________
#class NextIdHelper:
    # def __init__(self):