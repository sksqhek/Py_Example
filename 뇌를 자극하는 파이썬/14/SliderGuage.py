import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Slider & Gauge")
        self.SetSize(300, 120)
        self.mainPanel = wx.Panel(self)

        self.slider = wx.Slider(self.mainPanel, minValue=0, maxValue=100)
        self.gauge = wx.Gauge(self.mainPanel, range=100)        
                    
        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)        
        self.vtBoxSizer.Add(self.slider, 0, wx.EXPAND|wx.ALL, 5)
        self.vtBoxSizer.Add(self.gauge, 0, wx.EXPAND|wx.ALL, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_SLIDER, self.OnSliderChange, self.slider)

    def OnSliderChange(self, e):
        self.gauge.SetValue(self.slider.GetValue())
                
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()

    app.MainLoop()