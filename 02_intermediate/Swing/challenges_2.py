with open('data.txt', "a+") as myfile:
    myfile.seek(0)
    data = myfile.read()
    myfile.seek(0)
    myfile.write(data)
    myfile.write(data)


    