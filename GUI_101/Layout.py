import tkinter

window = tkinter.Tk()
window.title('Layout Learning codes')

# top and bottom frame
topFrame = tkinter.Frame(window).pack()
bottomFrame = tkinter.Frame(window).pack(side="bottom")

btn1 = tkinter.Button(topFrame,text="Button 1", fg='green').pack()
btn2 = tkinter.Button(topFrame,text="Button 2", fg='red').pack()
btn3 = tkinter.Button(bottomFrame,text="Button 3", fg='purple').pack(side="left")
btn4 = tkinter.Button(bottomFrame,text="Button 4", fg='blue').pack(side="left")


window.mainloop()