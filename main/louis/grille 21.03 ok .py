import tkinter as tk
import numpy as np

class SudokuSolver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")

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

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self)
        self.frame.pack()

        self.entries = []
        for i in range(9):
            row_entries = []
            for j in range(9):
                value = matrice_a_trou[i, j]
                if value == 0:
                    entry = tk.Entry(self.frame, width=2, font=('Helvetica', 16), justify='center')
                    entry.grid(row=i, column=j)
                    row_entries.append(entry)
                else:
                    label = tk.Label(self.frame, text=str(value), font=('Helvetica', 16), width=2, relief='ridge')
                    label.grid(row=i, column=j)
                    row_entries.append(label)
            self.entries.append(row_entries)

        self.verify_button = tk.Button(self, text="Vérifier", command=recuperer_valeurs_grille)
        self.verify_button.pack()

def recuperer_valeurs_grille():
       grille_joueur = []
       for i in range(9):
           row_values = []
           for j in range(9):
               if isinstance(self.entries[i][j], tk.Entry):
                   value = self.entries[i][j].get()
                   if value.isdigit():
                       row_values.append(int(value))
                   else:
                       row_values.append(0)
               else:
                   row_values.append(self.matrice_a_trou[i][j])
           grille_joueur.append(row_values)
       grille_joueur = np.array(grille_joueur)
       print("Grille du joueur:")
       print(grille_joueur)


if __name__ == "__main__":
    app = SudokuSolver()
    app.mainloop()
