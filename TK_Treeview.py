import tkinter.ttk
from tkinter import *

window = tkinter.Tk()
window.title("ACUOUS")
window.geometry("640x400+100+100")

def cc(tag):
    print(tag)
    #treeview.tag_configure("tag2", fg="yellow")

treeview2 = tkinter.ttk.Treeview(window)
treeview = tkinter.ttk.Treeview(window, columns=["one", "two", "three", "four", "five"], displaycolumns=["two", "one", "three", "four", "five"])
treeview2.pack(side=LEFT, expand=YES, padx=0, pady=5, ipadx=5, ipady=5)
treeview.pack(side=LEFT, expand=YES, padx=0, pady=5, ipadx=5, ipady=5)


treeview.column("one", width=100, anchor="center")
treeview.heading("one", text="등록번호", anchor="center")

treeview.column("two", width=50, anchor="center")
treeview.heading("two", text="이름", anchor="center")

treeview.column("three", width=50, anchor="center")
treeview.heading("three", text="나이", anchor="center")

treeview.column("four", width=50, anchor="center")
treeview.heading("four", text="성별", anchor="center")

treeview.column("five", width=100, anchor="center")
treeview.heading("five", text="진단명", anchor="center")

treelist = [["1","2","3","4","5"], ["1","2","3","4","5"]]

for i in range(len(treelist)):
    treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i) + "번")

top = treeview2.insert('', 'end', text=str(len(treelist)), iid="7번", tags="tag1")
top_mid1 = treeview2.insert(top, 'end', text="5-2", values=["SOH", 1], iid="6번-1")
top_mid2 = treeview2.insert(top, 0, text="5-1", values=["NUL", 1], iid="6번-0", tags="tag2")
top_mid3 = treeview2.insert(top, 'end', text="5-3", values=["STX", 2], iid="6번-2", tags="tag2")

treeview2.tag_bind("tag1", sequence="<<TreeviewSelect>>", callback=cc)

window.mainloop()