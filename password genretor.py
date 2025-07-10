from tkinter import *
import string
import random
#import pyperclip

equ = ""

def generator():
    global equ
    small_alpha=string.ascii_lowercase
    capital_alpha=string.ascii_uppercase
    numbers=string.digits
    special_char=string.punctuation

    all=small_alpha+capital_alpha+numbers+special_char
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alpha,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alpha+capital_alpha+numbers,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


  #  password=random.sample(all,password_length
    #passwordField.insert(0,password)"""

"""def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)"""


root=Tk()
root.title("Password Generator") 
root.resizable(False,False)
root.configure(bg="#17161b")


choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text="Password generator",font=("times new roman",20,"bold"),bg="gray20",fg="white")
passwordLabel.grid()
weakradioButton=Radiobutton(root,text="Weak",value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text="Medium",value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

hardradioButton=Radiobutton(root,text="Hard",value=3,variable=choice,font=Font)
hardradioButton.grid(pady=5)

passwordlenght=Label(root,text="Password lenght",font=("times new roman",20,"bold"),bg="gray20",fg="white")
passwordlenght.grid(pady=30)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

generateButton=Button(root,text="Generate",font=("times new roman,",20,"bold"),bg="#fe9037",fg="white",command=generator)
generateButton.grid(pady=15)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid()

copyButton=Button(root,text="Copy",font=("times new roman,",15,"bold"),fg="#fff",bg="#3697f5")
copyButton.grid(pady=10)
