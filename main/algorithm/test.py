# Création d'une matrice valide connue via internet
import copy
import itertools
def chercher_les_possibilites_ligne_colonne(region : list) -> list :
    print(region)
    
    region = copy.deepcopy(region)
    grille_des_chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9] # chiffres possibles dans une régio
    grille_temporaire = []
    for number in region: # pour un élément dans une région
            if number == 0:
                for element in grille_des_chiffres : # je parcours la grille des chiffres
                    if element not in region: # j'élémine déjà tous les chiffres qui sont déjà dans la région
                                try: # si il n'est pas le premier
                                    boolean = region[region.index(number) - 1] != element
                                    try: # je regarde le suivant
                                        boolean = region[region.index(number) + 1] != element
                                        if boolean is True : grille_temporaire.append(element)
                                    except IndexError: # si il est le dernier, c'est bon
                                        grille_temporaire.append(element)
                                except IndexError: # si il est le premier, je regarde le suivant
                                    try:
                                        boolean = region[region.index(number) + 1] != element
                                        if boolean is True : grille_temporaire.append(element)
                                    except:
                                        pass
                break
    return grille_temporaire



def possibilite_recu(possibilite):
    for element in possibilite:
        if element[0] == element[1] or element[1] == element[2] or element[0] == element[2]:
            possibilite.remove(element)
            possibilite_recu(possibilite)
    
    return possibilite



import numpy as np

matrice_valide = np.array([
                            [5, 9, 7, 2, 1, 8, 6, 3, 4], [4, 3, 1, 5, 7, 6, 2, 8, 9], [6, 2, 8, 3, 9, 4, 1, 7, 5],
                            [4, 8, 6, 1, 2, 5, 9, 7, 3], [7, 1, 3, 6, 9, 4, 8, 5, 2], [9, 5, 2, 7, 8, 3, 4, 1, 6],
                            [3, 5, 1, 7, 4, 2, 8, 6, 9], [9, 4, 8, 1, 6, 5, 3, 2, 7], [2, 6,7, 8, 3, 9, 5, 4, 1]
                           ])


matrice_a_trou = np.array([
                            [5, 0, 7, 2, 0, 8, 6, 0, 4], [0, 0, 1, 0, 0, 6, 0, 8, 0], [0, 0, 0, 3, 9, 0, 0, 7, 5],
                            [0, 0, 0, 1, 0, 0, 9, 7, 0], [0, 1, 3, 6, 0, 4, 8, 5, 0], [0, 5, 2, 0, 0, 3, 0, 0, 0],
                            [3, 5, 0, 0, 4, 2, 0, 0, 0], [0, 4, 0, 1, 0, 0, 3, 0, 0], [2, 0, 7, 8, 0, 9, 0, 0, 1]
                           ])

# Essayer d'évaluer les possibilités par région (carré de 3x3)

possibilite_totales = []
compteur = 0
for region in matrice_a_trou: # je détermine pour chaque région les possibilités
    possibilites_ligne_region = chercher_les_possibilites_ligne_colonne(region.tolist())
    print(possibilites_ligne_region)

# Il faut que je détermine toutes les combinaisons alors possibles pour la région donnée
# Chaque liste de possibilités en ligne est de dimension 7

    possibilite_totales.append(list(itertools.permutations(possibilites_ligne_region))) 
    
    compteur += len(list(itertools.permutations(possibilites_ligne_region)) ) # il y a n! permutations possibles par matrice
print(possibilite_totales, len(possibilite_totales), compteur)

print(possibilite_totales[1], len(possibilite_totales[1]))


# Je dois maintenant faire une liste avec des ensemble de permutations qui fonctionnent en ligne, puis en colonne, puis croiser les deux

combolist_ligne  = []

# Je dois essayer de savoir par ligne quels sont les éléments tronqués
# Les trois premières lignes sont constituées des trois premières matrices, les trois autres lignes les trois autres matrices, etc...

ligne_placement = [] # [[l,a,b]] l = numéro de la ligne (de 1 à 9), a = numéro de la matrice (de 1 à 9); b = position du tronqué (de 1 à 3)
for ligne in range(0, 9):
    matrice_gauche = ligne//3
    matrice_milieu = ligne%3   
    matrice_droite = ligne//3 + 2
    print(ligne, matrice_gauche, matrice_milieu)

          
