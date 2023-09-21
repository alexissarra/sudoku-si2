import tkinter as tkt 

# initialisation de la fenêtre
root = tkt.Tk()

# création du message
message = tkt.Label(root, text="Alban est le meilleur !")
message2 = tkt.Label(root, text="Longue vie à Alban !")

# affichage du message
message.pack()
message2.pack()

# ligne nécessaire si l'on veut garder la fenêtre ouverte
root.mainloop()










