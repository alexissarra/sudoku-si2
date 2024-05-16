import numpy as np
import copy
import itertools


def verificateur(grille) -> bool :
    # On regarde la validité par région
    for region in grille:
        chiffresDansLaRegion = []
        for chiffre in region:
            if chiffre in chiffresDansLaRegion or chiffre == 0 :
                return False
            else: chiffresDansLaRegion.append(chiffre)

   # Si on arrive là, c'est que toutes les régions sont bonnes
    # On regarde la validité en colonne
    # On prends les éléments trois par trois, on commence au début puis on recommence en d&callant l'indice de 1 à chaque fois
    for sequence in range(0,3):
        for hauteur in range(0, 3): # pour avoir trois colonnes par trois colonnes
            chiffresDansLaColonne = []
            for region in grille[sequence::3]: # pour les region qui sont les unes en dessus des autres
                for element in region[hauteur::3]:
                    if element in chiffresDansLaColonne or element == 0: # si il y a un doublon dans la colonne, on renvoit faux
                        return False
                    else : chiffresDansLaColonne.append(element) # sinon on ajoute ce chiffre dans la liste
    
    # Si on arrive là, c'est que toutes les colonnes sont bonnes
    # On s'attaque aux lignes par meme logique que pour les ligne
    for sequence in range(0,3):
        for hauteur in range(0, 3): # pour avoir trois ligne par trois ligne
            chiffresDansLaLigne = []
            for region in grille[sequence*3:sequence*3+3]: # pour les region qui sont les unes en dessus des autres
                for element in region[hauteur*3:hauteur*3+3]:
                    if element in chiffresDansLaLigne or element == 0: # si il y a un doublon dans la colonne, on renvoit faux
                        return False
                    else : chiffresDansLaLigne.append(element) # sinon on ajoute ce chiffre dans la liste
    return True

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
'''

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
'''

# Maintenant il faut essayer de déterminer une bonne combinaison
# On va se baser sur la région qui possède le plus de chiffres déjà posés. Si il n'y en as pas, on prends la première qui vient
# On prends une région possible, puis on teste avec toutes les autres régions possibles
# Dès qu'une solution est trouvée, on renvoie cette dernière

# On détermine la région base



def determiner_region_reference(matrice):
    region_reference = []
    longueur_region_reference = 0
    for region in matrice:
        longueur_region = 0
        for chiffre in region:
            if chiffre != 0:
                longueur_region += 1
            if longueur_region > longueur_region_reference:
                longueur_region_reference = longueur_region
                region_reference = region
    return region_reference




print(determiner_region_reference(matrice_a_trou))

matrice_a_trou = np.array([
                            [5, 0, 7, 2, 0, 8, 6, 0, 4], [0, 0, 1, 0, 0, 6, 0, 8, 0], [0, 0, 0, 3, 9, 0, 0, 7, 5],
                            [0, 0, 0, 1, 0, 0, 9, 7, 0], [0, 1, 3, 6, 0, 4, 8, 5, 0], [0, 5, 2, 0, 0, 3, 0, 0, 0],
                            [3, 5, 0, 0, 4, 2, 0, 0, 0], [0, 4, 0, 1, 0, 0, 3, 0, 0], [2, 0, 7, 8, 0, 9, 0, 0, 1]
                           ])



def determiner_combinaison_valide(matrice_utilisateur):
    region_reference = determiner_region_reference(matrice_utilisateur) # on détermine la région de référence
    matrice_utilisateur_list = matrice_utilisateur.tolist() # on transforme la grille utilisateur en liste
    index_region_reference =  matrice_utilisateur_list.index(region_reference.tolist()) # on récupère l'indice de la région de référence
    
    # Maintenant on veut récupérer toutes les combinaisons possibles pour la région de référence
    possibilites_region_reference = list(itertools.permutations(chercher_les_possibilites_ligne_colonne(region_reference.tolist())))

    

    
        
   

    
    
print(determiner_combinaison_valide(matrice_a_trou))


    
    

                

    
    