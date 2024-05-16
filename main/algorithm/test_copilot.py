import numpy as np



'''
GitHub Copilot
Pour vérifier si une grille de Sudoku donnée par l'utilisateur est potentiellement finissable, vous pouvez suivre les étapes suivantes :

Vérifiez d'abord que la grille est valide. Cela signifie qu'aucun chiffre ne se répète dans une même ligne, colonne ou région (une sous-grille de 3x3).

Ensuite, essayez de résoudre la grille. Il existe plusieurs algorithmes pour cela, mais une approche courante est l'algorithme de backtracking. Il s'agit d'une approche de force brute où vous essayez chaque chiffre possible dans chaque case vide, puis revenez en arrière chaque fois que vous atteignez une impasse.

Si l'algorithme de résolution parvient à remplir toutes les cases vides sans contradiction, alors la grille est finissable. Sinon, elle ne l'est pas.
'''

import numpy as np

def est_valide(grille, ligne, colonne, num):
    # Vérifie si num est déjà présent dans la même ligne
    for x in range(9):
        if grille[ligne][x] == num:
            return False

    # Vérifie si num est déjà présent dans la même colonne
    for x in range(9):
        if grille[x][colonne] == num:
            return False

    # Vérifie si num est déjà présent dans la même région (sous-grille 3x3)
    startLigne = ligne - ligne % 3
    startColonne = colonne - colonne % 3
    for i in range(3):
        for j in range(3):
            if grille[i + startLigne][j + startColonne] == num:
                return False

    return True

def resoudre_sudoku(grille, ligne=0, colonne=0):
    if ligne == 9:
        return True
    if colonne == 9:
        return resoudre_sudoku(grille, ligne + 1, 0)
    if grille[ligne][colonne] != 0:
        return resoudre_sudoku(grille, ligne, colonne + 1)
    for num in range(1, 10):
        if est_valide(grille, ligne, colonne, num):
            grille[ligne][colonne] = num
            if resoudre_sudoku(grille, ligne, colonne + 1):
                return True
        grille[ligne][colonne] = 0
    return False

def est_finissable(grille):
    # Vérifie si la grille initiale est valide
    for i in range(9):
        for j in range(9):
            num = grille[i][j]
            if num != 0:
                grille[i][j] = 0
                if not est_valide(grille, i, j, num):
                    return False
                grille[i][j] = num

    return resoudre_sudoku(grille.copy())


matrice_a_trou = np.array([
                            [5, 0, 7, 2, 0, 8, 6, 0, 4], [0, 0, 1, 0, 0, 6, 0, 8, 0], [0, 0, 0, 3, 9, 0, 0, 7, 5],
                            [0, 0, 0, 1, 0, 0, 9, 7, 0], [0, 1, 3, 6, 0, 4, 8, 5, 0], [0, 5, 2, 0, 0, 3, 0, 0, 0],
                            [3, 5, 0, 0, 4, 2, 0, 0, 0], [0, 4, 0, 1, 0, 0, 3, 0, 0], [2, 0, 7, 8, 0, 9, 0, 0, 1]
                           ])


print(est_finissable(matrice_a_trou))

grille = [
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

grille = np.array([
    [7, 8, 1, 5, 6, 3, 2, 4, 9],
    [4,5,2,9,1,7,6,3,8],
    [6,9,3,2,4,8,5,1,7],
    [3,5,4,6,8,0    ,9,1,8],
    [2,8,6,1,9,4,5,7,3],
    [1,7,9,3,8,5,4,2,6],
    [4,9,5,1,3,6,8,2,7],
    [8,6,1,7,2,9,3,4,5],
    [7,3,2,8,5,4,9,6,1]
])
print(est_finissable(grille))