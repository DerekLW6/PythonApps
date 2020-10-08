from tkinter import * 

window = Tk()

def km_to_miles():
    # print(e1_value.get())
    miles = float(e1_value.get())/1.6
    t1.insert(END, miles)

# Adding a Button Widget
b1 = Button(window, text="Execute", command = km_to_miles) # this the above function
b1.grid(row=0, column=0, rowspan=1)

# Entry Widget 
e1_value = StringVar() # This allowed you to save the string object
e1 = Entry(window, textvariable=e1_value) # Getting the variable
e1.grid(row=0, column=1)

# Text Widget
t1 = Text(window, height =1, width=20)
t1.grid(row=0, column=2)

window.mainloop()



