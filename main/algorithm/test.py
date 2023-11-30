# Création d'une matrice valide connue via internet
import copy
def chercher_les_possibilites_ligne_colonne(region : list) -> list :
    print(region)
    region_ligne = copy.deepcopy(region)
    grille_des_chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    grilles_des_possibilites = []
    grille_temporaire = []

    # Chercher les voisins à gauche et à droite
    for number in region_ligne:
        if number == 0 :
            print(number)
            for element in grille_des_chiffres :
                
                if grille_des_chiffres.index(element) == 0:
                     if region_ligne[region_ligne.index(number) + 1] != element:
                         grille_temporaire.append(element)
                elif grille_des_chiffres.index(element) == (len(grille_des_chiffres) - 1):
                    
                    if region_ligne[region_ligne.index(number) - 1] != element:
                        grille_temporaire.append(element)   
                else:
                    if region_ligne[region_ligne.index(number) - 1] != element and region_ligne[region_ligne.index(number) + 1] != element: 
                        grille_temporaire.append(element)
                    
            grilles_des_possibilites.append(grille_temporaire)
            region_ligne = region_ligne[region_ligne.index(number) +1:]
            grille_temporaire = []

    return grilles_des_possibilites


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

print(matrice_valide)

print(matrice_a_trou)

# Essayer d'évaluer les possibilités par région (carré de 3x3)

possibilite_totales = []
for region in matrice_a_trou: # je détermine pour chaque région les possibilités
    possibilites_ligne_region = chercher_les_possibilites_ligne_colonne(region.tolist())

# Il faut que je détermine toutes les combinaisons alors possibles pour la région donnée
# Chaque liste de possibilités en ligne est de dimension 7

    possibilite = []
    for mu1 in possibilites_ligne_region[0]:
        for mu2 in possibilites_ligne_region[1]:
            for mu3 in possibilites_ligne_region[2]:

                possibilite.append([mu1, mu2, mu3])   
    a = possibilite_recu(possibilite)
    a.sort()
    possibilite_totales.append(a)


print(possibilite_totales)




