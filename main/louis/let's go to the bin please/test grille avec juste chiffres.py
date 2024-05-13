##-----Importation des Modules-----##
import tkinter as tkt


##----- Définition des Variables globales -----##
n=9
L=50
N=int(L*n+4)
d= 4                                                #décalage (épaisseur trait cadre)

##----- Définition des Variables pour les chiffres -----##

c1 = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]

c=  [[5, 9, 7, 2, 1, 8, 6, 3, 4], [4, 3, 1, 5, 7, 6, 2, 8, 9], [6, 2, 8, 3, 9, 4, 1, 7, 5],
     [4, 8, 6, 1, 2, 5, 9, 7, 3], [7, 1, 3, 6, 9, 4, 8, 5, 2], [9, 5, 2, 7, 8, 3, 4, 1, 6],
     [3, 5, 1, 7, 4, 2, 8, 6, 9], [9, 4, 8, 1, 6, 5, 3, 2, 7], [2, 6,7, 8, 3, 9, 5, 4, 1]]


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
chiffre_1a = tkt.Canvas(fen,width=41, height=41,)
chiffre_1a.place(x=57 ,y=57)
chiffre_1a.create_text(20, 20, text=c[0][0], fill="black",font=('Helvetica','30','bold'))

chiffre_1b = tkt.Canvas(fen,width=41, height=41,)
chiffre_1b.place(x=107 ,y=57)
chiffre_1b.create_text(20, 20, text=c[0][1], fill="black",font=('Helvetica','30','bold'))

chiffre_1c = tkt.Canvas(fen,width=41, height=41,)
chiffre_1c.place(x=157 ,y=57)
chiffre_1c.create_text(20, 20, text=c[0][2], fill="black",font=('Helvetica','30','bold'))

chiffre_1d = tkt.Canvas(fen,width=41, height=41,)
chiffre_1d.place(x=57 ,y=107)
chiffre_1d.create_text(20, 20, text=c[0][3], fill="black",font=('Helvetica','30','bold'))

chiffre_1e = tkt.Canvas(fen,width=41, height=41,)
chiffre_1e.place(x=107 ,y=107)
chiffre_1e.create_text(20, 20, text=c[0][4], fill="black",font=('Helvetica','30','bold'))

chiffre_1f = tkt.Canvas(fen,width=41, height=41,)
chiffre_1f.place(x=157 ,y=107)
chiffre_1f.create_text(20, 20, text=c[0][5], fill="black",font=('Helvetica','30','bold'))

chiffre_1g = tkt.Canvas(fen,width=41, height=41,)
chiffre_1g.place(x=57 ,y=157)
chiffre_1g.create_text(20, 20, text=c[0][6], fill="black",font=('Helvetica','30','bold'))

chiffre_1h = tkt.Canvas(fen,width=41, height=41,)
chiffre_1h.place(x=107 ,y=157)
chiffre_1h.create_text(20, 20, text=c[0][7], fill="black",font=('Helvetica','30','bold'))

chiffre_1i = tkt.Canvas(fen,width=41, height=41,)
chiffre_1i.place(x=157 ,y=157)
chiffre_1i.create_text(20, 20, text=c[0][8], fill="black",font=('Helvetica','30','bold'))

##-----case_2 -----##
chiffre_2a = tkt.Canvas(fen,width=41, height=41,)
chiffre_2a.place(x=207 ,y=57)
chiffre_2a.create_text(20, 20, text=c[1][0], fill="black",font=('Helvetica','30','bold'))

chiffre_2b = tkt.Canvas(fen,width=41, height=41,)
chiffre_2b.place(x=257 ,y=57)
chiffre_2b.create_text(20, 20, text=c[1][1], fill="black",font=('Helvetica','30','bold'))

chiffre_2c = tkt.Canvas(fen,width=41, height=41,)
chiffre_2c.place(x=307 ,y=57)
chiffre_2c.create_text(20, 20, text=c[1][2], fill="black",font=('Helvetica','30','bold'))

chiffre_2d = tkt.Canvas(fen,width=41, height=41,)
chiffre_2d.place(x=207 ,y=107)
chiffre_2d.create_text(20, 20, text=c[1][3], fill="black",font=('Helvetica','30','bold'))

chiffre_2e = tkt.Canvas(fen,width=41, height=41,)
chiffre_2e.place(x=257 ,y=107)
chiffre_2e.create_text(20, 20, text=c[1][4], fill="black",font=('Helvetica','30','bold'))

chiffre_2f= tkt.Canvas(fen,width=41, height=41,)
chiffre_2f.place(x=307 ,y=107)
chiffre_2f.create_text(20, 20, text=c[1][5], fill="black",font=('Helvetica','30','bold'))

chiffre_2g = tkt.Canvas(fen,width=41, height=41,)
chiffre_2g.place(x=207 ,y=157)
chiffre_2g.create_text(20, 20, text=c[1][6], fill="black",font=('Helvetica','30','bold'))

chiffre_2h = tkt.Canvas(fen,width=41, height=41,)
chiffre_2h.place(x=257 ,y=157)
chiffre_2h.create_text(20, 20, text=c[1][7], fill="black",font=('Helvetica','30','bold'))

chiffre_2i = tkt.Canvas(fen,width=41, height=41,)
chiffre_2i.place(x=307 ,y=157)
chiffre_2i.create_text(20, 20, text=c[1][8], fill="black",font=('Helvetica','30','bold'))


##-----case_3 -----##
chiffre_3a = tkt.Canvas(fen,width=41, height=41,)
chiffre_3a.place(x=357 ,y=57)
chiffre_3a.create_text(20, 20, text=c[2][0], fill="black",font=('Helvetica','30','bold'))

chiffre_3b = tkt.Canvas(fen,width=41, height=41,)
chiffre_3b.place(x=407 ,y=57)
chiffre_3b.create_text(20, 20, text=c[2][1], fill="black",font=('Helvetica','30','bold'))

chiffre_3c = tkt.Canvas(fen,width=41, height=41,)
chiffre_3c.place(x=457 ,y=57)
chiffre_3c.create_text(20, 20, text=c[2][2], fill="black",font=('Helvetica','30','bold'))

chiffre_3d = tkt.Canvas(fen,width=41, height=41,)
chiffre_3d.place(x=357 ,y=107)
chiffre_3d.create_text(20, 20, text=c[2][3], fill="black",font=('Helvetica','30','bold'))

chiffre_3e = tkt.Canvas(fen,width=41, height=41,)
chiffre_3e.place(x=407 ,y=107)
chiffre_3e.create_text(20, 20, text=c[2][4], fill="black",font=('Helvetica','30','bold'))

chiffre_3f= tkt.Canvas(fen,width=41, height=41,)
chiffre_3f.place(x=457 ,y=107)
chiffre_3f.create_text(20, 20, text=c[2][5], fill="black",font=('Helvetica','30','bold'))

chiffre_3g = tkt.Canvas(fen,width=41, height=41,)
chiffre_3g.place(x=357 ,y=157)
chiffre_3g.create_text(20, 20, text=c[2][6], fill="black",font=('Helvetica','30','bold'))

chiffre_3h = tkt.Canvas(fen,width=41, height=41,)
chiffre_3h.place(x=407 ,y=157)
chiffre_3h.create_text(20, 20, text=c[2][7], fill="black",font=('Helvetica','30','bold'))

chiffre_3i = tkt.Canvas(fen,width=41, height=41,)
chiffre_3i.place(x=457 ,y=157)
chiffre_3i.create_text(20, 20, text=c[2][8], fill="black",font=('Helvetica','30','bold'))



##-----case_4 -----##
chiffre_4a = tkt.Canvas(fen,width=41, height=41,)
chiffre_4a.place(x=57 ,y=207)
chiffre_4a.create_text(20, 20, text=c[3][0], fill="black",font=('Helvetica','30','bold'))

chiffre_4b = tkt.Canvas(fen,width=41, height=41,)
chiffre_4b.place(x=107 ,y=207)
chiffre_4b.create_text(20, 20, text=c[3][1], fill="black",font=('Helvetica','30','bold'))

chiffre_4c = tkt.Canvas(fen,width=41, height=41,)
chiffre_4c.place(x=157 ,y=207)
chiffre_4c.create_text(20, 20, text=c[3][2], fill="black",font=('Helvetica','30','bold'))

chiffre_4d = tkt.Canvas(fen,width=41, height=41,)
chiffre_4d.place(x=57 ,y=257)
chiffre_4d.create_text(20, 20, text=c[3][3], fill="black",font=('Helvetica','30','bold'))

chiffre_4e = tkt.Canvas(fen,width=41, height=41,)
chiffre_4e.place(x=107 ,y=257)
chiffre_4e.create_text(20, 20, text=c[3][4], fill="black",font=('Helvetica','30','bold'))

chiffre_4f = tkt.Canvas(fen,width=41, height=41,)
chiffre_4f.place(x=157 ,y=257)
chiffre_4f.create_text(20, 20, text=c[3][5], fill="black",font=('Helvetica','30','bold'))

chiffre_4g = tkt.Canvas(fen,width=41, height=41,)
chiffre_4g.place(x=57 ,y=307)
chiffre_4g.create_text(20, 20, text=c[3][6], fill="black",font=('Helvetica','30','bold'))

chiffre_4h = tkt.Canvas(fen,width=41, height=41,)
chiffre_4h.place(x=107 ,y=307)
chiffre_4h.create_text(20, 20, text=c[3][7], fill="black",font=('Helvetica','30','bold'))

chiffre_4i = tkt.Canvas(fen,width=41, height=41,)
chiffre_4i.place(x=157 ,y=307)
chiffre_4i.create_text(20, 20, text=c[3][8], fill="black",font=('Helvetica','30','bold'))


##-----case_5 -----##
chiffre_5a = tkt.Canvas(fen,width=41, height=41,)
chiffre_5a.place(x=207 ,y=207)
chiffre_5a.create_text(20, 20, text=c[4][0], fill="black",font=('Helvetica','30','bold'))

chiffre_5b = tkt.Canvas(fen,width=41, height=41,)
chiffre_5b.place(x=257 ,y=207)
chiffre_5b.create_text(20, 20, text=c[4][1], fill="black",font=('Helvetica','30','bold'))

chiffre_5c = tkt.Canvas(fen,width=41, height=41,)
chiffre_5c.place(x=307 ,y=207)
chiffre_5c.create_text(20, 20, text=c[4][2], fill="black",font=('Helvetica','30','bold'))

chiffre_5d = tkt.Canvas(fen,width=41, height=41,)
chiffre_5d.place(x=207 ,y=257)
chiffre_5d.create_text(20, 20, text=c[4][3], fill="black",font=('Helvetica','30','bold'))

chiffre_5e = tkt.Canvas(fen,width=41, height=41,)
chiffre_5e.place(x=257 ,y=257)
chiffre_5e.create_text(20, 20, text=c[4][4], fill="black",font=('Helvetica','30','bold'))

chiffre_5f = tkt.Canvas(fen,width=41, height=41,)
chiffre_5f.place(x=307 ,y=257)
chiffre_5f.create_text(20, 20, text=c[4][5], fill="black",font=('Helvetica','30','bold'))

chiffre_5g = tkt.Canvas(fen,width=41, height=41,)
chiffre_5g.place(x=207 ,y=307)
chiffre_5g.create_text(20, 20, text=c[4][6], fill="black",font=('Helvetica','30','bold'))

chiffre_5h = tkt.Canvas(fen,width=41, height=41,)
chiffre_5h.place(x=257 ,y=307)
chiffre_5h.create_text(20, 20, text=c[4][7], fill="black",font=('Helvetica','30','bold'))

chiffre_5i = tkt.Canvas(fen,width=41, height=41,)
chiffre_5i.place(x=307 ,y=307)
chiffre_5i.create_text(20, 20, text=c[4][8], fill="black",font=('Helvetica','30','bold'))


##-----case_6 -----##
chiffre_6a = tkt.Canvas(fen,width=41, height=41,)
chiffre_6a.place(x=357 ,y=207)
chiffre_6a.create_text(20, 20, text=c[5][0], fill="black",font=('Helvetica','30','bold'))

chiffre_6b = tkt.Canvas(fen,width=41, height=41,)
chiffre_6b.place(x=407 ,y=207)
chiffre_6b.create_text(20, 20, text=c[5][1], fill="black",font=('Helvetica','30','bold'))

chiffre_6c = tkt.Canvas(fen,width=41, height=41,)
chiffre_6c.place(x=457 ,y=207)
chiffre_6c.create_text(20, 20, text=c[5][2], fill="black",font=('Helvetica','30','bold'))

chiffre_6d = tkt.Canvas(fen,width=41, height=41,)
chiffre_6d.place(x=357 ,y=257)
chiffre_6d.create_text(20, 20, text=c[5][3], fill="black",font=('Helvetica','30','bold'))

chiffre_6e = tkt.Canvas(fen,width=41, height=41,)
chiffre_6e.place(x=407 ,y=257)
chiffre_6e.create_text(20, 20, text=c[5][4], fill="black",font=('Helvetica','30','bold'))

chiffre_6f= tkt.Canvas(fen,width=41, height=41,)
chiffre_6f.place(x=457 ,y=257)
chiffre_6f.create_text(20, 20, text=c[5][5], fill="black",font=('Helvetica','30','bold'))

chiffre_6g = tkt.Canvas(fen,width=41, height=41,)
chiffre_6g.place(x=357 ,y=307)
chiffre_6g.create_text(20, 20, text=c[5][6], fill="black",font=('Helvetica','30','bold'))

chiffre_6h = tkt.Canvas(fen,width=41, height=41,)
chiffre_6h.place(x=407 ,y=307)
chiffre_6h.create_text(20, 20, text=c[5][7], fill="black",font=('Helvetica','30','bold'))

chiffre_6i = tkt.Canvas(fen,width=41, height=41,)
chiffre_6i.place(x=457 ,y=307)
chiffre_6i.create_text(20, 20, text=c[5][8], fill="black",font=('Helvetica','30','bold'))

##-----case_7 -----##
chiffre_7a = tkt.Canvas(fen,width=41, height=41,)
chiffre_7a.place(x=57 ,y=357)
chiffre_7a.create_text(20, 20, text=c[6][0], fill="black",font=('Helvetica','30','bold'))

chiffre_7b = tkt.Canvas(fen,width=41, height=41, )
chiffre_7b.place(x=107 ,y=357)
chiffre_7b.create_text(20, 20, text=c[6][1], fill="black",font=('Helvetica','30','bold'))

chiffre_7c = tkt.Canvas(fen,width=41, height=41,)
chiffre_7c.place(x=157 ,y=357)
chiffre_7c.create_text(20, 20, text=c[6][2], fill="black",font=('Helvetica','30','bold'))

chiffre_7d = tkt.Canvas(fen,width=41, height=41,)
chiffre_7d.place(x=57 ,y=407)
chiffre_7d.create_text(20, 20, text=c[6][3], fill="black",font=('Helvetica','30','bold'))

chiffre_7e = tkt.Canvas(fen,width=41, height=41,)
chiffre_7e.place(x=107 ,y=407)
chiffre_7e.create_text(20, 20, text=c[6][4], fill="black",font=('Helvetica','30','bold'))

chiffre_7f = tkt.Canvas(fen,width=41, height=41,)
chiffre_7f.place(x=157 ,y=407)
chiffre_7f.create_text(20, 20, text=c[6][5], fill="black",font=('Helvetica','30','bold'))

chiffre_7g = tkt.Canvas(fen,width=41, height=41,)
chiffre_7g.place(x=57 ,y=457)
chiffre_7g.create_text(20, 20, text=c[6][6], fill="black",font=('Helvetica','30','bold'))

chiffre_7h = tkt.Canvas(fen,width=41, height=41,)
chiffre_7h.place(x=107 ,y=457)
chiffre_7h.create_text(20, 20, text=c[6][7], fill="black",font=('Helvetica','30','bold'))

chiffre_7i = tkt.Canvas(fen,width=41, height=41,)
chiffre_7i.place(x=157 ,y=457)
chiffre_7i.create_text(20, 20, text=c[6][8], fill="black",font=('Helvetica','30','bold'))

##-----case_8 -----##
chiffre_8a = tkt.Canvas(fen,width=41, height=41,)
chiffre_8a.place(x=207 ,y=357)
chiffre_8a.create_text(20, 20, text=c[7][0], fill="black",font=('Helvetica','30','bold'))

chiffre_8b = tkt.Canvas(fen,width=41, height=41,)
chiffre_8b.place(x=257 ,y=357)
chiffre_8b.create_text(20, 20, text=c[7][1], fill="black",font=('Helvetica','30','bold'))

chiffre_8c = tkt.Canvas(fen,width=41, height=41,)
chiffre_8c.place(x=307 ,y=357)
chiffre_8c.create_text(20, 20, text=c[7][2], fill="black",font=('Helvetica','30','bold'))

chiffre_8d = tkt.Canvas(fen,width=41, height=41,)
chiffre_8d.place(x=207 ,y=407)
chiffre_8d.create_text(20, 20, text=c[7][3], fill="black",font=('Helvetica','30','bold'))

chiffre_8e = tkt.Canvas(fen,width=41, height=41,)
chiffre_8e.place(x=257 ,y=407)
chiffre_8e.create_text(20, 20, text=c[7][4], fill="black",font=('Helvetica','30','bold'))

chiffre_8f= tkt.Canvas(fen,width=41, height=41,)
chiffre_8f.place(x=307 ,y=407)
chiffre_8f.create_text(20, 20, text=c[7][5], fill="black",font=('Helvetica','30','bold'))

chiffre_8g = tkt.Canvas(fen,width=41, height=41,)
chiffre_8g.place(x=207 ,y=457)
chiffre_8g.create_text(20, 20, text=c[7][6], fill="black",font=('Helvetica','30','bold'))

chiffre_8h = tkt.Canvas(fen,width=41, height=41,)
chiffre_8h.place(x=257 ,y=457)
chiffre_8h.create_text(20, 20, text=c[7][7], fill="black",font=('Helvetica','30','bold'))

chiffre_8i = tkt.Canvas(fen,width=41, height=41,)
chiffre_8i.place(x=307 ,y=457)
chiffre_8i.create_text(20, 20, text=c[7][8], fill="black",font=('Helvetica','30','bold'))


##-----case_9 -----##
chiffre_9a = tkt.Canvas(fen,width=41, height=41,)
chiffre_9a.place(x=357 ,y=357)
chiffre_9a.create_text(20, 20, text=c[8][0], fill="black",font=('Helvetica','30','bold'))

chiffre_9b = tkt.Canvas(fen,width=41, height=41,)
chiffre_9b.place(x=407 ,y=357)
chiffre_9b.create_text(20, 20, text=c[8][1], fill="black",font=('Helvetica','30','bold'))

chiffre_9c = tkt.Canvas(fen,width=41, height=41,)
chiffre_9c.place(x=457 ,y=357)
chiffre_9c.create_text(20, 20, text=c[8][2], fill="black",font=('Helvetica','30','bold'))

chiffre_9d = tkt.Canvas(fen,width=41, height=41,)
chiffre_9d.place(x=357 ,y=407)
chiffre_9d.create_text(20, 20, text=c[8][3], fill="black",font=('Helvetica','30','bold'))

chiffre_9e = tkt.Canvas(fen,width=41, height=41,)
chiffre_9e.place(x=407 ,y=407)
chiffre_9e.create_text(20, 20, text=c[8][4], fill="black",font=('Helvetica','30','bold'))

chiffre_9f= tkt.Canvas(fen,width=41, height=41,)
chiffre_9f.place(x=457 ,y=407)
chiffre_9f.create_text(20, 20, text=c[8][5], fill="black",font=('Helvetica','30','bold'))

chiffre_9g = tkt.Canvas(fen,width=41, height=41,)
chiffre_9g.place(x=357 ,y=457)
chiffre_9g.create_text(20, 20, text=c[8][6], fill="black",font=('Helvetica','30','bold'))

chiffre_9h = tkt.Canvas(fen,width=41, height=41,)
chiffre_9h.place(x=407 ,y=457)
chiffre_9h.create_text(20, 20, text=c[8][7], fill="black",font=('Helvetica','30','bold'))

chiffre_9i = tkt.Canvas(fen,width=41, height=41,)
chiffre_9i.place(x=457 ,y=457)
chiffre_9i.create_text(20, 20, text=c[8][8], fill="black",font=('Helvetica','30','bold'))


##-----Programme principal-----##
fen.mainloop()                      # affichage de la fenêtre