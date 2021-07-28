import googletrans 
from googletrans import Translator
from tkinter import *
from PIL import Image, ImageTk
def clear():
	box.delete(1.0,END)
	box1.delete(1.0,END)
def trans():
	n=box.get(1.0,END)
	t=Translator()
	a=t.translate(n,src="vi",dest="ja")
	box1.insert(END,a.text)

base=Tk()
base.title('Translation')
base.geometry("500x600")
base.iconbitmap('logo_icon.ico')

img_load=Image.open('bg.jpg')
render=ImageTk.PhotoImage(img_load)
img=Label(base,image=render)
img.place(x=0,y=0)

box=Text(base,width=35,height=10,font=("dlx",16))
box.pack(pady=25)

button_frame=Frame(base).pack(side=BOTTOM)

clear_button=Button(button_frame,text="Clear",font=(("Arial"),12,'bold'),bg='#303030',fg='#FFFFFF',command=clear)
clear_button.place(x=150,y=280)
trans_button=Button(button_frame,text="Translate",font=(("Arial"),12,'bold'),bg='#303030',fg='#FFFFFF',command=trans)
trans_button.place(x=290,y=280)

box1=Text(base,width=35,height=10,font=("dlx",16))
box1.pack(pady=25)

base.mainloop()