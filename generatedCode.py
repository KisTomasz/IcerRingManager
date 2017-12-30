# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

from Bookkeeper import Bookkeeper
from DataBaseController import DataBaseController
import to_be_moved

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1074, 606), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        #######################################################################
        # NOT GUI ELEMENTS HERE
        self.bookkeeper = Bookkeeper()

        #####################################################################


        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        mainLayoutManager = wx.BoxSizer(wx.HORIZONTAL)

        leftSideGridSizer = wx.FlexGridSizer(0, 1, 0, 0)
        leftSideGridSizer.AddGrowableCol(0)
        leftSideGridSizer.AddGrowableRow(2)
        leftSideGridSizer.SetFlexibleDirection(wx.BOTH)
        leftSideGridSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)

        self.searchStaticText = wx.StaticText(self, wx.ID_ANY, u"Wyszukiwanie", wx.DefaultPosition, wx.DefaultSize, 0)
        self.searchStaticText.Wrap(-1)
        leftSideGridSizer.Add(self.searchStaticText, 0, wx.ALL, 5)

        boxSizerForDataEntry = wx.BoxSizer(wx.HORIZONTAL)

        self.surnameTextCtrl = wx.TextCtrl(self, wx.ID_ANY, u"Nazwisko...", wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizerForDataEntry.Add(self.surnameTextCtrl, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.nameTextCtrl = wx.TextCtrl(self, wx.ID_ANY, u"Imię...", wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizerForDataEntry.Add(self.nameTextCtrl, 1, wx.ALL | wx.EXPAND, 5)

        leftSideGridSizer.Add(boxSizerForDataEntry, 1, wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.searchListCtrl = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        self.searchListCtrl.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))
        self.searchListCtrl.InsertColumn(0, "id")
        self.searchListCtrl.InsertColumn(1, "Imię")
        self.searchListCtrl.InsertColumn(2, "Nazwisko")
        self.searchListCtrl.InsertColumn(3, "typ biletu")

        leftSideGridSizer.Add(self.searchListCtrl, 0, wx.ALL | wx.EXPAND, 5)

        controllButtonsBSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.enterIceringButton = wx.Button(self, wx.ID_ANY, u"Wpuść", wx.DefaultPosition, wx.DefaultSize, 0)
        controllButtonsBSizer.Add(self.enterIceringButton, 0, wx.ALL, 5)
        self.enterIceringButton.Enabled = False # TODO when would it work

        self.modifyDataButton = wx.Button(self, wx.ID_ANY, u"Modyfikuj dane", wx.DefaultPosition, wx.DefaultSize, 0)
        controllButtonsBSizer.Add(self.modifyDataButton, 0, wx.ALL, 5)

        self.NonStandardEntry = wx.Button(self, wx.ID_ANY, u"Niestandardowe wejście", wx.DefaultPosition,
            wx.DefaultSize, 0)
        controllButtonsBSizer.Add(self.NonStandardEntry, 0, wx.ALL, 5)

        leftSideGridSizer.Add(controllButtonsBSizer, 1, wx.EXPAND, 5)

        mainLayoutManager.Add(leftSideGridSizer, 1, wx.BOTTOM | wx.EXPAND, 5)

        self.separatorStaticline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        mainLayoutManager.Add(self.separatorStaticline, 0, wx.EXPAND | wx.ALL, 5)

        rightFlexGridSizer = wx.FlexGridSizer(0, 1, 0, 0)
        rightFlexGridSizer.AddGrowableCol(0)
        rightFlexGridSizer.AddGrowableRow(1)
        rightFlexGridSizer.SetFlexibleDirection(wx.BOTH)
        rightFlexGridSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)

        self.iceRingStaticText = wx.StaticText(self, wx.ID_ANY, u"Lodowisko:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.iceRingStaticText.Wrap(-1)
        rightFlexGridSizer.Add(self.iceRingStaticText, 0, wx.ALL, 5)

        self.iceRingListCtrl = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.iceRingListCtrl.SetFont(wx.Font(13, 74, 90, 90, False, "Arial")) # musi być minimum 13. Nie widac inaczej
        self.iceRingListCtrl.InsertColumn(0, "Imię")
        self.iceRingListCtrl.InsertColumn(1, "Nazwisko")
        self.iceRingListCtrl.InsertColumn(2, "Czy łyżwy")
        self.iceRingListCtrl.InsertColumn(3, "Czas wejścia")
        self.iceRingListCtrl.InsertColumn(4, "Zakupionych godzin")
        self.iceRingListCtrl.InsertColumn(5, "Pozostało")
        self.iceRingListCtrl.InsertColumn(6, "id")

        rightFlexGridSizer.Add(self.iceRingListCtrl, 0, wx.ALL | wx.EXPAND, 5)

        counterBSizer = wx.BoxSizer(wx.VERTICAL)

        self.peopleCounterStaticText = wx.StaticText(self, wx.ID_ANY, u"Liczba osób:", wx.DefaultPosition,
            wx.DefaultSize, 0)
        self.peopleCounterStaticText.Wrap(-1)
        counterBSizer.Add(self.peopleCounterStaticText, 0, wx.TOP, 5)

        self.peopleCounterTextCtrl = wx.TextCtrl(self, wx.ID_ANY, '0', wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)

        counterBSizer.Add(self.peopleCounterTextCtrl, 0, wx.ALL, 5) # dupa

        rightFlexGridSizer.Add(counterBSizer, 1, wx.EXPAND, 5)

        mainLayoutManager.Add(rightFlexGridSizer, 1, wx.EXPAND, 5)

        self.SetSizer(mainLayoutManager)
        self.Layout()
        self.m_timer = wx.Timer()
        self.m_timer.SetOwner(self, wx.ID_ANY)
        self.menubar = wx.MenuBar(0)
        self.mainMenu = wx.Menu()
        self.addClientMenuItem = wx.MenuItem(self.mainMenu, wx.ID_ANY, u"Dodaj nowego klienta", wx.EmptyString,
                                             wx.ITEM_NORMAL)
        self.mainMenu.AppendItem(self.addClientMenuItem)

        self.menubar.Append(self.mainMenu, u"Menu")

        self.raportsMenu = wx.Menu()
        self.dummyMenuItem = wx.MenuItem(self.raportsMenu, wx.ID_ANY, u"raport sesji", wx.EmptyString, wx.ITEM_NORMAL)
        self.raportsMenu.AppendItem(self.dummyMenuItem)

        self.menubar.Append(self.raportsMenu, u"Raporty")

        self.SetMenuBar(self.menubar)

        self.Centre(wx.BOTH)

        # Connect Events
        self.nameTextCtrl.Bind(wx.EVT_TEXT, self.onNameEntered)
        self.surnameTextCtrl.Bind(wx.EVT_TEXT, self.onSurnamenEntered)
        self.enterIceringButton.Bind(wx.EVT_BUTTON, self.onEnterRiderButton)
        self.modifyDataButton.Bind(wx.EVT_BUTTON, self.onModifyClientData)
        self.NonStandardEntry.Bind(wx.EVT_BUTTON, self.onCustomEntry)
        self.searchListCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSearchListCtrlItemSelected)
        self.iceRingListCtrl.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnIceringParticipantRightClick)
        self.Bind(wx.EVT_TIMER, self.onTick, id=wx.ID_ANY)
        self.m_timer.Start(milliseconds=1000) #uncomment to start timer
        self.Bind(wx.EVT_MENU, self.onAddNewCustomer, id=self.addClientMenuItem.GetId())
        self.Bind(wx.EVT_MENU, self.printRaport, id=self.dummyMenuItem.GetId())

    def __del__(self):
        pass

    def onNameEntered(self, evt):
        print self.nameTextCtrl.GetValue()
        enteredMsg = self.nameTextCtrl.GetValue()
        dataBaseConroller = DataBaseController()
        foundCursor = dataBaseConroller.findByName(enteredMsg)

        self.searchListCtrl.DeleteAllItems()

        for entity in foundCursor:
            # print entity
            self.searchListCtrl.Append(entity)

    def onSurnamenEntered(self, evt):
        print self.surnameTextCtrl.GetValue()
        enteredMsg = self.surnameTextCtrl.GetValue()
        dataBaseConroller = DataBaseController()
        foundCursor = dataBaseConroller.findBySurname(enteredMsg)

        self.searchListCtrl.DeleteAllItems()

        for entity in foundCursor:
            # print entity
            self.searchListCtrl.Append(entity)

    def onSearchListCtrlItemSelected(self, evt):
        pass

    def onEnterRiderButton(self, evt):
        idx = self.searchListCtrl.GetNextSelected(-1)
        nameObj = self.searchListCtrl.GetItem(idx, 1)
        surnameObj = self.searchListCtrl.GetItem(idx, 2)
        bootsTaken = "Tak"
        self.iceRingListCtrl.Append((nameObj.GetText(), surnameObj.GetText(), bootsTaken, to_be_moved.getCurrentTime(), '0', ''))
        countInt = self.iceRingListCtrl.GetItemCount()
        self.peopleCounterTextCtrl.SetValue(str(countInt))

    def OnIceringParticipantRightClick(self, evt):
        idx = evt.GetIndex()

        try:
            nameObj = self.iceRingListCtrl.GetItem(idx, 0)
            surnameObj = self.iceRingListCtrl.GetItem(idx, 1)
            # self.iceRingListCtrl.Append((nameObj.GetText(), surnameObj.GetText(), False)) for development
            menu = wx.Menu()
            addClientMenuItem = wx.MenuItem(self.mainMenu, wx.ID_ANY, u"Wypuść", wx.EmptyString,
                wx.ITEM_NORMAL)
            addTimeMenuItem = wx.MenuItem(self.mainMenu, wx.ID_ANY, u"Dodaj czas", wx.EmptyString,
                                            wx.ITEM_NORMAL)
            menu.Append(addClientMenuItem.GetId(), u"Wypuść")
            menu.Append(addTimeMenuItem.GetId(), u'Dodaj czas')
            self.Bind(wx.EVT_MENU, self.onRemoveFromIceRingClicked, id=addClientMenuItem.GetId())
            self.Bind(wx.EVT_MENU, self.addTimeForClient, id=addTimeMenuItem.GetId())
            self.PopupMenu(menu)
            menu.Destroy() # destroy to avoid mem leak
        except:
            print "Nothing selected on iceringListCtrl"

    def onRemoveFromIceRingClicked(self, evt):
        idx = self.iceRingListCtrl.GetNextSelected(-1)

        ####################################################
        # Book keepere work here
        name = self.iceRingListCtrl.GetItem(idx, 0).GetText() # name
        surname = self.iceRingListCtrl.GetItem(idx, 1).GetText() #surname
        boots_taken = self.iceRingListCtrl.GetItem(idx, 2).GetText() #boots_taken
        hours_count = int(self.iceRingListCtrl.GetItem(idx, 4).GetText()) #hours_cout
        customer_id = int(self.iceRingListCtrl.GetItem(idx, 6).GetText()) #customer_id
        were_boots = True

        if boots_taken == 'Tak':
            were_boots = True
        elif boots_taken == 'Nie':
            were_boots = False

        self.bookkeeper.save_entry_to_data_base(customer_id=customer_id, hours_count=hours_count, were_boots=were_boots)

        ####################################################
        self.iceRingListCtrl.DeleteItem(idx)
        countInt = self.iceRingListCtrl.GetItemCount()
        self.peopleCounterTextCtrl.SetValue(str(countInt))

    def addTimeForClient(self, evt):
        index = self.iceRingListCtrl.GetNextSelected(-1)
        boughtHoursStr = self.iceRingListCtrl.GetItem(index, 4).GetText()
        updated_bought_hours = int(boughtHoursStr) + 1
        self.iceRingListCtrl.SetStringItem(index, 4, str(updated_bought_hours))

    def printRaport(self, evt):
        self.bookkeeper.printAll()

    def onTick(self, evt):
        to_be_moved.updateTimesOnParticipantList(self.iceRingListCtrl)

    def onAddNewCustomer(self, evt):
        dialog = to_be_moved.AddNewClientDialog(None)
        dialog.ShowModal()
        dialog.Destroy()

    def onModifyClientData(self, evt):
        try:
            dialog = to_be_moved.ModifyClientDataDialog(None, self.searchListCtrl)
            dialog.ShowModal()
            dialog.Destroy()
        except:
            print "No record selected on searchList"

    def onCustomEntry(self, evt):
       # dialog = None
        try:
            dialog = to_be_moved.CustomEntryDialog(None, self.searchListCtrl, self.iceRingListCtrl,
                self.peopleCounterTextCtrl, self.bookkeeper)
            dialog.ShowModal()
            dialog.Destroy()
        except:
            print "No record selected on searchList"

if __name__ == "__main__":
    # wxGlade default stuff
    app = wx.App()
    wx.InitAllImageHandlers()
    mFrame = mainFrame(None)
    mFrame.Show()
    app.MainLoop()
