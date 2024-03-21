import tkinter as tk

def open_difficulty_page(difficulty):
    difficulty_page = tk.Toplevel(root)
    difficulty_page.title("Jeu du sudoku - Difficulté: " + difficulty)
    
    # Ajouter du contenu à la page de difficulté ici
    
    back_button = tk.Button(difficulty_page, text="Retour à l'accueil", command=difficulty_page.destroy)
    back_button.pack()
    
def open_main_page():
    main_page = tk.Toplevel(root)
    main_page.title("Jeu du sudoku")
    
    message_label = tk.Label(main_page, text="Choisissez votre difficulté")
    message_label.pack()
    
    simple_button = tk.Button(main_page, text="Simple", command=lambda: open_difficulty_page("Simple"))
    simple_button.pack()
    
    medium_button = tk.Button(main_page, text="Moyen", command=lambda: open_difficulty_page("Moyen"))
    medium_button.pack()
    
    difficult_button = tk.Button(main_page, text="Difficile", command=lambda: open_difficulty_page("Difficile"))
    difficult_button.pack()
    
    quit_button = tk.Button(main_page, text="Quitter", command=root.destroy)
    quit_button.pack()
    
root = tk.Tk()
root.title("Jeu du sudoku")

open_main_page()

root.mainloop()
