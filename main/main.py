import tkinter as tkt 
from tkinter import ttk


def fP():
    root = tkt.Tk()
    root.title('Jeu du Sudoku') 
    root.geometry('600x400+50+50')
   # root.iconbitmap('C:/Users/ponch/Documents/GitHub/sudoku-si2/Alexis.jpg')
    message = tkt.Label(root, text="Choisissez votre difficulté")
    message.pack()

    bouton_simple = ttk.Button(
        root,
        text='Simple',
        command = f1 and 
    )
    bouton_simple.pack(
        ipadx=5,
        ipady=5,
        expand=False
    )
    bouton_normal = ttk.Button(
        root,
        text='Normal',
        command = f2  
    )
    bouton_normal.pack(
        ipadx=5,
        ipady=5,
        expand=False
    )
    bouton_difficile = ttk.Button(
        root,
        text='Difficile',
        command = f3
    )
    bouton_difficile.pack(
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
    root1 = tkt.Tk()
    root1.title('Jeu du Sudoku') 
    root1.geometry('600x400+50+50')
    message = tkt.Label(root1, text="Simple")
    message.pack()
        
    exit1_button = ttk.Button(
    root1,
    text='Retour au menu principal',
    command= fP
    )
    exit1_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
    )
    
def f2(): 
    root2 = tkt.Tk()
    root2.title('Jeu du Sudoku') 
    root2.geometry('600x400+50+50')
    message = tkt.Label(root2, text="Normal")
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

def f3(): 
    root3 = tkt.Tk()
    root3.title('Jeu du Sudoku') 
    root3.geometry('600x400+50+50')
    message = tkt.Label(root3, text="Difficile")
    message.pack()
    
    exit3_button = ttk.Button(
    root3,
    text='Retour au menu principal',
    command= fP
    )
    exit3_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
    )

print(fP())



    























