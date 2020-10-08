with open('..//00_files//vegetables.txt', "a+") as myfile:
    myfile.write("\nDerek")
    myfile.seek(0)
    content = myfile.read()


print(content)