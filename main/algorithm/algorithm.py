# réfléchir à comment générer les tables pour le sudoku


import numpy as np
# générer aléatoirement une matrice de sudoku valide
# 1. générer une matrice aléatoire
# 2. vérifier que la matrice est valide
# 3. si la matrice n'est pas valide, recommencer
# 4. si la matrice est valide, la renvoyer

# génération matrice aléatoire
n = 3 # dimension souahaitée
m = n*n # dimension de la matrice
mat = np.zeros((m,m)) # matrice de sudoku vide
for i in range(m):
    for j in range(m):
        mat[i,j] = np.random.randint(1,m+1) # remplissage aléatoire de la matrice
print(mat)

# vérification de la validité de la matrice
# 1. vérifier que chaque ligne contient tous les entiers de 1 à m
for i in range(m):
    if set(mat[i,:]) != set(range(1,m+1)):
        print("ligne",i,"non valide")

# 2. vérifier que chaque colonne contient tous les entiers de 1 à m
for j in range(m):
    if set(mat[:,j]) != set(range(1,m+1)):
        print("colonne",j,"non valide")

# 3. vérifier que chaque carré contient tous les entiers de 1 à m
for i in range(n):
    for j in range(n):
        if set(mat[i*n:(i+1)*n,j*n:(j+1)*n].flatten()) != set(range(1,m+1)):
            print("carré",i,j,"non valide")
# 4. si toutes ces conditions sont vérifiées, la matrice est valide

if set(mat[i,:]) == set(range(1,m+1)) and set(mat[:,j]) == set(range(1,m+1)) and set(mat[i*n:(i+1)*n,j*n:(j+1)*n].flatten()) == set(range(1,m+1)):
    print("matrice valide")
else:
    print("matrice non valide")


# Évidement la génération aléatoire n'est pas la meilleure solution, il faut trouver une méthode plus efficace
# On peut par exemple générer une matrice valide et la modifier aléatoirement

# génération d'une matrice valide
mat = np.zeros((m,m)) # matrice de sudoku vide
for i in range(m):
    for j in range(m):
        mat[i,j] = (i*n + i//n + j) % m + 1 # remplissage de la matrice
print(mat)

# modification aléatoire de la matrice
# 1. choisir une ligne
# 2. choisir deux colonnes
# 3. échanger les deux colonnes
# 4. choisir deux carrés
# 5. échanger les deux carrés
# 6. choisir deux lignes
# 7. échanger les deux lignes
# 8. recommencer à l'étape 1

# modification : 
# 1. choisir une ligne
i = np.random.randint(0,m)
print("ligne",i)

# 2. choisir deux colonnes
j1 = np.random.randint(0,m)
j2 = np.random.randint(0,m)
print("colonnes",j1,"et",j2)

# 3. échanger les deux colonnes
mat[:,[j1,j2]] = mat[:,[j2,j1]]
print(mat)

# 4. choisir deux carrés
i1 = np.random.randint(0,n)
i2 = np.random.randint(0,n)
j1 = np.random.randint(0,n)
j2 = np.random.randint(0,n)
print("carrés",i1,j1,"et",i2,j2)

# 5. échanger les deux carrés
mat[i1*n:(i1+1)*n,j1*n:(j1+1)*n], mat[i2*n:(i2+1)*n,j2*n:(j2+1)*n] = mat[i2*n:(i2+1)*n,j2*n:(j2+1)*n], mat[i1*n:(i1+1)*n,j1*n:(j1+1)*n]
print(mat)

# 6. choisir deux lignes
i1 = np.random.randint(0,m)
i2 = np.random.randint(0,m)
print("lignes",i1,"et",i2)

# 7. échanger les deux lignes
mat[[i1,i2],:] = mat[[i2,i1],:]
print(mat)



