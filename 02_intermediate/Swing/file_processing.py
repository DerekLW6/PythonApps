# Reading a file
myfile = open('fruits.txt')

# Here is saving the contents
myContent = myfile.read()

# Closing the file
myfile.close()

# Printing
print(myContent)
