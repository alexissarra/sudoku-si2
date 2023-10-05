#### -------------------------- Modules & variables
from tkinter import *
c = 30                                              ####---- Longueur coté case
n = 9                                               ####---- Nombre de cases totales (par ligne et par colonne)
cases = []                                          ####---- Liste contenant les objets cases

#### -------------------------- fenetre
fenetre_grille = Tk()
fenetre_grille.title('Fenetre grille')              ####---- nom de la fenetre
fenetre_grille.config(bg = "#87CEEB")               ####---- couleur de la fenetre
fenetre_grille.geometry("640x480")                  ####---- taille de la fenetre

#### -------------------------- bouton
bouton1 = Button (fenetre_grille, text = "Fermer",command = fenetre_grille.destroy)
bouton1.pack()
bouton1.place(x=25, y=100)




#### -------------------------- ATTENTION DERNIERE LIGNE DU CODE
fenetre_grille.mainloop()                            ####---- affichage permanant de la fenetre