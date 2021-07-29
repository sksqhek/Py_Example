import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="TreeCtrl Example")
        self.SetSize(420, 320)
        self.mainPanel = wx.Panel(self)
        self.expandButton = wx.Button(self.mainPanel, 
                                        label="Expand")        

        self.tree = wx.TreeCtrl(self.mainPanel)
        root = self.tree.AddRoot('태조')
        self.tree.AppendItem(root, '방우')
        self.tree.AppendItem(root, '정종(방과)')
        self.tree.AppendItem(root, '방의')
        self.tree.AppendItem(root, '방간')
        taejong = self.tree.AppendItem(root, '태종(방원)')
        self.tree.AppendItem(root, '방연')

        self.tree.AppendItem(taejong, '양녕')
        self.tree.AppendItem(taejong, '효령')
        self.tree.AppendItem(taejong, '세종(충녕)')
        self.tree.AppendItem(taejong, '효령')

        self.staticText = wx.StaticText(self.mainPanel, 
                                        style=wx.ALIGN_CENTER)
                    
        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)        
        self.vtBoxSizer.Add(self.expandButton, 0, wx.EXPAND|wx.ALL, 5)
        self.vtBoxSizer.Add(self.tree, 5, wx.EXPAND|wx.ALL, 5)
        self.vtBoxSizer.Add(self.staticText, 0, wx.EXPAND|wx.ALL, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_BUTTON, self.OnExpandButton, self.expandButton)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnNodeSelected, self.tree)

    def OnExpandButton(self, e):
        self.tree.ExpandAll()

    def OnNodeSelected(self, e):
        selected = self.tree.GetSelection()
        self.staticText.SetLabel(self.tree.GetItemText(selected))
        self.mainPanel.Layout()
        
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()