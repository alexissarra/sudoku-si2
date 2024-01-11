##-----Importation des Modules-----##
import tkinter as tkt


##----- Définition des Variables globales -----##
n=9
L=50
N=int(L*n+4)
d= 4                                                #décalage (épaisseur trait cadre)

##-----Création de la fenêtre-----##
fen = tkt.Tk()
fen.title('Grille SUDOKU')

##-----Création du canevas-----##
dessin=tkt.Canvas(fen, bg="SpringGreen2", width=N, height=N)
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

##-----les chiffres -----##

chiffre_a = tkt.Canvas(fen,width=41, height=41, bg="yellow")
chiffre_a.place(x=57 ,y=57)
chiffre_a.create_text(20, 20, text="1", fill="black",font=('Helvetica','30','bold'))

chiffre_b = tkt.Canvas(fen,width=41, height=41, bg="purple")
chiffre_b.place(x=107 ,y=57)
chiffre_b.create_text(20, 20, text="2", fill="black",font=('Helvetica','30','bold'))

chiffre_c = tkt.Canvas(fen,width=41, height=41, bg="red")
chiffre_c.place(x=157 ,y=57)
chiffre_c.create_text(20, 20, text="3", fill="black",font=('Helvetica','30','bold'))

chiffre_d = tkt.Canvas(fen,width=41, height=41, bg="#FF6103")
chiffre_d.place(x=57 ,y=107)
chiffre_d.create_text(20, 20, text="4", fill="black",font=('Helvetica','30','bold'))

chiffre_f = tkt.Canvas(fen,width=41, height=41, bg="#00FFFF")
chiffre_f.place(x=107 ,y=107)
chiffre_f.create_text(20, 20, text="5", fill="black",font=('Helvetica','30','bold'))

chiffre_g = tkt.Canvas(fen,width=41, height=41, bg="#BF3EFF")
chiffre_g.place(x=157 ,y=107)
chiffre_g.create_text(20, 20, text="6", fill="black",font=('Helvetica','30','bold'))

chiffre_h = tkt.Canvas(fen,width=41, height=41, bg="#DCDCDC")
chiffre_h.place(x=57 ,y=157)
chiffre_h.create_text(20, 20, text="7", fill="black",font=('Helvetica','30','bold'))

chiffre_i = tkt.Canvas(fen,width=41, height=41, bg="#FFD700")
chiffre_i.place(x=107 ,y=157)
chiffre_i.create_text(20, 20, text="8", fill="black",font=('Helvetica','30','bold'))

chiffre_j = tkt.Canvas(fen,width=41, height=41, bg="#4B0082")
chiffre_j.place(x=157 ,y=157)
chiffre_j.create_text(20, 20, text="9", fill="black",font=('Helvetica','30','bold'))

##-----Programme principal-----##
fen.mainloop()                      # affichage de la fenêtre