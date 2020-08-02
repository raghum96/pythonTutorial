splitString = "The string has been \nsplit iver \nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3"
print(tabbedString)

print('Hey bro "How are you"?')
print("Hey bro \"How are you\"?")
print("""Hey bro "How are you"?""")

anotherSplitString = """hey
bro"""
print(anotherSplitString)

anotherNotSplitString = """hey \
bro"""
print(anotherNotSplitString)

print("C:\\Users\\test\\notes")
print(r"C:\Users\test\notes")

age = 24
greeting = "hey"
print(type(age))
print(type(greeting))

# TypeError: can only concatenate str (not "int") to str
# print("name" + age)

print("name" + str(age))

age = "2 years"
print(age)
print(type(age))
