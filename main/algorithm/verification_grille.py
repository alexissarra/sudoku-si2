import numpy as np



# On travaille avec des tableaux numpy



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

matrice_valide = np.array([
                            [5, 9, 7, 2, 1, 8, 6, 3, 4], [4, 3, 1, 5, 7, 6, 2, 8, 9], [6, 2, 8, 3, 9, 4, 1, 7, 5],
                            [4, 8, 6, 1, 2, 5, 9, 7, 3], [7, 1, 3, 6, 9, 4, 8, 5, 2], [9, 5, 2, 7, 8, 3, 4, 1, 6],
                            [3, 5, 1, 7, 4, 2, 8, 6, 9], [9, 4, 8, 1, 6, 5, 3, 2, 7], [2, 6, 7, 8, 3, 9, 5, 4, 1]
                           ])


print(matrice_valide)
print(verificateur(matrice_valide))

matrice_a_trou = np.array([
                            [5, 0, 7, 2, 0, 8, 6, 0, 4], [0, 0, 1, 0, 0, 6, 0, 8, 0], [0, 0, 0, 3, 9, 0, 0, 7, 5],
                            [0, 0, 0, 1, 0, 0, 9, 7, 0], [0, 1, 3, 6, 0, 4, 8, 5, 0], [0, 5, 2, 0, 0, 3, 0, 0, 0],
                            [3, 5, 0, 0, 4, 2, 0, 0, 0], [0, 4, 0, 1, 0, 0, 3, 0, 0], [2, 0, 7, 8, 0, 9, 0, 0, 1]
                           ])


# Maintenant, on va créer un solveur de sudoku
# On teste déjà la méthode suivante : https://zestedesavoir.com/tutoriels/476/le-backtracking-par-lexemple-resoudre-un-sudoku/


def solveur_de_sudoku(grille):
    if verificateur(grille) == True :
        return grille
    else:
        for 
        
    
    
    return 'True default'

