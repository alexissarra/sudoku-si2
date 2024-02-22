import tkinter as tk

gui = tk.Tk()
gui.geometry("300x100")

def getEntry():
    res = myEntry.get()
    print(res)

myEntry = tk.Entry(gui, width=40)
myEntry.pack(pady=20)

btn = tk.Button(gui, height=1, width=10, text="Lire", command=getEntry)
btn.pack()

gui.mainloop()