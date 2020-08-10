parrot = "Norwegian Blue"

for character in parrot:
    print(character)

number = "9,456,789,1233,852,963,741"
separarters = ""

for char in number:
    if not char.isnumeric():
        separarters = separarters + char

print(separarters)

# range
for i in range(1, 20):
    print("i is {}".format(i))

# steps
for i in range(0, 10, 2):
    print(i)

# negative step
for i in range(10, 0, -2):
    print(i)

# divisible by 7
for i in range(0, 100, 7):
    print(i)
