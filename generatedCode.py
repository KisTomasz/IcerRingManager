# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


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

        self.nameTexController = wx.TextCtrl(self, wx.ID_ANY, u"Imię...", wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizerForDataEntry.Add(self.nameTexController, 1, wx.ALL | wx.EXPAND, 5)

        self.surnameTextCtrl = wx.TextCtrl(self, wx.ID_ANY, u"Nazwisko...", wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizerForDataEntry.Add(self.surnameTextCtrl, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        leftSideGridSizer.Add(boxSizerForDataEntry, 1, wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.searchListCtrl = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        leftSideGridSizer.Add(self.searchListCtrl, 1, wx.ALL | wx.EXPAND, 5)

        boxSizerButtons = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"Wpuść", wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizerButtons.Add(self.m_button13, 0, wx.ALL, 5)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"Modyfikuj dane", wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizerButtons.Add(self.m_button15, 0, wx.ALL, 5)

        self.m_button16 = wx.Button(self, wx.ID_ANY, u"Niestandardowe wejście", wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizerButtons.Add(self.m_button16, 0, wx.ALL, 5)

        leftSideGridSizer.Add(boxSizerButtons, 1, wx.EXPAND, 5)

        mainLayoutManager.Add(leftSideGridSizer, 1, wx.BOTTOM | wx.EXPAND, 5)

        self.separatorStaticline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        mainLayoutManager.Add(self.separatorStaticline, 0, wx.EXPAND | wx.ALL, 5)

        rightFlexGridSizer = wx.FlexGridSizer(0, 1, 0, 0)
        rightFlexGridSizer.AddGrowableCol(0)
        rightFlexGridSizer.AddGrowableRow(1)
        rightFlexGridSizer.SetFlexibleDirection(wx.BOTH)
        rightFlexGridSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)

        self.lodowisko_staticText = wx.StaticText(self, wx.ID_ANY, u"Lodowisko:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lodowisko_staticText.Wrap(-1)
        rightFlexGridSizer.Add(self.lodowisko_staticText, 0, wx.ALL, 5)

        self.m_listCtrl1 = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        rightFlexGridSizer.Add(self.m_listCtrl1, 0, wx.ALL | wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.peopleCounterStaticText = wx.StaticText(self, wx.ID_ANY, u"Liczba osób:", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.peopleCounterStaticText.Wrap(-1)
        bSizer5.Add(self.peopleCounterStaticText, 0, wx.TOP, 5)

        self.peopleCounterTextCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.peopleCounterTextCtrl.Enable(False)

        bSizer5.Add(self.peopleCounterTextCtrl, 0, wx.ALL, 5)

        rightFlexGridSizer.Add(bSizer5, 1, wx.EXPAND, 5)

        mainLayoutManager.Add(rightFlexGridSizer, 1, wx.EXPAND, 5)

        self.SetSizer(mainLayoutManager)
        self.Layout()
        self.menuBar = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.addNewClientMenuItem = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Dodaj nowego klienta", wx.EmptyString,
                                                wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.addNewClientMenuItem)

        self.menuBar.Append(self.m_menu1, u"Menu")

        self.raportsMenu = wx.Menu()
        self.dummyMenuItem = wx.MenuItem(self.raportsMenu, wx.ID_ANY, u"raport sesji", wx.EmptyString, wx.ITEM_NORMAL)
        self.raportsMenu.AppendItem(self.dummyMenuItem)

        self.menuBar.Append(self.raportsMenu, u"Raporty")

        self.SetMenuBar(self.menuBar)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == "__main__":
    # wxGlade default stuff
    app = wx.App(0)
    wx.InitAllImageHandlers()
    mFrame = mainFrame(None)
    mFrame.Show()
    app.MainLoop()