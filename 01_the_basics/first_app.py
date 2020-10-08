text_list = []
modified_text_list = []
interrogatives = ('How', 'What', 'Why')

while True:
    user_input = input("Say something: ")

    if user_input == '\end':
        for element in text_list:
            x = element.capitalize()
            if x.startswith(interrogatives):
                x = x + "?"
                modified_text_list.append(x)
            else:
                x = x + "."
                modified_text_list.append(x)
        break
    else:
        text_list.append(user_input)
        continue
    
print(" ".join(modified_text_list))
        