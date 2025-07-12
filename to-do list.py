import tkinter
from tkinter import *


root=Tk()
root.title("To-Do List")
root.geometry("400x600+400+100")
root.resizable(False,False)

task_list= []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt","a")as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)

def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")

        listbox.delete(ANCHOR)


def openTaskFile():
    try:
        
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END ,task)

    except:
            file=open('tasklist.txt','w')
            file.close()
    

#icon

Image_icon=PhotoImage(file="D:\\DOWNLOADS\\Images\\icon.png")
root.iconphoto(False,Image_icon)

#top bar
TopImage=PhotoImage(file="D:\\DOWNLOADS\\Images\\topbar.png")
Label(root,image=TopImage).pack()

#dots img
dockImage=PhotoImage(file="D:\\DOWNLOADS\\Images\\dock.png")
Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)


noteImage=PhotoImage(file="D:\\DOWNLOADS\\Images\\task.png")
Label(root,image=noteImage,bg="#32405b").place(x=340,y=24)

Heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b")
Heading.place(x=130,y=24)


#main
frame= Frame(root,width=400,height=50,bg="#daf7f9",bd=0)
frame.place(x=0,y=150)

"""#command=Label(root,text="Enter the task")"""

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)#bg="#daf7f9")
task_entry.place(x=10,y=7)
"""#task_entry.focus()"""

button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#0c9bfc",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)


#listB0x
frame1= Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(120,0))

listbox= Listbox(frame1,font=("arial",12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side= RIGHT, fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile()


#delete
Delete_icon=PhotoImage(file="D:\\DOWNLOADS\\Images\\delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)


root.mainloop()
