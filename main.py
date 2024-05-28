import numpy as np
import tkinter as tk
import solving_functions as SF # module des fonctions algorithmiques de complétion 
import copy

def set_window_geometry(window, width=600, height=600):
    # Récupère la largeur de l'écran
    screen_width = window.winfo_screenwidth()
    # Récupère la hauteur de l'écran
    screen_height = window.winfo_screenheight()

    # Calcule la position x de la fenêtre pour la centrer
    x = (screen_width // 2) - (width // 2)
    # Calcule la position y de la fenêtre pour la centrer
    y = (screen_height // 2) - (height // 2)

    # Définit la géométrie de la fenêtre (largeur, hauteur et position)
    window.geometry(f"{width}x{height}+{x}+{y}")
    return None

def fenetre_principale(): #fenêtre principale avec les boutons
    main_window = tk.Tk()
    set_window_geometry(main_window)
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
    
    global sudoku
    sudoku = SF.generate_sudoku(difficulty)
    
    parent_window.withdraw()  # cache la fenêtre principale
    difficulty_window = tk.Toplevel()
    set_window_geometry(difficulty_window)

    difficulty_window.title("Jeu du Sudoku - " + difficulty)
    
    label = tk.Label(difficulty_window, text=f"Difficulté: {difficulty}", font=("Arial", 16))
    label.pack(pady=20)

    frame = tk.Frame(difficulty_window)                             #créer une frame sur la fenetre de jeu soit difficulty_window
    frame.pack()                                                    #affiche la frame
    entries = [[0 for _ in range(9)] for _ in range(9)]             #créer une zone de 9*9 soit 81 cases dans cette frame
    
    
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                entries[i][j] = tk.Label(frame, text=str(sudoku[i][j]), relief="groove", font=('Times 18'), width=3, fg = 'black',justify= "center", bg= '#E5E5E5' )
            else:
                entries[i][j] = tk.Entry(frame, relief="groove", font=('Times 18'),width=3, fg = 'blue', justify= "center",bg= '#E5E5E5')
            entries[i][j].grid(row=i, column=j)   

#       ces deux boucles permettent de mettre dans chaque case du label 
#       soit un Label (c'est une zone de texte non modifiable) 
#       soit un Entry (c'est est une zone de texte modifiable par le joueur)
#       en fonction de la matrice tronqué  

    check_button = tk.Button(difficulty_window, text="Vérifier", command=lambda: verifier_grille(entries, difficulty_window))
    check_button.pack(pady=10)          

    sol_button = tk.Button(difficulty_window,text="Solution", command= lambda : fenetre_solution())
    sol_button.pack(pady=10)
    global result_label
    result_label = None

    btn_home = tk.Button(difficulty_window, text="Retour à l'accueil", command=lambda: return_to_main(difficulty_window, parent_window))
    btn_home.pack(pady=10)

def fenetre_solution():
    
    global sudoku
    unfilled_board = copy.deepcopy(sudoku)
    
    sol_window = tk.Tk()
    set_window_geometry(sol_window)
    sol_window.title("Jeu du Sudoku")
    
    frame = tk.Frame(sol_window)
    frame.pack(pady=50)
    entries = [[0 for _ in range(9)] for _ in range(9)]
    
    filled_board = SF.fill_board(sudoku)
    
    for i in range(9):
            for j in range(9):
                if unfilled_board[i][j] != 0:
                    entries[i][j] = tk.Label(frame, text=str(filled_board[1][i][j]), relief="ridge", font=('Times 18'), width=3, fg = 'black', justify= "center" )
                else:
                    entries[i][j] = tk.Label(frame, text=str(filled_board[1][i][j]), relief="ridge", font=('Times 18'), width=3, fg = 'blue', justify= "center")
                entries[i][j].grid(row=i, column=j) 
     

def return_to_main(window, parent_window):
    window.destroy()
    parent_window.deiconify()
    
    
def verifier_grille(entries, window):
    
    global result_label
    
    # récupérer les valeurs du joueur
    valeurs_grille = np.zeros((9, 9), dtype=int)

    for i in range(9):
        for j in range(9):
            if isinstance(entries[i][j], tk.Entry):  # Vérifier si c'est un Entry
                valeur = entries[i][j].get()  # Récupérer la valeur entrée par le joueur
                if valeur:  # Vérifier si une valeur a été entrée
                    valeurs_grille[i][j] = int(valeur)  # Stocker la valeur dans le tableau numpy
                else:  # Si le champ est vide
                    valeurs_grille[i][j] = 0
            else:  # Si c'est un Label
                valeur = entries[i][j]["text"]  # Récupérer le texte du label
                if valeur:
                    valeurs_grille[i][j] = int(valeur)  # Stocker la valeur dans le tableau numpy

    valeurs_grille = valeurs_grille.tolist()



    # Vérifier si c'est complétable
    is_completable = SF.is_completable(valeurs_grille)
    print(is_completable)
    

    if result_label is None:
        result_label = tk.Label(window)
        result_label.pack()

    # Update the label text based on the result
    if is_completable:
            result_label.config(text="Complétable", fg="green", font=("Helvetica", 16, "bold"))
    else:
        result_label.config(text="Incomplétable", fg="red", font=("Helvetica", 16, "bold"))

    return None


main_window = fenetre_principale()