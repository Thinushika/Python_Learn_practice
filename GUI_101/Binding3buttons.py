import tkinter

window = tkinter.Tk()
window.title("Binding")


# left click
def left_click(event):
    tkinter.Label(window,text="Left click").pack()

# middle click
def moddle_click(event):
    tkinter.Label(window,text="Middle click").pack()

# right click
def right_click(event):
    tkinter.Label(window,text="Right click").pack()

# binding
window.bind("<Button-1>", left_click)
window.bind("<Button-2>", moddle_click)
window.bind("<Button-3>", right_click)

window.mainloop()