import tkinter

window = tkinter.Tk()
window.title("Tkinter First Window")  # Name the title
label = tkinter.Label(window,text = "Hello World").pack()
window.mainloop()
