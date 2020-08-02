#         0123456789
parrot = "Norwegian Blue"

print(parrot[0:6])
print(parrot[3:6])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

# negative slicing
print(parrot[-4:-2])
print(parrot[-4:-12])
print(parrot[0:6])

# step slicing
print(parrot[0:6:2])
print(parrot[1::4])

letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]

print(backwards)

backwards1 = letters[25::-1]
print(backwards1)

backwards2 = letters[::-1]
print(backwards2)


