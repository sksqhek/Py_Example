import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="RadioButton Example")
        self.SetSize(380, 100)
        self.mainPanel = wx.Panel(self)
        self.mainBox = wx.StaticBox(self.mainPanel, label="Color")

        self.rdoRed     = wx.RadioButton(self.mainBox, label="Red", 
                                         style=wx.RB_GROUP)
        self.rdoGreen   = wx.RadioButton(self.mainBox, label="Green")
        self.rdoBlue    = wx.RadioButton(self.mainBox, label="Blue")
        self.rdoEnable  = wx.RadioButton(self.mainBox, label="Enable", 
                                         style=wx.RB_GROUP)
        self.rdoDisable = wx.RadioButton(self.mainBox, label="Disable")
        
        self.gridSizer = wx.GridSizer(rows=2, cols=3, hgap=5, vgap=15)
        self.gridSizer.Add(self.rdoRed)
        self.gridSizer.Add(self.rdoGreen)
        self.gridSizer.Add(self.rdoBlue)
        self.gridSizer.Add(self.rdoEnable)
        self.gridSizer.Add(self.rdoDisable)

        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.gridSizer, 1, wx.EXPAND|wx.ALL, 15)
        self.mainBox.SetSizer(self.vtBoxSizer)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.mainSizer.Add(self.mainBox, 1, wx.EXPAND|wx.ALL, 5)
        self.mainPanel.SetSizer(self.mainSizer)

        self.Bind(wx.EVT_RADIOBUTTON, self.OnRed, self.rdoRed)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnGreen, self.rdoGreen)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnBlue, self.rdoBlue)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnEnable, self.rdoEnable)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnDisable, self.rdoDisable)

    def OnRed(self, e):
        self.mainBox.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.mainBox.Refresh()

    def OnGreen(self, e):
        self.mainBox.SetBackgroundColour(wx.Colour(0, 255, 0))
        self.mainBox.Refresh()

    def OnBlue(self, e):
        self.mainBox.SetBackgroundColour(wx.Colour(0, 0, 255))
        self.mainBox.Refresh()

    def OnEnable(self, e):
        self.rdoRed.Enable(True)
        self.rdoGreen.Enable(True)
        self.rdoBlue.Enable(True)

    def OnDisable(self, e):
        self.rdoRed.Enable(False)
        self.rdoGreen.Enable(False)
        self.rdoBlue.Enable(False)
        

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()