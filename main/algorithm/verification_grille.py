import numpy as np

# Fonction qui vérifie la validité d'une grille de sudoku

def est_sudoku_valide(grille):
    # Vérifier les lignes
    for ligne in grille:
        if len(ligne) != 9 or len(set(ligne)) != 9 or 0 in ligne:
            return False
    
    # Vérifier les colonnes
    for col in range(9):
        colonne = [grille[ligne][col] for ligne in range(9)]
        if len(set(colonne)) != 9 or 0 in colonne:
            return False
    
    # Vérifier les régions
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            region = grille[i][j:j+3] + grille[i+1][j:j+3] + grille[i+2][j:j+3]
            if len(set(region)) != 9 or 0 in region:
                return False
    
    return True

# Exemple de grille valide:
grille = [[0, 0, 0, 0, 0, 0, 0, 0, 0], # 0 = case vide
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 2, 3, 0, 0, 0, 0],
          [0, 0, 4, 5, 6, 0, 0, 0, 0],
          [0, 0, 7, 8, 9, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 2, 3, 0],
          [0, 0, 0, 0, 0, 4, 5, 6, 0],
          [0, 0, 0, 0, 0, 7, 8, 9, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(est_sudoku_valide(grille))


matrice_valide = [[5, 9, 7, 2, 1, 8, 6, 3, 4],
                  [4, 3, 1, 5, 7, 6, 2, 8, 9],
                  [6, 2, 8, 3, 9, 4, 1, 7, 5],
                  [4, 8, 6, 1, 2, 5, 9, 7, 3],
                  [7, 1, 3, 6, 9, 4, 8, 5, 2],
                  [9, 5, 2, 7, 8, 3, 4, 1, 6],
                  [3, 5, 1, 7, 4, 2, 8, 6, 9],
                  [9, 4, 8, 1, 6, 5, 3, 2, 7],
                  [2, 6,7, 8, 3, 9, 5, 4, 1]]


print(est_sudoku_valide(matrice_valide)) # True


# Exemple d'utilisation
grille_sudoku = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

print(est_sudoku_valide(grille_sudoku)) 


import numpy as np

def est_sudoku_valide(grille):
    # Vérifier les lignes
    for ligne in grille:
        if len(ligne) != 9 or len(set(ligne)) != 9 or 0 in ligne:
            return False
    
    # Vérifier les colonnes
    for col in range(9):
        colonne = [grille[ligne][col] for ligne in range(9)]
        if len(set(colonne)) != 9 or 0 in colonne:
            return False
    
    # Vérifier les régions
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            region = []
            for m in range(3):
                for n in range(3):
                    region.append(grille[i+m][j+n])
            if len(set(region)) != 9 or 0 in region:
                return False
    
    return True

# Exemple d'utilisation
grille_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print(est_sudoku_valide(grille_sudoku))  # Renvoie True car la grille est valide
