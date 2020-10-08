# Reading from one file and appending it to another
with open('bear1.txt', "r") as myfile1:
    bear1 = myfile1.read()

with open('bear2.txt', "a") as myfile2:
    myfile2.write(bear1)

