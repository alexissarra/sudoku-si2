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


def fenetre_principale(): #fenêtre principale avec les boutons
    main_window = tk.Tk()
    main_window.geometry("1000x1000+50+50")
    main_window.title("Jeu du Sudoku")
   
    label = tk.Label(main_window, text="Choisissez votre difficulté", font=("Arial", 16))
    label.pack(pady=20)
    
    btn_simple = tk.Button(main_window, text="Simple",bg='green',fg="white", command=lambda: fenetre_difficulté("Simple", main_window)) # bouton simple 
    btn_simple.pack(pady=10)
    
    btn_medium = tk.Button(main_window, text="Moyen",bg='orange',fg="white", command=lambda: fenetre_difficulté("Moyen", main_window))
    btn_medium.pack(pady=10)
    
    btn_hard = tk.Button(main_window, text="Difficile",bg='red',fg="white", command=lambda: fenetre_difficulté("Difficile", main_window))
    btn_hard.pack(pady=10)

    btn_ginot = tk.Button(main_window, text="Ginot",bg='black',fg="white", command=lambda: fenetre_difficulté("Ginot", main_window))
    btn_ginot.pack(pady=10)

    btn_quit = tk.Button(main_window, text="Quitter", command=main_window.quit)
    btn_quit.pack(pady=10)
    
    main_window.mainloop()

def fenetre_difficulté(difficulty, parent_window): # créer une fenêtre en fonction de la difficulté sélectionné
    parent_window.withdraw()  # cache la fenêtre principale
    difficulty_window = tk.Toplevel()
    difficulty_window.geometry("1000x1000+50+50")
    difficulty_window.title("Jeu du Sudoku - " + difficulty)
    
    label = tk.Label(difficulty_window, text=f"Difficulté: {difficulty}", font=("Arial", 16))
    label.pack(pady=20)

    frame = tk.Frame(difficulty_window)
    frame.pack()
    entries = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if matrice_a_trou[i][j] != 0:
                entries[i][j] = tk.Label(frame, text=str(matrice_a_trou[i][j]), relief="groove", font=('Times 18'), width=3, fg = 'black',justify= "center", bg= '#E5E5E5' )
            else:
                entries[i][j] = tk.Entry(frame, relief="groove", font=('Times 18'),width=3, fg = 'blue', justify= "center",bg= '#E5E5E5')
            entries[i][j].grid(row=i, column=j)  

    check_button = tk.Button(difficulty_window, text="Vérifier", command=lambda: recuperer_valeurs_grille(entries))
    check_button.pack(pady=10)          

    sol_button = tk.Button(difficulty_window,text="Solution", command= lambda : fenetre_solution())
    sol_button.pack(pady=10)

    btn_home = tk.Button(difficulty_window, text="Retour à l'accueil", command=lambda: return_to_main(difficulty_window, parent_window))
    btn_home.pack(pady=10)

def fenetre_solution():
    sol_window = tk.Tk()
    sol_window.geometry("600x400+50+50")
    sol_window.title("Jeu du Sudoku")
    
    frame = tk.Frame(sol_window)
    frame.pack(pady=50)
    entries = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if matrice_a_trou[i][j] != 0:
                entries[i][j] = tk.Label(frame, text=str(matrice_a_trou[i][j]), relief="ridge", font=('Times 18'), width=3, fg = 'black', justify= "center" )
            else:
                entries[i][j] = tk.Label(frame, text=str(matrice_valide[i][j]), relief="ridge", font=('Times 18'), width=3, fg = 'blue', justify= "center")
            entries[i][j].grid(row=i, column=j)  
    

    

def return_to_main(window, parent_window):
    window.destroy()
    parent_window.deiconify()

def quit_all():
    main_window.quit()

def recuperer_valeurs_grille(entries):
    valeurs_grille = np.zeros((9, 9), dtype=int)

    for i in range(9):
         for j in range(9):
                if isinstance(entries[i][j], tk.Entry):  # Vérifier si c'est un Entry
                    valeur = entries[i][j].get()  # Récupérer la valeur entrée par le joueur
                    if valeur:  # Vérifier si une valeur a été entrée
                        valeurs_grille[i][j] = int(valeur)  # Stocker la valeur dans le tableau numpy
                else:  # Si c'est un Label
                    valeur = entries[i][j]["text"]  # Récupérer le texte du label
                    if valeur:
                        valeurs_grille[i][j] = int(valeur)  # Stocker la valeur dans le tableau numpy


    print("Valeurs de la grille entrées par le joueur :")
    print(valeurs_grille)
    return valeurs_grille



if __name__ == "__main__":
    main_window = fenetre_principale()
