from math import sqrt

squares = [4, 9, 16, 25]
values = [1, 2, 3, 1, 2]
names = ["Eric", "anna", "Sophie", "sam"]
colours = ["red", "green", "yellow", "blue", "red"]

for i in range(len(squares)):
    print(sqrt(squares[i]))

squares.append(49)
squares.append(64)
squares.append(81)

squares.extend([121, 144, 169])

squares.remove(49)
print(squares)
values.remove(2)
print(values)

values.pop()
print(values)

names.sort(key=lambda n: str.upper(n))
print(names)

names.reverse()
print(names)

print(colours.index("blue"))
NewColours = colours
colours.append("test")
print(NewColours)


squares = [x * x * x for x in range(2, 20)]

