import tkinter

window = tkinter.Tk()
window.title("Binding")

def Hi(event):
    tkinter.Label(window, text="Hi").pack()

#tkinter.Button(window,text="click me", command=Hi).pack()

#binding using mouse button
btn = tkinter.Button(window, text="click me")
btn.bind("<Button-1>",Hi)
btn.pack()


window.mainloop()