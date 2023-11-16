##-----Importation des Modules-----##
from tkinter import *


##----- Définition des Variables globales -----##
n=9
L=50
N=int(L*n+4)
d= 4

##-----Création de la fenêtre-----##
fen = Tk()
fen.title('name')

##-----Création du canevas-----##
dessin=Canvas(fen, bg="white", width=N, height=N)
dessin.grid(padx=50, pady=50)


##-----La grille-----##
dessin.create_line(4, N, N, N, width=4)
dessin.create_line(N, 4, N, N, width=4)
dessin.create_line(4, 4, N, 4, width=4)
dessin.create_line(4, 4, 4, N, width=4)


dessin.create_line(3*L+d, 0, 3*L+d, N, width=3) #ligne verticale 4
dessin.create_line(6*L+d, 0, 6*L+d, N, width=3) #ligne verticale 7 

dessin.create_line(L+d, 0, L+d, N, width=2) #ligne verticale 2
dessin.create_line(2*L+d, 0, 2*L+d, N, width=2) #ligne verticale 3
dessin.create_line(4*L+d, 0, 4*L+d, N, width=2) #ligne verticale 5 
dessin.create_line(5*L+d, 0, 5*L+d, N, width=2) #ligne verticale 6
dessin.create_line(7*L+d, 0, 7*L+d, N, width=2) #ligne verticale 6
dessin.create_line(8*L+d, 0, 8*L+d, N, width=2) #ligne verticale 6


dessin.create_line(0, 3*L+d, N, 3*L+d, width=3) #ligne horizontale 3
dessin.create_line(0, 6*L+d, N, 6*L+d, width=3) #ligne horizontale 6


dessin.create_line(0, L+d, N, L+d, width=2) #ligne horizontale 3
dessin.create_line(0, 2*L+d, N, 2*L+d, width=2) #ligne horizontale 6
dessin.create_line(0, 4*L+d, N, 4*L+d, width=2) #ligne horizontale 3
dessin.create_line(0, 5*L+d, N, 5*L+d, width=2) #ligne horizontale 6
dessin.create_line(0, 7*L+d, N, 7*L+d, width=2) #ligne horizontale 3
dessin.create_line(0, 8*L+d, N, 8*L+d, width=2) #ligne horizontale 6


##-----Programme principal-----##
fen.mainloop()                      # Boucle d'attente des événements