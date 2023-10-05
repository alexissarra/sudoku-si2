# Création d'un solveur de sudoku
#   1. choisir une case vide
#   2. choisir un chiffre
#   3. tester si le chiffre est valide
#   4. si oui, remplacer la case vide par le chiffre
#   5. si non, recommencer à l'étape 2
#   6. recommencer à l'étape 1


import numpy as np

# génération d'une matrice valide
def matrice_valide(n):
    m = n**2
    mat = np.zeros((m,m)) # matrice de sudoku vide
    for i in range(m):
        for j in range(m):
            mat[i,j] = (i*n + i//n + j) % m + 1 # remplissage de la matrice
    return mat

print (matrice_valide(3))

# Enlèvement des deux diagonales
for i in range ()