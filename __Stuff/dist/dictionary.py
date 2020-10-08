from tkinter import * 
import json
from difflib import get_close_matches

data = json.load(open('.\\_completed_apps\\Dictionary_App\\full_app\\data.json'))  

def lookup():
    # Clearning the list
    list1.delete('1.0', END)

    # Converting the user input to string and lowering it
    word = str(word_input.get())
    word = word.lower() 

# Printing to the screen
    if word in data:
        list1.insert(END, data[word])

    elif len(get_close_matches(word, data.keys())) > 0:
        string = "Did you mean %s instead? " % get_close_matches(word, data.keys())[0]
        list1.insert(END, string)   
        
    else:
        string2 = 'Word not found. Please try again.'
        list1.insert(END, string2)  
  
# Build the Framework
window = Tk()

window.wm_title("Dictionary")

# Entering a Word (Label)
l1=Label(window,text="Enter a Word")
l1.grid(row=0, column=0)

# Entering a Word (Field)
word_input = StringVar()
e1=Entry(window, textvariable = word_input)
e1.grid(row=0,column=1)

list1 = Text(window, wrap =WORD)
list1.grid(row=2, column=0,rowspan=20, columnspan=6)

# Add the lookup button   //// command = basic(str(word_input)) # (word_input.get())
b1 = Button(window, text= "Search", width = 12, command=lookup)
b1.grid(row=0, column=10)

# Adding the close button
b2 = Button(window, text="Close", width = 12, command = window.destroy)
b2.grid(row=25, column=10)

window.mainloop()

