from gtts import gTTS
import os
from tkinter import *
from tkinter import messagebox
import pandas as pd

# ------------------ CONSTANTS --------------
GRAY = "#d3d3d3"
GREEN = "#9bdeac"
BLUE = "#154c79"
FONT_NAME = "Courier"
# filename = None

# -------------------- GENERATE --------------
def text_to_speech():
    text = message_entry.get()
    try:
        tts = gTTS(text=text, lang='ro')
    except:
        messagebox.showinfo(title = "Camp necompletat", message= "Completeaza campul 'Mesaj' pentru a putea rula.")
    global filename
    if len(key_entry.get())  > 0:
        filename = f'{key_entry.get()}.mp3'
    else:
        messagebox.showinfo(title = "Camp necompletat", message= "Completeaza campul 'Cod fisier' pentru a putea rula.")
    tts.save(f'./audio/{filename}')

def generate_all():
    try:
        df = pd.read_csv("./db/DB.csv",dtype = str)
    except:
        messagebox.showinfo(title="Fișierul nu a fost găsit", message="Fișierul corespunzător bazei de date nu există")
    # DB = df.to_string()
    print(df)
    print(type(df))
    for index,row in df.iterrows():
        tts = gTTS(text=row[1], lang='ro')
        tts.save(f'./audio/{row[0]}.mp3')

# --------------------- PLAY ------------------
def play():
    
    try:
        global filename
        os.system(f"start ./audio/{filename}")
    except:
        messagebox.showinfo(title = "Fisierul nu a fost gasit! ", message= "Pentru a rula un fisier audio mai intai acesta trebuie generat")
        
# ---------------------- UI --------------------
# creare fereastră și setare titlu
window = Tk()
window.title("Convertor de Text în Vorbire")
window.config(padx=40,pady=40,bg=GRAY, highlightthickness=0)

canvas = Canvas(width=400, height=200,bg=GRAY)

# adaugare titlu
title_label = Label(text="Convertor de Text în Vorbire",fg=BLUE, bg=GRAY, font=(FONT_NAME,30,"bold"))
title_label.grid(column=1, row=0)

# adaugare imagine
logo_img = PhotoImage(file="./contents/tts.png")
canvas.create_image(200, 100, image=logo_img)
canvas.config(highlightthickness=0)
canvas.grid(row=1,column=1)

# creare etichetă pentru caseta introducere text
message_label = Label(text="Mesajul tău",bg=GRAY, font=(FONT_NAME,10))
message_label.grid(column=0, row=3)

# creare case de introducere text pentru mesaj
message_entry = Entry(width=66)
message_entry.insert(END, string="")
message_entry.focus()
message_entry.grid(column=1,row=3)

# creare buton de generare manuala
generate_button = Button(text="Generează sunet", command=text_to_speech)
generate_button.config(width=15, )
generate_button.grid(column=2,row=3)

# creare buton pentru redarea continutul anterior generat 
play_button = Button(text="Redă sunet", command=play)
play_button.config(width=15, )
play_button.grid(column=2,row=4)


# creare buton pentru generarea automată a fisierelor audio
generate_all_button = Button(text="Genereaza din CSV", command=generate_all)
generate_all_button.config(width=15, )
generate_all_button.grid(column=2,row=5)

# creare caseta de introduce cheie pentru denumirea fișierului
key_entry = Entry(width=10)
key_entry.insert(END, string="")
key_entry.grid(column=1,row=4)

# creare etichetă pentru caseta de introducere cheie
key_label = Label(text="Cod fisier:",bg=GRAY, font=(FONT_NAME,10))
key_label.grid(column=0, row=4)

window.mainloop()
