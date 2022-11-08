from tkinter import *
from pygame import mixer
import PIL

file = "unnatural.mp3"
playlist = Tk()

player_status = "STOP"

mixer.init()
mixer.music.load(file)
playlist.title("My playlist")
playlist.geometry("700x700+550+350")
playlist.resizable(width=TRUE, height=TRUE)


def play_music():
    global player_status
    mixer.music.play()
    player_status = "PLAY"


def pause_music():
    global player_status
    if player_status == "PLAY":
        mixer.music.pause()
        player_status = "PAUSE"
    elif player_status == "PAUSE":
        mixer.music.unpause()
        player_status = "PLAY"


def stop_music():
    mixer.music.stop()


label1 = Label(playlist, text="Title", fg='skyblue')
label1.pack(side=TOP)
label2 = Label(playlist, text="Singer", fg='black')
label2.pack(side=TOP)

photo = PhotoImage(file="play button.png")
photo2 = PhotoImage(file="stop button.png")
photo3 = PhotoImage(file="pause button.png")
photo4 = PhotoImage(file="Happy face.png")

label3 = Label(playlist, image=photo4)
label3.pack()
button1 = Button(playlist, width=75, height=75, image=photo, command=play_music)
button1.place(x=200, y=500)
button2 = Button(playlist, width=75, height=75, image=photo2, command=pause_music)
button2.place(x=300, y=500)
button3 = Button(playlist, width=75, height=75, image=photo3, command=stop_music)
button3.place(x=400, y=500)
playlist.mainloop()