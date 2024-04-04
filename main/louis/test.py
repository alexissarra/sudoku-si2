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


        for i in range(0,9):
            for j in range(0,9):
                for a in range(0,9,3):
                    for b in range(0,9,3):
                        self.entries[a][b] = tk.Label(self.frame, text=str(matrice_a_trou[i][j]), width=5, relief="ridge")
                        self.entries[a][b].grid(row=i, column=j)


        self.check_button = tk.Button(self.root, text="Vérifier", command=self.verify)
        self.check_button.pack()

    def verify(self):
        print(matrice_v_verif)


root = tk.Tk()
app = SudokuSolver(root)
root.mainloop()





#for a in range(0,9):
          #  for i in range(0,3):
           #      for j in range(0,3):
            #        if matrice_a_trou[a][i] != 0:
             #           self.entries[a][i] = tk.Label(self.frame, text=str(matrice_a_trou[i][j]), width=5, relief="ridge")
              #      else:
               #         self.entries[a][i] = tk.Entry(self.frame, width=5)
                #    self.entries[a][i].grid(row=i, column=j)