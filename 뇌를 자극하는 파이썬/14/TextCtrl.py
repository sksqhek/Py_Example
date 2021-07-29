import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="TextCtrl Example")
        self.SetSize(280, 130)
        self.mainPanel = wx.Panel(self)
        
        self.staticRed = wx.StaticText(self.mainPanel, label="Red : ")
        self.textRed = wx.TextCtrl(self.mainPanel, value='255')
        self.staticGreen = wx.StaticText(self.mainPanel, label="Green : ")
        self.textGreen = wx.TextCtrl(self.mainPanel, value='255')
        self.staticBlue = wx.StaticText(self.mainPanel, label="Blue : ")
        self.textBlue = wx.TextCtrl(self.mainPanel, value='255')
        
        self.gridSizer = wx.GridSizer(rows=3, cols=2, hgap=5, vgap=5)
        self.gridSizer.Add(self.staticRed)
        self.gridSizer.Add(self.textRed, 0, wx.EXPAND)
        self.gridSizer.Add(self.staticGreen)
        self.gridSizer.Add(self.textGreen, 0, wx.EXPAND)
        self.gridSizer.Add(self.staticBlue)
        self.gridSizer.Add(self.textBlue, 0, wx.EXPAND)

        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.gridSizer, 1, wx.EXPAND|wx.ALL, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_TEXT, self.OnTextChange, self.textRed)
        self.Bind(wx.EVT_TEXT, self.OnTextChange, self.textGreen)
        self.Bind(wx.EVT_TEXT, self.OnTextChange, self.textBlue)
        self.ChangeColor()

    def OnTextChange(self, e):
        self.ChangeColor();

    def ChangeColor(self):
        r = int(self.textRed.GetValue())
        g = int(self.textGreen.GetValue())
        b = int(self.textBlue.GetValue())
        self.mainPanel.SetBackgroundColour(wx.Colour(r, g, b))
        self.mainPanel.Refresh()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()