import numpy as np
import tkinter as tk

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

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.entries = [[0 for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if matrice_a_trou[i][j] != 0:
                    self.entries[i][j] = tk.Label(self.frame, text=str(matrice_a_trou[i][j]), width=5, relief="ridge")
                else:
                    self.entries[i][j] = tk.Entry(self.frame, width=5)
                self.entries[i][j].grid(row=i, column=j)

        self.check_button = tk.Button(self.root, text="Vérifier", command=self.recuperer_valeurs_grille)
        self.check_button.pack()

    def recuperer_valeurs_grille(self):
        valeurs_grille = np.zeros((9, 9), dtype=int)  # Créer un tableau numpy de la même forme que les grilles

        for i in range(9):
         for j in range(9):
                if isinstance(self.entries[i][j], tk.Entry):  # Vérifier si c'est un Entry
                    valeur = self.entries[i][j].get()  # Récupérer la valeur entrée par le joueur
                    if valeur:  # Vérifier si une valeur a été entrée
                        valeurs_grille[i][j] = int(valeur)  # Stocker la valeur dans le tableau numpy
                else:  # Si c'est un Label
                    valeur = self.entries[i][j]["text"]  # Récupérer le texte du label
                    if valeur:
                        valeurs_grille[i][j] = int(valeur)  # Stocker la valeur dans le tableau numpy

        print("Valeurs de la grille entrées par le joueur :")
        print(valeurs_grille)

        return valeurs_grille

                


root = tk.Tk()
app = SudokuSolver(root)
root.mainloop()
