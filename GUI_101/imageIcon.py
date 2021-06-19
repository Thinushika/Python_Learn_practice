import tkinter

window = tkinter.Tk()
window.title("image")

icon = tkinter.PhotoImage(file = r"C:\Users\TJ\Downloads\Images\hair cut.png")
label = tkinter.Label(window, image = icon)
label.pack()

window.mainloop()