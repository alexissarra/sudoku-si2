##-----Importation des Modules-----##
from tkinter import *


##----- Définition des Variables globales -----##
n=9
L=50
N=int(L*n)

##-----Création de la fenêtre-----##
fen = Tk()
fen.title('Morpion')

##-----Création du canevas-----##
dessin=Canvas(fen, bg="white", width=N+10, height=N+10)
dessin.grid(padx=20, pady=20)


##-----La grille-----##
dessin.create_line(10, N, N, N, width=5)
dessin.create_line(N, 10, N, N, width=5)
dessin.create_line(10, 10, N, 10, width=5)
dessin.create_line(10, 10, 10, N, width=5)


dessin.create_line(3*L, 10, 3*L, N, width=3)
dessin.create_line(6*L, 10, 6*L, N, width=3)

##-----Programme principal-----##
fen.mainloop()                      # Boucle d'attente des événements