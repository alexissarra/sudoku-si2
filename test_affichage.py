import tkinter as tkt 
from tkinter import ttk


# initialisation de la fenêtre
root = tkt.Tk()
root.title('Jeu du Sudoku') #donne un nom à la fenêtre
root.geometry('600x400+50+50')

# logo
root.iconbitmap('Alexis.JPG')

# création du message
message = tkt.Label(root, text="Choisissez votre difficulté")

# affichage du message
message.pack()


def test():
    root2 = tkt.Tk()
    root2.title('Jeu du Sudoku') 
    root2.geometry('600x400+50+50')
    message = tkt.Label(root2, text="Simple")
    message.pack()

    exit2_button = ttk.Button(
    root2,
    text='Quitter',
    command=lambda: root2.quit()
    )
    
    exit2_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
    )

    root.mainloop()


#affichage bouton simple 
easy_button = ttk.Button(
    root,
    text='Simple',
    command=test
)

easy_button.pack(
    ipadx=5,
    ipady=5,
    expand=False
)

# bouton normal
normal_button = ttk.Button(
    root,
    text='Normal',  
)
normal_button.pack(
    ipadx=5,
    ipady=5,
    expand=False
)

# bouton difficile
impossible_button = ttk.Button(
    root,
    text='Difficile',
)
impossible_button.pack(
    ipadx=5,
    ipady=5,
    expand=False
)

# bouton ginot
ginot_button = ttk.Button(
    root,
    text='Ginot',
)
ginot_button.pack(
    ipadx=5,
    ipady=5,
    expand=False
)

#bouton pour quitter
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




# ligne nécessaire si l'on veut garder la fenêtre ouverte
root.mainloop()




















