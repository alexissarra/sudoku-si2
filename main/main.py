import tkinter as tkt 
from tkinter import ttk


def fP():
    root = tkt.Tk()
    root.title('Jeu du Sudoku') 
    root.geometry('600x400+50+50')
   # root.iconbitmap('C:/Users/ponch/Documents/GitHub/sudoku-si2/Alexis.jpg')
    message = tkt.Label(root, text="Choisissez votre difficulté")
    message.pack()

    easy_button = ttk.Button(
        root,
        text='Simple',
        command = f1
    )
    easy_button.pack(
        ipadx=5,
        ipady=5,
        expand=False
    )
    normal_button = ttk.Button(
        root,
        text='Normal',  
    )
    normal_button.pack(
        ipadx=5,
        ipady=5,
        expand=False
    )
    impossible_button = ttk.Button(
        root,
        text='Difficile',
    )
    impossible_button.pack(
        ipadx=5,
        ipady=5,
        expand=False
    )
    exit_button = ttk.Button(
        root,
        text='Quitter',
        command=lambda: root.quit()
    )
    exit_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )
    root.mainloop()
    


def f1(): 
    root2 = tkt.Tk()
    root2.title('Jeu du Sudoku') 
    root2.geometry('600x400+50+50')
    message = tkt.Label(root2, text="Simple")
    message.pack()
    
    exit2_button = ttk.Button(
    root2,
    text='Retour au menu principal',
    command= fP
    )
    exit2_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
    )



print(fP())



    























