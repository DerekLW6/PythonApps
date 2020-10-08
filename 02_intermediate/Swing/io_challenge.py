def findLetter (letter, filepath = 'fruits.txt'):
    # Opening the file
    myfile = open(path)
    
    # Saving to a variable
    myContent = myfile.read()
    
    # Closing the file
    myfile.close()
    
    # Finding the string value
    count = myContent.count(letter) 
    return count

    

