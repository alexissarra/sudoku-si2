import random
import numpy as np

def generate_sudoku(difficulty):
    # Un difficulté correspond au nombre d'éléments (en %) qui sont soustraits à la grille d'origine (complète)
    if difficulty == 'Simple':
        difficulty_ratio = 0.3
    elif difficulty == 'Moyen':
        difficulty_ratio = 0.4
    elif difficulty == 'Difficile':
        difficulty_ratio = 0.5
    elif difficulty == 'Ginot':
        difficulty_ratio = 0.6  
    else:
        raise ValueError('Difficulté de niveau invalide')
    
    
    # Crée un tableau 9x9 (la grille vide de Sudoku) rempli de zéros par compréhension
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    fill_board(board) # crée une grille complète de jeu
    clear_cells(board, difficulty_ratio) # enlève un % d'éléments dans la grille selon la difficulté
    
    return board






def fill_board(board):
    # Parcourt chaque cellule du tableau
    for i in range(9):
        for j in range(9):
            # Si la cellule est vide
            if board[i][j] == 0:
                # Crée une liste de nombres de 1 à 9
                numbers = list(range(1, 10))
                # Mélange la liste
                random.shuffle(numbers)
                # Parcourt chaque nombre de la liste
                for number in numbers:
                    # Si le nombre est valide dans cette position
                    if is_valid(board, i, j, number):
                        # Ajoute le nombre à la cellule
                        board[i][j] = number
                        # Essaye de remplir le reste du tableau
                        result, filled_board = fill_board(board)
                        # Si le reste du tableau a été rempli avec succès
                        if result:
                            return True, filled_board
                        # Si le reste du tableau n'a pas pu être rempli, retire le nombre
                        board[i][j] = 0
                # Si aucun nombre n'est valide dans cette cellule, retourne False
                return False, board
    # Si toutes les cellules sont remplies, retourne True
    return True, board

'''
La fonction fill_board utilise une technique appelée "backtracking",
ou retour sur trace. C'est une approche algorithmique qui tente de trouver une solution
à un problème en essayant toutes les possibilités une par une jusqu'à ce qu'une solution acceptable soit trouvée.

Cette fonction remplit un tableau Sudoku vide.
Elle parcourt chaque cellule du tableau.
Si une cellule est vide, elle crée une liste de nombres de 1 à 9, mélange la liste,
et parcourt chaque nombre de la liste. Si un nombre est valide dans cette position,
elle ajoute le nombre à la cellule et essaie de remplir le reste du tableau.
Si le reste du tableau a été rempli avec succès, elle retourne True. Si le reste du tableau n'a pas pu être rempli,
elle retire le nombre et essaie le suivant. Si aucun nombre n'est valide dans une cellule, elle retourne False.
Si toutes les cellules sont remplies, elle retourne True.

'''






def is_valid(board, row, col, number):
    # Vérifie si le nombre est un entier et dans la plage autorisée
    if not isinstance(number, int) or number < 1 or number > 9:
        return False

    # Vérifie la ligne
    for x in range(9):
        if board[row][x] == number:
            return False

    # Vérifie la colonne
    for x in range(9):
        if board[x][col] == number:
            return False

    # Vérifie la boîte 3x3
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == number:
                return False

    return True

'''
Cette fonction vérifie si un nombre est valide dans une certaine position d'un tableau Sudoku.
Elle vérifie d'abord si le nombre est un entier et s'il est dans la plage autorisée (1 à 9).
Ensuite, elle vérifie si le nombre est déjà présent dans la même ligne,
la même colonne ou la même boîte 3x3.
Si le nombre est déjà présent dans l'une de ces positions, la fonction retourne False.
Si le nombre n'est présent dans aucune de ces positions, la fonction retourne True.
'''




def clear_cells(board, difficulty):
    # Définit la taille totale du tableau (9x9 car fixé ainsi dans le projet)
    size = 9 * 9
    # Calcule le nombre de cellules à vider en fonction de la difficulté
    cells_to_clear = int(size * difficulty)

    # Tant qu'il reste des cellules à vider
    while cells_to_clear > 0:
        # Choisis une ligne et une colonne au hasard
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        # Si la cellule n'est pas déjà vide
        if board[row][col] != 0:
            # Vide la cellule
            board[row][col] = 0
            # Décrémente le nombre de cellules à vider
            cells_to_clear -= 1
'''
Cette fonction vide un certain nombre de cellules d'un tableau Sudoku en fonction de la difficulté spécifiée.
Elle choisit une cellule au hasard et, si elle n'est pas déjà vide,
la vide et décrémente le nombre de cellules à vider.
Elle répète ce processus jusqu'à ce que le nombre requis de cellules ait été vidé.
''' 
  
  
            
def is_valid_sudoku(board):
    # Parcourt chaque cellule du tableau
    for i in range(9):
        for j in range(9):
            # Récupère le nombre dans la cellule
            number = board[i][j]
            # Si la cellule n'est pas vide
            if number != 0:
                # Retire temporairement le nombre de la cellule
                board[i][j] = 0
                # Si le nombre n'est pas valide dans cette position
                if not is_valid(board, i, j, number):
                    # Remet le nombre et retourne False
                    board[i][j] = number
                    return False
                # Remet le nombre
                board[i][j] = number
    # Si tous les nombres sont valides, retourne True
    return True
'''
Cette fonction vérifie si un tableau Sudoku est valide.
Elle parcourt chaque cellule du tableau. Si une cellule n'est pas vide,
elle retire temporairement le nombre de la cellule et vérifie si le nombre est valide dans cette position.
Si le nombre n'est pas valide, elle remet le nombre et retourne False. Si tous les nombres sont valides,
elle retourne True.
'''


def is_completable(board):
    # Vérifie si le tableau Sudoku est valide
    if not is_valid_sudoku(board):
        return False

    # Parcourt chaque cellule du tableau
    for i in range(9):
        for j in range(9):
            # Si la cellule est vide
            if board[i][j] == 0:
                # Essaye tous les nombres de 1 à 9
                for number in range(1, 10):
                    # Si le nombre est valide dans cette position
                    if is_valid(board, i, j, number):
                        # Ajoute le nombre à la cellule
                        board[i][j] = number
                        # Si le tableau est complétable avec ce nombre
                        if is_completable(board):
                            return True
                        # Si le tableau n'est pas complétable, retire le nombre
                        board[i][j] = 0
                # Si aucun nombre n'est valide dans cette cellule, retourne False
                return False
    # Si toutes les cellules sont remplies, retourne True
    return True

'''
Cette fonction vérifie si un tableau Sudoku est complétable. Elle utilise une approche de backtracking,
où elle essaie chaque nombre de 1 à 9 dans chaque cellule vide. 
Si un nombre est valide dans une cellule
(c'est-à-dire qu'il ne se trouve pas déjà dans la même ligne, colonne ou carré 3x3),
elle ajoute le nombre à la cellule et vérifie si le tableau est complétable avec ce nombre.
Si le tableau n'est pas complétable, elle retire le nombre et essaie le suivant.
Si aucun nombre n'est valide dans une cellule, elle retourne False.
Si toutes les cellules sont remplies, elle retourne True.
'''