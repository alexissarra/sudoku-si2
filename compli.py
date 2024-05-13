import tkinter as tk


def fenetre_principale(): #fenêtre principale avec les boutons
    main_window = tk.Tk()
    main_window.geometry("600x400+50+50")
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
    difficulty_window.geometry("600x400+50+50")
    difficulty_window.title("Jeu du Sudoku - " + difficulty)
    
    label = tk.Label(difficulty_window, text=f"Difficulté: {difficulty}", font=("Arial", 16))
    label.pack(pady=20)
    
    btn_home = tk.Button(difficulty_window, text="Retour à l'accueil", command=lambda: return_to_main(difficulty_window, parent_window))
    btn_home.pack(pady=10)

def return_to_main(window, parent_window):
    window.destroy()
    parent_window.deiconify()

def quit_all():
    main_window.quit()

if __name__ == "__main__":
    main_window = fenetre_principale()
