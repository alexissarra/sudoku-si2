import tkinter as tk
from tkinter import messagebox
import numpy as np

# Matrices fournies
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

# Fonction pour vérifier la solution
def verifier_solution():
    # Récupérer la matrice entrée par l'utilisateur
    matrice_verif = np.array([[int(entries[i][j].get()) for j in range(9)] for i in range(9)])
    
    # Comparer avec la solution valide
    if np.array_equal(matrice_verif, matrice_valide):
        messagebox.showinfo("Résultat", "Bravo ! Sudoku résolu correctement.")
    else:
        messagebox.showerror("Résultat", "Sudoku incorrect. Veuillez vérifier votre solution.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Résolution Sudoku")

# Créer les cases de saisie pour le sudoku
entries = []
for i in range(9):
    row = []
    for j in range(9):
        if matrice_a_trou[i][j] != 0:
            entry = tk.Entry(root, width=2, font=('Helvetica', 20, 'bold'), bd=5, justify='center', state='disabled')
            entry.insert(0, str(matrice_a_trou[i][j]))
        else:
            entry = tk.Entry(root, width=2, font=('Helvetica', 20, 'bold'), bd=5, justify='center')
        entry.grid(row=i, column=j)
        row.append(entry)
    entries.append(row)

# Créer le bouton pour vérifier la solution
verifier_button = tk.Button(root, text="Vérifier", command=verifier_solution)
verifier_button.grid(row=9, columnspan=9)

# Afficher la fenêtre
root.mainloop()
