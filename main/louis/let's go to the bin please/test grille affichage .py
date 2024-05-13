##-----Importation des Modules-----##
import tkinter as tkt
import numpy as np


##----- Définition des Variables globales -----##
n=9
L=50
N=int(L*n+4)
d= 4                                                #décalage (épaisseur trait cadre)

##----- Définition des Variables pour les chiffres -----##

c = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]

matrice_valide = np.array([
                            [5, 9, 7, 2, 1, 8, 6, 3, 4], [4, 3, 1, 5, 7, 6, 2, 8, 9], [6, 2, 8, 3, 9, 4, 1, 7, 5],
                            [4, 8, 6, 1, 2, 5, 9, 7, 3], [7, 1, 3, 6, 9, 4, 8, 5, 2], [9, 5, 2, 7, 8, 3, 4, 1, 6],
                            [3, 5, 1, 7, 4, 2, 8, 6, 9], [9, 4, 8, 1, 6, 5, 3, 2, 7], [2, 6, 7, 8, 3, 9, 5, 4, 1]
                           ])


matrice_a_trou = np.array([
                            [5, 0, 7, 2, 0, 8, 6, 0, 4], [0, 0, 1, 0, 0, 6, 0, 8, 0], [0, 0, 0, 3, 9, 0, 0, 7, 5],
                            [0, 0, 0, 1, 0, 0, 9, 7, 0], [0, 1, 3, 6, 0, 4, 8, 5, 0], [0, 5, 2, 0, 0, 3, 0, 0, 0],
                            [3, 5, 0, 0, 4, 2, 0, 0, 0], [0, 4, 0, 1, 0, 0, 3, 0, 0], [2, 0, 7, 8, 0, 9, 0, 0, 1]
                           ])
##-----Création de la fenêtre-----##
fen = tkt.Tk()
fen.title('Grille SUDOKU')

##-----Création du canevas-----##
dessin=tkt.Canvas(fen, width=N, height=N)
dessin.grid(padx=50, pady=50)

##bg="SpringGreen2" mettre ca dans dessin=tkt.Canvas

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

##-----les chiffres -----##

##bg="#FFD700"

##-----case_1 -----##
case_1a = tkt.Entry(fen,width=1)
case_1a.place(x=57 ,y=57)
case_1a.configure(font=('Helvetica','25','bold'))
chiffre_1a = case_1a.get()




##-----recuperer la valeur d'un input -----##
def ecrire(x) :
     return x 


btn = tkt.Button(fen, text="Lire", command= ecrire(chiffre_1a))
btn.place(x=500, y=500)


##-----Programme principal-----##
fen.mainloop()                      # affichage de la fenêtre