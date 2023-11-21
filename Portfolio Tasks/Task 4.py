def encryption():
    newText = text.replace(" ", "")
    print(newText[::-1])


text = input("Please enter some text ")
print(encryption())
