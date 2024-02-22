from tkinter import *

frame = Tk()

frame.geometry("320x320")

canvas = Canvas(frame, width=320, height=320, bg="SpringGreen2")

canvas.create_text(100, 100, text="Some Text", fill="black", font=("Helvetica 15 bold"))

canvas.pack()
frame.mainloop()