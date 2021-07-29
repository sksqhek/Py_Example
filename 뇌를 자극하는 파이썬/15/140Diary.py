from datetime import datetime
import sqlite3
import wx 
import wx.html2 # HTML Window
import ntpath # FILE NAME Extraction
import base64 # IMAGE URI Encoding
 
RECORD_PER_PAGE = 5

class MainFrame (wx.Frame):
    def __init__(self):
        wx.Frame.__init__ (self, 
                           None, 
                           title = "140자 일기장", 
                           size = wx.Size(715,655), 
                           style = wx.DEFAULT_FRAME_STYLE)
        
        self.MaxImageSize = 200
        
        self.mainPanel = wx.Panel(self)
        
        # 일기 입력 창
        self.leftPanel = wx.Panel(self.mainPanel)
        self.leftPanel.SetMaxSize(wx.Size(200,-1))        
        self.input_image_path = ""
        self.inputTextCtrl = wx.TextCtrl(
            self.leftPanel, size=wx.Size(200,100), style=wx.TE_MULTILINE)

        self.inputTextCtrl.SetMaxLength(140)
        self.inputTextCtrl.Bind(wx.EVT_TEXT, self.OnTypeText)
        self.lengthStaticText = wx.StaticText(self.leftPanel, style=wx.ALIGN_RIGHT)
        self.selectImageButton = wx.Button(self.leftPanel, label="이미지 추가")
        self.selectImageButton.Bind(wx.EVT_BUTTON, self.OnFindImageFile)
        self.imageStaticBitmap = wx.StaticBitmap(self.leftPanel)        
        self.inputButton = wx.Button(self.leftPanel, label="저장")
        self.inputButton.Bind(wx.EVT_BUTTON, self.OnInputButton)
        
        # 일기 표시 창
        self.rightPanel = wx.Panel(self.mainPanel)
        self.outputHtmlWnd = wx.html2.WebView.New(self.rightPanel)
        self.outputHtmlWnd.Bind(wx.html2.EVT_WEBVIEW_NAVIGATING, self.OnNavigating)

        # 위젯 배치        
        leftPanelSizer = wx.StaticBoxSizer(
            wx.VERTICAL, self.leftPanel, "글 남기기")
        leftPanelSizer.Add(self.inputTextCtrl, 0, wx.ALL, 5)
        leftPanelSizer.Add(self.lengthStaticText, 0, wx.ALIGN_RIGHT|wx.RIGHT, 5)
        leftPanelSizer.Add(self.selectImageButton, 0, wx.ALIGN_RIGHT|wx.RIGHT, 5)
        leftPanelSizer.Add(self.imageStaticBitmap, 0, wx.ALIGN_RIGHT|wx.ALL, 5)
        leftPanelSizer.Add(self.inputButton, 0, wx.ALIGN_RIGHT|wx.RIGHT, 5)
        self.leftPanel.SetSizer(leftPanelSizer)
        
        htmlWndSizer = wx.GridSizer(1, 1, 0, 0)
        htmlWndSizer.Add(self.outputHtmlWnd, 0, wx.ALL|wx.EXPAND, 5)

        self.rightPanel.SetSizer(htmlWndSizer)
        self.rightPanel.Layout()
        htmlWndSizer.Fit(self.rightPanel)
        
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(self.leftPanel, 1, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(self.rightPanel, 1, wx.ALL|wx.EXPAND , 5)
        self.mainPanel.SetSizer(mainSizer)
        self.Layout()

        # Database 초기화
        self.conn = sqlite3.connect("minutediary.db")
        self.cursor = self.conn.cursor()
        self.CheckSchema()
        self.LoadDiary(0)
                
    def CheckSchema(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS DIARY (
        DIARY_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        CREATEDATE DATETIME, 
        NOTE CHAR(140))
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS DIARY_IMG (
        IMG_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        IMG BLOB, 
        DIARY_ID INTEGER, 
        FOREIGN KEY(DIARY_ID) REFERENCES DIARY(DIARY_ID))
        """)

    def OnTypeText(self, event):
        self.lengthStaticText.SetLabel(
            "현재 글자 수 : {0}".format(len(self.inputTextCtrl.GetValue())))
        self.leftPanel.Layout()

    def OnFindImageFile(self, event):
        openFileDialog = wx.FileDialog(
            self, "Open", 
            wildcard="Image files (*.png, *.jpg, *.gif)|*.png;*.jpg;*.jpeg;*.gif",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if openFileDialog.ShowModal() == wx.ID_OK:
            self.input_image_path = openFileDialog.GetPath()
            
            # 비율을 유지하면서 이미지 크기를 윈도우에 맞추기
            img = wx.Image(self.input_image_path, wx.BITMAP_TYPE_ANY)
            Width = img.GetWidth()
            Height = img.GetHeight()
            if Width > Height:
                NewWidth = self.MaxImageSize
                NewHeight = self.MaxImageSize * Height / Width
            else:
                NewWidth = self.MaxImageSize
                NewHeight = self.MaxImageSize * Width / Height
            img = img.Scale(NewWidth, NewHeight)
            self.imageStaticBitmap.SetBitmap(wx.Bitmap(img))
            self.leftPanel.Layout()
            self.leftPanel.Refresh()
        
        openFileDialog.Destroy()

    def OnInputButton(self, event):
        fileName = ntpath.basename(self.input_image_path)
        self.cursor.execute(
            "INSERT INTO DIARY (DIARY_ID, CREATEDATE, NOTE) VALUES(NULL, ?, ? )", 
            (str(datetime.now()), self.inputTextCtrl.GetValue()))

        diary_id = self.cursor.lastrowid

        if self.input_image_path.strip() != "":
            self.cursor.execute(
                "INSERT INTO DIARY_IMG (IMG_ID, IMG, DIARY_ID) VALUES(NULL, ?, ?)",
                (sqlite3.Binary(open(self.input_image_path,"rb").read()), 
                 diary_id))
        
        self.conn.commit()

        wx.MessageBox("저장되었습니다.", "140자 일기장", wx.OK) 

        self.inputTextCtrl.SetValue("")        
        self.input_image_path = ""
        self.imageStaticBitmap.SetBitmap(wx.Bitmap(0,0))

        self.leftPanel.Layout()
        self.leftPanel.Refresh()
        self.LoadDiary(0)

    def LoadDiary(self, page):
        self.cursor.execute(
            "SELECT D.DIARY_ID, D.CREATEDATE, D.NOTE, I.IMG FROM DIARY "
            + "AS D LEFT OUTER JOIN DIARY_IMG AS I "
            + "ON D.DIARY_ID = I.DIARY_ID ORDER BY D.CREATEDATE DESC "
            + "LIMIT {0} OFFSET {1}"
            .format(RECORD_PER_PAGE, page*RECORD_PER_PAGE))

        html = """
            <html>
            <head>
            </head><body>{0}</body></html>
            """
        diary_id = 0
        body = ""
        for row in self.cursor:
            diary_id = int(row[0]);
            imgTag = ""
            if row[3] != None:
                imgTag = """<img src='data:image/png;base64,{0}' 
                style='width:300px; height:auto;' align=center>
                """.format(
                    base64.b64encode(row[3]).decode("ascii")
                    )

            content = """<a name="neural">
                <p style="word-wrap:break-word;font-size=12px;">
                <font size=2><b><i>
                {1}
                </i></b>
                <a href="del:{0}">[삭제]</a></font><br>
                {2}
                <br>
                {3}
                """.format(diary_id, row[1], row[2], imgTag)
            body += content

        pageNavigation = "<p align='center' style='font-size=12px'>"
        
        # Prev 버튼(링크)
        if page > 0:
            pageNavigation += "<a href='nav:{0}'>Prev</a>".format(page - 1)
        
        pageNavigation += "&nbsp;"

        # Next 버튼(링크)
        self.cursor.execute(
            "SELECT count(*) FROM DIARY WHERE DIARY_ID<{0}".format(diary_id))
        row = self.cursor.fetchone() 
        
        if row != None:
            nextRowCount = row[0]
            if nextRowCount > 0:
                pageNavigation += "<a href='nav:{0}'>Next</a>".format(page + 1)

        pageNavigation += "</p>"
        body += pageNavigation

        self.outputHtmlWnd.SetPage(html.format(body), "")

    def OnNavigating(self, event):
        if event.URL.startswith("del:") == True:
            diary_id = event.URL.rpartition(":")[-1]
            self.cursor.execute(
                "DELETE FROM DIARY WHERE DIARY_ID={0}".format(diary_id))
            self.cursor.execute(
                "DELETE FROM DIARY_IMG WHERE DIARY_ID={0}".format(diary_id))
            self.conn.commit()
            self.LoadDiary(0)
            wx.MessageBox("삭제했습니다.", "140자 일기장", wx.OK)
        elif event.URL.startswith("nav:") == True:
            page = event.URL.rpartition(":")[-1]
            self.LoadDiary(int(page))
        
        event.Skip(False) # WebView 위젯이 해당 이벤트를 받아서 해당 URL로 이동하려는 것을 막기 위함.

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    frame.Show()

    app.MainLoop()