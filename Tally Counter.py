from tkinter import *

say=0

def tikla(): #Tikla means Click
    global say
    say+=1
    etiket.config(text=say)

def sifir(): #Sifir means "Reset"
    global say
    say=0
    etiket.config(text=say)

def geri(): #Geri means "Undo"
    global say
    say -=1
    etiket.config(text=say)


#Pencereayar ve ilk tus (Window Settings and frist button)
rot=Tk()
rot.title("Tally Counter")
rot.geometry("250x350")
rot.config(bg="#dfd7f9")
rot.iconbitmap("applogoo.ico")
button=Button(rot,text="Count")
button.config(font=('Arial',33,))
button.config(bg="#382700")
button.config(fg="#ffd900")
button.config(activebackground="#ff6200")
button.config(command=tikla)
clickk=PhotoImage(file="clickk.png")
button.config(image=clickk)
button.config(compound="right")
etiket=Label(rot,font=("Arial",50),text=say)
etiket.config(bg="#dfd7f9")
#Reset Button
reset_button = Button (rot, text="Reset", font=('Arial', 36 ),command=sifir)
reset_button.config(fg="#42361B",bg="#a89528")
reset_button.config(activebackground="#b04f13")

#Undo button
geributton=Button (rot, text="Undo", font=('Arial', 35 ))
geributton.config(fg="#210200",bg="#dabd78")
geributton.config(activebackground="#6e433f")
undo=PhotoImage(file="undoimage.png")
geributton.config(image=undo)
geributton.config(compound="right")
geributton.config(command=geri)

#Gui yerlestir (Place buttons (pack))
etiket.pack()
button.pack()
geributton.pack()
reset_button.pack()

#Pencere dongusu (Window loop)
rot.mainloop()
