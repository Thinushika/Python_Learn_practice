import tkinter

window = tkinter.Tk()
window.title("Hi")

# sufficient width
tkinter.Label(window,text="Suf. width", fg="white",bg="black").pack()

# width of X
tkinter.Label(window,text="Taking all available X width", fg="white",bg="purple").pack(fill="x")

# height of Y
tkinter.Label(window,text="Taking all available Y height", fg="white",bg="green").pack(side="left", fill="y")

window.mainloop()