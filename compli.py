import tkinter as tk


def create_main_window():
    main_window = tk.Tk()
    main_window.geometry("600x400+50+50")
    main_window.title("Jeu du Sudoku")
   
    label = tk.Label(main_window, text="Choisissez votre difficulté", font=("Arial", 16))
    label.pack(pady=20)
    
    btn_simple = tk.Button(main_window, text="Simple",bg='green',fg="white", command=lambda: create_difficulty_window("Simple", main_window))
    btn_simple.pack(pady=10)
    
    btn_medium = tk.Button(main_window, text="Moyen",bg='orange',fg="white", command=lambda: create_difficulty_window("Moyen", main_window))
    btn_medium.pack(pady=10)
    
    btn_hard = tk.Button(main_window, text="Difficile",bg='red',fg="white", command=lambda: create_difficulty_window("Difficile", main_window))
    btn_hard.pack(pady=10)

    btn_ginot = tk.Button(main_window, text="Ginot",bg='black',fg="white", command=lambda: create_difficulty_window("Ginot", main_window))
    btn_ginot.pack(pady=10)

    btn_quit = tk.Button(main_window, text="Quitter", command=main_window.quit)
    btn_quit.pack(pady=10)
    
    main_window.mainloop()

def create_difficulty_window(difficulty, parent_window):
    parent_window.withdraw()  # Hide the parent window
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
    main_window = create_main_window()
