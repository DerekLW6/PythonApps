from tkinter import * 

window = Tk()

# Coversion Function
def convert():
    # Grams Text Area
    grams = float(e1_value.get())*1000
    t1.insert(END, grams)

    # Pounds
    lbs = float(e1_value.get())*2.20462
    t2.insert(END, lbs)

    # Pounds
    ounces = float(e1_value.get())*35.274
    t3.insert(END, ounces)

# UI Label
e2=Label(window,text="Kg")
e2.grid(row=0,column=0)

# Adding a Button Widget
b1 = Button(window, text="Convert", command = convert) 
b1.grid(row=0, column=6, rowspan=1)

# Entry Widget 
e1_value = StringVar() 
e1 = Entry(window, textvariable=e1_value) 
e1.grid(row=0, column=4)

# Text Widget 1
t1 = Text(window, height =1, width=20)
t1.grid(row=4, column=2)

# Text Widget 2
t2 = Text(window, height =1, width=20)
t2.grid(row=4, column=4)

# Text Widget 3
t3 = Text(window, height = 1, width=20)
t3.grid(row=4, column=6)

window.mainloop()