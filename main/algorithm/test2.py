import numpy as np



def est_valide(grille, pos, num):
    # Vérifie la ligne
    for i in range(9):
        if grille[pos[0]][i] == num:
            return False

    # Vérifie la colonne
    for i in range(9):
        if grille[i][pos[1]] == num:
            return False

    # Vérifie la région
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grille[i][j] == num:
                return False

    return True

def trouver_vide(grille):
    for i in range(9):
        for j in range(9):
            if grille[i][j] == 0:
                return (i, j)  # ligne, colonne

    return None

def resoudre(grille):
    vide = trouver_vide(grille)
    if not vide:
        return True
    else:
        ligne, colonne = vide

    for i in range(1, 10):
        if est_valide(grille, (ligne, colonne), i):
            grille[ligne][colonne] = i

            if resoudre(grille):
                return True

            grille[ligne][colonne] = 0

    return False

def est_finissable(grille):
    return resoudre(grille.copy())

def convertir_grille(grille):
    nouvelle_grille = [[0]*9 for _ in range(9)]
    for region in range(9):
        for i in range(3):
            for j in range(3):
                nouvelle_grille[(region//3)*3 + i][(region%3)*3 + j] = grille[region][i*3 + j]
    return nouvelle_grille


matrice_a_trou = np.array([
                            [5, 0, 7, 2, 0, 8, 6, 0, 4], [0, 0, 1, 0, 0, 6, 0, 8, 0], [0, 0, 0, 3, 9, 0, 0, 7, 5],
                            [0, 0, 0, 1, 0, 0, 9, 7, 0], [0, 1, 3, 6, 0, 4, 8, 5, 0], [0, 5, 2, 0, 0, 3, 0, 0, 0],
                            [3, 5, 0, 0, 4, 2, 0, 0, 0], [0, 4, 0, 1, 0, 0, 3, 0, 0], [2, 0, 7, 8, 0, 9, 0, 0, 1]
                           ])



matrice_a_trou = convertir_grille(matrice_a_trou)
print(est_finissable(matrice_a_trou))

grille = np.array([
    [7, 8, 1, 5, 6, 3, 2, 4, 9],
    [4,5,2,9,1,7,6,3,8],
    [6,9,3,2,4,8,5,1,7],
    [3,5,4,6,8,0,9,1,8],
    [2,8,6,1,0,4,5,7,3],
    [1,7,9,3,8,5,4,2,6],
    [4,9,5,1,3,6,8,2,7],
    [8,6,1,7,2,9,3,4,5],
    [7,3,2,8,5,4,9,6,0]
])
print(est_finissable(grille))


"""
import matplotlib.pyplot as plt
import numpy as np

def afficher_grille(grille):
    plt.imshow(grille, cmap='tab20')
    plt.colorbar()
    plt.show()

matrice_a_trou = np.array([
    [5, 0, 7, 2, 0, 8, 6, 0, 4], [0, 0, 1, 0, 0, 6, 0, 8, 0], [0, 0, 0, 3, 9, 0, 0, 7, 5],
    [0, 0, 0, 1, 0, 0, 9, 7, 0], [0, 1, 3, 6, 0, 4, 8, 5, 0], [0, 5, 2, 0, 0, 3, 0, 0, 0],
    [3, 5, 0, 0, 4, 2, 0, 0, 0], [0, 4, 0, 1, 0, 0, 3, 0, 0], [2, 0, 7, 8, 0, 9, 0, 0, 1]
])

print("Grille avant conversion:")
afficher_grille(matrice_a_trou)

matrice_a_trou = convertir_grille(matrice_a_trou)

print("Grille après conversion:")
afficher_grille(matrice_a_trou)
"""