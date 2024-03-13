import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x645+400+100")
root .resizable(False, False)

task_list = []

Image_icon = PhotoImage(file="images/checklist.png")
root.iconphoto(False, Image_icon)

TopImage = PhotoImage(file="images/progress.png")
Label(root, image = TopImage).pack()

dockImage = PhotoImage(file="images/new-blank-page.png")
Label(root, image=dockImage).place(x=5, y=130)

noteImage = PhotoImage(file="images/checklist2.png")
Label(root, image = noteImage, bg="#32405b").place(x=25, y=30)

frame = Frame(root,width=351, height=50, bg="lightgray")
frame.place(x=22, y=140)

task = StringVar()
task_entry = Entry(frame, width=22, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="Add", font="arial 20 bold", width=6, bg="lightgray", fg="#fff", bd=0)
button.place(x=236, y=0)

frame1 = Frame(root, bd=3, width = 260, height = 250, bg = "black")
frame1.pack(pady=(50,0))

listbox = Listbox(frame1, font=('arial', 12), width = 37, height = 16, bg = "lightgray", fg="white", cursor="hand2", selectbackground="white")
listbox.pack(side=LEFT, padx=0)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Delete_icon = PhotoImage(file="images/trash-bin.png")
Button(root, image=Delete_icon, bd = 0).place(x=140, y=520)

root.mainloop()