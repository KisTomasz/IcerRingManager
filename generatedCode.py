# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

from DataBaseController import DataBaseController


###########################################################################
## Class mainFrame
###########################################################################

class mainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1074, 606), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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

        self.nameTextCtrl = wx.TextCtrl(self, wx.ID_ANY, u"Imię...", wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizerForDataEntry.Add(self.nameTextCtrl, 1, wx.ALL | wx.EXPAND, 5)

        self.surnameTextCtrl = wx.TextCtrl(self, wx.ID_ANY, u"Nazwisko...", wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizerForDataEntry.Add(self.surnameTextCtrl, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        leftSideGridSizer.Add(boxSizerForDataEntry, 1, wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.searchListCtrl = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        self.searchListCtrl.InsertColumn(0, "id")
        self.searchListCtrl.InsertColumn(1, "Imię")
        self.searchListCtrl.InsertColumn(2, "Nazwisko")
        self.searchListCtrl.InsertColumn(3, "typ biletu")

        leftSideGridSizer.Add(self.searchListCtrl, 0, wx.ALL | wx.EXPAND, 5)

        controllButtonsBSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.enterIceringButton = wx.Button(self, wx.ID_ANY, u"Wpuść", wx.DefaultPosition, wx.DefaultSize, 0)
        controllButtonsBSizer.Add(self.enterIceringButton, 0, wx.ALL, 5)

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
        self.iceRingListCtrl.InsertColumn(0, "Imię")
        self.iceRingListCtrl.InsertColumn(1, "Nazwisko")
        self.iceRingListCtrl.InsertColumn(2, "Czy łyżwy")

        rightFlexGridSizer.Add(self.iceRingListCtrl, 0, wx.ALL | wx.EXPAND, 5)

        counterBSizer = wx.BoxSizer(wx.VERTICAL)

        self.peopleCounterStaticText = wx.StaticText(self, wx.ID_ANY, u"Liczba osób:", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.peopleCounterStaticText.Wrap(-1)
        counterBSizer.Add(self.peopleCounterStaticText, 0, wx.TOP, 5)

        self.peopleCounterTextCtrl = wx.TextCtrl(self, wx.ID_ANY, '0', wx.DefaultPosition, wx.DefaultSize, 0)
        self.peopleCounterTextCtrl.Enable(False)

        counterBSizer.Add(self.peopleCounterTextCtrl, 0, wx.ALL, 5)

        rightFlexGridSizer.Add(counterBSizer, 1, wx.EXPAND, 5)

        mainLayoutManager.Add(rightFlexGridSizer, 1, wx.EXPAND, 5)

        self.SetSizer(mainLayoutManager)
        self.Layout()
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
        self.nameTextCtrl.Bind(wx.EVT_TEXT_ENTER, self.onNameEntered)
        self.surnameTextCtrl.Bind(wx.EVT_TEXT_ENTER, self.onSurnamenEntered)
        self.enterIceringButton.Bind(wx.EVT_BUTTON, self.onEnterRiderButton)
        self.searchListCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSearchListCtrlItemSelected)
        self.iceRingListCtrl.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnIceringParticipantRightClick)

    def __del__(self):
        pass

    def onNameEntered(self, evt):
        print self.nameTextCtrl.GetValue()
        enteredMsg = self.nameTextCtrl.GetValue()
        dataBaseConroller = DataBaseController("test.db")
        foundCursor = dataBaseConroller.findByName(enteredMsg)

        for entity in foundCursor:
            print entity
            self.searchListCtrl.Append(entity)

    def onSurnamenEntered(self, evt):
        print self.surnameTextCtrl.GetValue()
        enteredMsg = self.surnameTextCtrl.GetValue()
        dataBaseConroller = DataBaseController("test.db")
        foundCursor = dataBaseConroller.findBySurname(enteredMsg)

        for entity in foundCursor:
            print entity
            self.searchListCtrl.Append(entity)

    def onSearchListCtrlItemSelected(self, evt):
        pass

    def onEnterRiderButton(self, evt):
        idx = self.searchListCtrl.GetNextSelected(-1)
        nameObj = self.searchListCtrl.GetItem(idx, 1)
        surnameObj = self.searchListCtrl.GetItem(idx, 2)
        bootsTaken = "Tak"
        self.iceRingListCtrl.Append((nameObj.GetText(), surnameObj.GetText(), bootsTaken))

        countText = self.peopleCounterTextCtrl.GetValue()
        countInt = int(countText) + 1
        self.peopleCounterTextCtrl.SetLabelText(str(countInt))

    def OnIceringParticipantRightClick(self, evt):
        idx = evt.GetIndex()
        nameObj = self.iceRingListCtrl.GetItem(idx, 0)
        surnameObj = self.iceRingListCtrl.GetItem(idx, 1)
        # self.iceRingListCtrl.Append((nameObj.GetText(), surnameObj.GetText(), False)) for development
        #menu.Destroy()  # destroy to avoid mem leak
        menu = wx.Menu()

        addClientMenuItem = wx.MenuItem(self.mainMenu, wx.ID_ANY, u"Wypuść", wx.EmptyString,
            wx.ITEM_NORMAL)


        menu.Append(addClientMenuItem)
        menu.Append(1, u'Dodaj czas')

        # menu.Bind(wx.EVT_MENU, self.printDupa)
        self.Bind(wx.EVT_MENU, self.onRemoveFromIceRingClicked, id=addClientMenuItem.GetId())
        self.Bind(wx.EVT_MENU, self.printTwo, id=1)
        self.PopupMenu(menu)
        # self.Bind(wx.EVT_MENU, self.printDupa, id=self.addClientMenuItem.GetId())

        menu.Destroy()

    def onRemoveFromIceRingClicked(self, evt):
        idx = self.iceRingListCtrl.GetNextSelected(-1)
        self.iceRingListCtrl.DeleteItem(idx)

        countText = self.peopleCounterTextCtrl.GetValue()
        countInt = int(countText) - 1
        self.peopleCounterTextCtrl.SetLabelText(str(countInt))

    def printTwo(self, evt):
        print "2"

if __name__ == "__main__":
    # wxGlade default stuff
    app = wx.App()
    wx.InitAllImageHandlers()
    mFrame = mainFrame(None)
    mFrame.Show()
    app.MainLoop()
