import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Menu Example")
            
        self.menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileNewMenu = fileMenu.Append(wx.ID_ANY, "새 파일")
        fileOpenMenu = fileMenu.Append(wx.ID_ANY, "열기")
        fileMenu.AppendSeparator()
        fileExitMenu = fileMenu.Append(wx.ID_ANY, "끝내기")

        customMenu = wx.Menu()
        customHelloMenu = customMenu.Append(wx.ID_ANY, "&Hello", )
        self.menuBar.Append(fileMenu, "&File")
        self.menuBar.Append(customMenu, "&Test")
        self.SetMenuBar(self.menuBar)

        self.Bind(wx.EVT_MENU, self.OnNew, fileNewMenu)
        self.Bind(wx.EVT_MENU, self.OnOpen, fileOpenMenu)
        self.Bind(wx.EVT_MENU, self.OnExit, fileExitMenu)        
        self.Bind(wx.EVT_MENU, self.OnHello, customHelloMenu)
    
    def OnNew(self, e):
        wx.MessageBox("OnNew() Clicked!")

    def OnOpen(self, e):
        wx.MessageBox("OnOpen() Clicked!")

    def OnExit(self, e):
        self.Close()

    def OnHello(self, e):
        wx.MessageBox("Hello.");

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()