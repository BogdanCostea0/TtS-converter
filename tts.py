from gtts import gTTS
import os
from tkinter import *
import pandas as pd
# ------------------ CONSTANTS --------------
GRAY = "#d3d3d3"
GREEN = "#9bdeac"
BLUE = "#154c79"
FONT_NAME = "Courier"
# filename = None
DEX = {}

# -------------------- GENERATE --------------
def text_to_speech():
    text = message_entry.get()
    tts = gTTS(text=text, lang='ro')
    global filename
    filename = f'{key_entry.get()}.mp3' 
    tts.save(filename)
    DEX[f'{key_entry.get()}']=f'{message_entry.get()}'
    print(DEX)

def generate_all():
    df = pd.read_csv("./db/DB.csv",dtype = str)
    # DB = df.to_string()
    print(df)
    print(type(df))
    for index,row in df.iterrows():
        
        # print(row[0],row[1])
        # text = row[1]
        tts = gTTS(text=row[1], lang='ro')
        # global filename
        # filename = f'{row[0]}.mp3' 
        tts.save(f'./audio/{row[0]}.mp3')

# --------------------- PLAY ------------------
def play():
    global filename
    try:
        os.system(f"start {filename}")
    except:
        
# ---------------------- UI --------------------
window = Tk()
window.title("Text to Speech Converter")
window.config(padx=40,pady=40,bg=GRAY, highlightthickness=0)

canvas = Canvas(width=400, height=200,bg=GRAY)

title_label = Label(text="Text to Speech Converter",fg=BLUE, bg=GRAY, font=(FONT_NAME,30,"bold"))
title_label.grid(column=1, row=0)

logo_img = PhotoImage(file="./contents/tts.png")
canvas.create_image(200, 100, image=logo_img)
canvas.config(highlightthickness=0)
canvas.grid(row=1,column=1)

message_label = Label(text="Your message",bg=GRAY, font=(FONT_NAME,10))
message_label.grid(column=0, row=3)

message_entry = Entry(width=66)
message_entry.insert(END, string="")
message_entry.focus()
message_entry.grid(column=1,row=3)

generate_button = Button(text="Generate sound", command=text_to_speech)
generate_button.config(width=15, )
generate_button.grid(column=2,row=3)

play_button = Button(text="Play sound", command=play)
play_button.config(width=15, )
play_button.grid(column=2,row=4)

generate_all_button = Button(text="Generate all from csv", command=generate_all)
generate_all_button.config(width=15, )
generate_all_button.grid(column=2,row=5)

key_entry = Entry(width=10)
key_entry.insert(END, string="")
key_entry.grid(column=1,row=4)

key_label = Label(text="Cod fisier:",bg=GRAY, font=(FONT_NAME,10))
key_label.grid(column=0, row=4)

window.mainloop()
