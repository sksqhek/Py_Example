import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="FlexGridSizer Example")
        self.SetSize(300, 170)
        self.mainPanel = wx.Panel(self)        

        self.fgridSizer = wx.FlexGridSizer(rows=3, cols=2, hgap=5, vgap=5)

        self.nameStatic  = wx.StaticText(self.mainPanel, label="Name :")
        self.emailStatic = wx.StaticText(self.mainPanel, label="Email :")
        self.phoneStatic = wx.StaticText(self.mainPanel, label="Phone :")

        self.nameText  = wx.TextCtrl(self.mainPanel)
        self.emailText = wx.TextCtrl(self.mainPanel)
        self.phoneText = wx.TextCtrl(self.mainPanel)

        self.fgridSizer.Add(self.nameStatic)
        self.fgridSizer.Add(self.nameText, 0, wx.EXPAND)
        self.fgridSizer.Add(self.emailStatic)
        self.fgridSizer.Add(self.emailText, 0, wx.EXPAND)
        self.fgridSizer.Add(self.phoneStatic)
        self.fgridSizer.Add(self.phoneText, 0, wx.EXPAND)

        # 윈도우 크기 변경시 두 번째 컬럼의 너비도 따라 변경되도록 지정함.
        self.fgridSizer.AddGrowableCol(1) 

        # 윈도우 크기 변경시 두 번째 컬럼의 너비도 따라 변경되도록 지정함.
        self.fgridSizer.AddGrowableRow(2)
        
        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.fgridSizer, 1, wx.EXPAND | wx.ALL, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)
        
        
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()