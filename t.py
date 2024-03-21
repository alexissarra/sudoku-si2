import tkinter as tk
from tkinter import ttk

def open_difficulty_page(difficulty):
    difficulty_page = tk.Toplevel(root)
    difficulty_page.title("Jeu du Sudoku - Difficulté: " + difficulty)
    
    message = tk.Label(difficulty_page, text=difficulty)
    message.pack()
    
    back_button = ttk.Button(difficulty_page, text="Retour à l'accueil", command=difficulty_page.destroy)
    back_button.pack()

def open_main_page():
    # Détruit la fenêtre précédente
    if 'main_page' in globals():
        main_page.destroy()
        
    main_page = tk.Toplevel(root)
    main_page.title("Jeu du Sudoku")
    
    message_label = tk.Label(main_page, text="Choisissez votre difficulté")
    message_label.pack()
    
    simple_button = ttk.Button(main_page, text="Simple", command=lambda: open_difficulty_page("Simple"))
    simple_button.pack()
    
    medium_button = ttk.Button(main_page, text="Normal", command=lambda: open_difficulty_page("Normal"))
    medium_button.pack()
    
    difficult_button = ttk.Button(main_page, text="Difficile", command=lambda: open_difficulty_page("Difficile"))
    difficult_button.pack()
    
    ginot_button = ttk.Button(main_page, text="Ginot", command=lambda: open_difficulty_page("Ginot"))
    ginot_button.pack()
    
    quit_button = ttk.Button(main_page, text="Quitter", command=root.quit)
    quit_button.pack()

root = tk.Tk()
root.title("Jeu du Sudoku")
root.geometry('600x400+50+50')

# Création du message d'accueil
message = tk.Label(root, text="Cliquez pour commencer")
message.pack()

# Bouton pour ouvrir la page principale
start_button = ttk.Button(root, text="Commencer", command=open_main_page)
start_button.pack()

root.mainloop()
