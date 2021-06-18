import tkinter
from tkinter.ttk import* # for combo box
from tkinter import scrolledtext # for scrolledtext
from tkinter import messagebox # for messageBox

window = tkinter.Tk()
# Name the title
window.title("Tkinter First Window")  

# make label
label = tkinter.Label(window,text = "Hello World", font=("Arial Bold",50))

#click event for button
def clicked():
    label.configure(text="Button was clicked !!")

# create button
bt1 = tkinter.Button(window, text="Enter", bg="green", fg="white", command=clicked)


# create entry widget (Text box)
txt = tkinter.Entry(window,width=10)
def txtClicked():
    res = "welcome to "+ txt.get()
    label.configure(text=res)
# button 2 clicked
bt2 = tkinter.Button(window, text="Enter", bg="green", fg="white", command=txtClicked)


# create combo box
combo = Combobox(window)
combo['values'] = (1,2,3,4,5,"Text")
combo.current(3)


# create check button
chk_state = tkinter.BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Select', var=chk_state) # var is to pass the chk_state to the chckbutton class to set the check state


# create radio button
rad1 = Radiobutton(window,text= "Python" , value = 1)
rad2 = Radiobutton(window,text= "Java" , value = 2)
rad3 = Radiobutton(window,text= "R" , value = 3)


# create scroll text
txtScroll = scrolledtext.ScrolledText(window, width= 40, height=10)


# create messageBox
def MssagePop():
    messagebox.showinfo('Alart', 'Hi, You got it')

msgBt = Button(window,text='Enter for message', command=MssagePop)


#SpinBox
spin = Spinbox(window,from_=0,to=100, width=5)


# positioning
label.grid(column=0,row=0)
bt1.grid(column=0,row=1)
bt2.grid(column=0,row=2)
txt.grid(column=0,row=3)
combo.grid(column=0,row=4)
chk.grid(column=0, row=5)
rad1.grid(column=0,row=6)
rad2.grid(column=1,row=6)
rad3.grid(column=2,row=6)
txtScroll.grid(column=0,row=7)
msgBt.grid(column=0,row=8)
spin.grid(column=0,row=9)

window.geometry('600x450') # make window size
window.mainloop()