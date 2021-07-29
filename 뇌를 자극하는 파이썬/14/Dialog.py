import wx

class MyDialog(wx.Dialog):
    def __init__(self, _parent, _title):
        wx.Dialog.__init__(self, parent=_parent, title=_title)
        self.SetSize(160, 80)
        self.mainPanel = wx.Panel(self)        
        self.closekButton = wx.Button(self.mainPanel, label="Close")

        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)        
        self.vtBoxSizer.Add(self.closekButton, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_BUTTON, self.OnClose, self.closekButton)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, e):        
        self.Destroy()
        
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Modal & Modeless")
        self.SetSize(300, 180)
        self.mainPanel = wx.Panel(self)

        self.modalButton = wx.Button(self.mainPanel, label="Modal")
        self.ModelessButton = wx.Button(self.mainPanel, label="Modeless")
                     
        self.fgridSizer = wx.FlexGridSizer(rows=1, cols=2, hgap=5, vgap=5) 
        self.fgridSizer.Add(self.modalButton, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        self.fgridSizer.Add(self.ModelessButton, 0, wx.ALIGN_RIGHT|wx.ALL, 5)
        self.fgridSizer.AddGrowableCol(1)
        self.mainPanel.SetSizer(self.fgridSizer)

        self.Bind(wx.EVT_BUTTON, self.OnModalButton, self.modalButton)
        self.Bind(wx.EVT_BUTTON, self.OnModelessButton, self.ModelessButton)

    def OnModalButton(self, e):
        dlg = MyDialog(self, "Modal Dialog")
        dlg.ShowModal()

    def OnModelessButton(self, e):
        dlg = MyDialog(self, "Modeless Dialog")
        dlg.Show()        
 
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()