import  tkinter as tk
from tkinter import *
import pyttsx3


engine=pyttsx3.init()

def starDay():
    engine.say("Olá! Vamos começar o dia?")


def speaknow():
    engine.setProperty("voice","brazil")
    engine.setProperty("rate",230)
    engine.say(texttv.get())
    engine.runAndWait()
    engine.stop()

root=Tk()

texttv=StringVar()

obj=LabelFrame(root,text="O que você deseja?",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Escreva",font=12)
lbl.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=texttv,font=30,width=20,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="Falar",font=20,bg="#656565",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)




root.title("Alfred")
root.geometry("400x200")
root.resizable(False,False)
root.mainloop()