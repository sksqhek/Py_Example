import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="CheckBox Example")
        self.SetSize(280, 130)
        self.mainPanel = wx.Panel(self)
        
        self.checkBold = wx.CheckBox(self.mainPanel, label="Bold")
        self.checkBold.SetValue(wx.CHK_CHECKED) 

        self.checkItalic = wx.CheckBox(self.mainPanel, label="Italic")
        self.checkItalic.SetValue(wx.CHK_UNCHECKED)
        
        self.staticText = wx.StaticText(self.mainPanel, 
                                        label="I am a Programmer.")        

        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.checkBold, 1, wx.ALL, 5)
        self.vtBoxSizer.Add(self.checkItalic, 1, wx.ALL, 5)
        self.vtBoxSizer.Add(self.staticText, 1, wx.EXPAND | wx.ALL, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_CHECKBOX, self.OnCheck, self.checkBold)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheck, self.checkItalic)
        self.ChangeFont()

    def OnCheck(self, e):
        self.ChangeFont()

    def ChangeFont(self):
        style = wx.FONTSTYLE_NORMAL
        weight = wx.FONTWEIGHT_NORMAL

        if self.checkBold.GetValue() == wx.CHK_CHECKED:
            weight = wx.FONTWEIGHT_BOLD
        if self.checkItalic.GetValue() == wx.CHK_CHECKED:
            style = wx.FONTSTYLE_ITALIC

        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, style, weight)
        self.staticText.SetFont(font)

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()