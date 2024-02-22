# Création d'une matrice valide connue via internet
import copy
import itertools
import numpy as np


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

print(matrice_a_trou)
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
# print(possibilite_totales, len(possibilite_totales), compteur)

#print(possibilite_totales[0], len(possibilite_totales[0]))





# Je dois maintenant faire une liste avec des ensemble de permutations qui fonctionnent en ligne, puis en colonne, puis croiser les deux
combolist_ligne  = []


# EN LIGNE

# Je dois essayer de savoir par ligne quels sont les éléments tronqués
# Les trois premières lignes sont constituées des trois premières matrices, les trois autres lignes les trois autres matrices, etc...

# Je peux essayer de parcourir chaque ligne totale de ma grille et déterminer les chiffres possibles

compteur = 0
matrices_gauche = []
matrices_milieu = []
matrices_droite = []

for region in matrice_a_trou:

    if compteur % 3 == 0:
        matrices_gauche.append(region)
    elif compteur % 3 == 1:
        matrices_milieu.append(region)
    else:
        matrices_droite.append(region)
    compteur += 1


# Maintenant que j'ai séparé par emplacement les matrice, je peux regarder par colonne
colonnes = []
colonnes_final = []


for i in range (0, 3):
    colonnes.append(matrices_gauche[0][i])
    colonnes.append(matrices_gauche[0][i+3])
    colonnes.append(matrices_gauche[0][i+6])

    colonnes.append(matrices_gauche[1][i])
    colonnes.append(matrices_gauche[1][i+3])
    colonnes.append(matrices_gauche[1][i+6])

    colonnes.append(matrices_gauche[2][i])
    colonnes.append(matrices_gauche[2][i+3])
    colonnes.append(matrices_gauche[2][i+6])

    colonnes_final.append(colonnes)
    colonnes = []



for i in range (0, 3):
    colonnes.append(matrices_milieu[0][i])
    colonnes.append(matrices_milieu[0][i+3])
    colonnes.append(matrices_milieu[0][i+6])

    colonnes.append(matrices_milieu[1][i])
    colonnes.append(matrices_milieu[1][i+3])
    colonnes.append(matrices_milieu[1][i+6])

    colonnes.append(matrices_milieu[2][i])
    colonnes.append(matrices_milieu[2][i+3])
    colonnes.append(matrices_milieu[2][i+6])

    colonnes_final.append(colonnes)
    colonnes = []

for i in range (0, 3):
    colonnes.append(matrices_droite[0][i])
    colonnes.append(matrices_droite[0][i+3])
    colonnes.append(matrices_droite[0][i+5])


    colonnes.append(matrices_droite[1][i])
    colonnes.append(matrices_droite[1][i+3])
    colonnes.append(matrices_droite[1][i+6])

    colonnes.append(matrices_droite[2][i])
    colonnes.append(matrices_droite[2][i+3])
    colonnes.append(matrices_droite[2][i+6])

    colonnes_final.append(colonnes)
    colonnes = []


# Désormais il y a dans cette liste les 9 colonnes sous forme de liste chacune
    
print(colonnes_final)
print(len(colonnes_final)) # logiquement 9

# Je cherche maintenanbt pour chaque colonne les possibilités

possibilites_colonnes = []
liste_chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for colonne in colonnes_final:
    chiffres_possibles = []
    for chiffre in liste_chiffres:
        if chiffre not in colonne:
            chiffres_possibles.append(chiffre)

    possibilites_colonnes.append(list(itertools.permutations(chiffres_possibles)))
     

print(len(possibilites_colonnes)) # logiquement 9

# Je veux désormais faire la même chose en ligne
# Ce sera juste un copié-collé de ce qui a été fait en colonne, en changeant les variables


liste_lignes = [[] for i in range(9)] #logiquement de dim 9
for iteration in range(0, 8, 3):
    for region in (matrice_a_trou[iteration], matrice_a_trou[iteration+1], matrice_a_trou[iteration+2]):
        compteur = 0
        for element in region:
            if compteur // 3 == 0:
                liste_lignes[iteration].append(element)
            elif compteur // 3 == 1:
                liste_lignes[iteration+1].append(element)
            else:
                liste_lignes[iteration+2].append(element)
            compteur += 1

print(matrice_a_trou)
print(liste_lignes)
print(len(liste_lignes)) # de dim 9
            

# Je dois maintenant déterminer toutes les possibilités en ligne, comme fait avant avec les permuttations

possibilites_ligne = []
liste_chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for colonne in colonnes_final:
    chiffres_possibles = []
    for chiffre in liste_chiffres:
        if chiffre not in colonne:
            chiffres_possibles.append(chiffre)

    possibilites_ligne.append(list(itertools.permutations(chiffres_possibles)))

print(len(possibilites_ligne))


# À partir de maintenant, toutes les possibilités en ligne, en colonne et par région ont été déterminées
# Il n'y a plus qu'à croiser ces données

# Comment croiser les données ?

# Compter le nombre de possibilités par ligne, par colonne et par région
compteur_colonnes, compteur_lignes, compteur_regions = 0, 0, 0

for element in possibilites_colonnes:
    for i in element:
        compteur_colonnes += 1

for element in possibilites_ligne:
    for i in element:
        compteur_lignes += 1


for element in possibilite_totales:
    for i in element:
        compteur_regions += 1

# Comme il y a moins de possibilités par région que de possibilités par ligne/colonne, on va prendre chaque possibilité par région
# et y associer les possibilités par ligne et colonnes possibles
        
# Il faut définir une fonction qui prends en entrée des possibilités, teste et renvoie si c'est possible ou pas
        
print(compteur_colonnes, compteur_lignes, compteur_regions)

# En prenant en compte les éléments déjà présents dans la matrice tronquée, je peux éliminer des lignes et des colonnes.
# C'est ce que je vais faire 

# Première approche : tester des combinaisons aléatoires de régions jusqu'à tomber sur la bonne





# Je peux tester des combinaisons aléatoires de régions


matrice_a_trou = matrice_a_trou.tolist()
for region in matrice_a_trou: # je parcours la grille de sudoku
    indice_de_region = matrice_a_trou.index(region)
    liste_candidats = possibilite_totales[indice_de_region] # liste de tous les candidats pour la région en cours
    for chiffre in region: # je parcours la région
        indice_chiffre = region.index(chiffre)
        if chiffre == 0: # je fais un test pour chaque chiffre différent de 0
            for region_candidat in liste_candidats:
                if region_candidat[indice_chiffre] != chiffre:
                    possibilite_totales[indice_de_region].remove(region_candidat) # pas de problèmes de doublons, je peux utiliser remove


print(possibilite_totales)
compteur_colonnes, compteur_lignes, compteur_regions = 0, 0, 0

for element in possibilites_colonnes:
    for i in element:
        compteur_colonnes += 1

for element in possibilites_ligne:
    for i in element:
        compteur_lignes += 1


for element in possibilite_totales:
    for i in element:
        compteur_regions += 1

        
print(compteur_colonnes, compteur_lignes, compteur_regions)



        



# Je vais essayer de faire une fonction qui prends en entrée une liste de possibilités et qui renvoie si c'est possible ou pas
# Je prends une région possible et j'essaie de compléter avec des colonnes qui pourraient correspondre et des lignes qui pourraient correspondre
# Si elle est valide, je la garde, sinon je la supprime


'''
for region1 in possibilite_totales[0]:
    # Je dois déjà choisir trois premières colonnes possibles et trois premières lignes possibles
    colonnes_possibles = []
    lignes_possibles = []
    print(region1)  
    print(possibilite_totales[0])
    print(1)
    colonne1 = [region1[0], region1[3], region1[6]]
    colonne2 = [region1[1], region1[4], region1[7]]
    colonne3 = [region1[2], region1[5], region1[8]]
    ligne1 = [region1[0], region1[1], region1[2]]
    ligne2 = [region1[3], region1[4], region1[5]]
    ligne3 = [region1[6], region1[7], region1[8]]

    # Je détermine toutes les colonnes et lignes réunissant ces débuts de colonnes et lignes
    # Pour les régions, le problème est que chaque possibilité ne contient que les éléments nuls de la région. Il faut donc compléter.
    for i in range (0, 8):
        for colonne in possibilites_colonnes[i]:
            if colonne[0] == colonne1[0] and colonne[1] == colonne1[1] and colonne[2] == colonne1[2]:
                colonnes_possibles.append(colonne)

print(colonnes_possibles)
'''



























'''
possibilite_totales_colonnes = []
compteur = 0

for colonne in colonnes_final: # je détermine pour chaque région les possibilités

    print(possibilites_ligne_region)

# Il faut que je détermine toutes les combinaisons alors possibles pour la région donnée
# Chaque liste de possibilités en ligne est de dimension 7

    possibilite_totales.append(list(itertools.permutations(possibilites_ligne_region))) 
    
    compteur += len(list(itertools.permutations(possibilites_ligne_region)) ) # il y a n! permutations possibles par matrice
# print(possibilite_totales, len(possibilite_totales), compteur)

#print(possibilite_totales[0], len(possibilite_totales[0]))
'''



'''
ligne_placement = [] # [[l,a,b]] l = numéro de la ligne (de 1 à 9), a = numéro de la matrice (de 1 à 9); b = position du tronqué (de 1 à 3)
for ligne in range(0, 9):
    matrice_gauche = ligne//3
    matrice_milieu = ligne%3   
    matrice_droite = ligne//3 + 2
    print(ligne, matrice_gauche, matrice_milieu)
'''
          
