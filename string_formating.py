for i in range(1, 13):
    print("No : {0}\tSquare : {1}\tCube : {2}".format(i, i ** 2, i ** 3))

# formatting
for i in range(1, 13):
    print("No : {0:2}\tSquare : {1:3}\tCube : {2:4}".format(i, i ** 2, i ** 3))

# left formatting
for i in range(1, 13):
    print("No : {0:<2}\tSquare : {1:<3}\tCube : {2:<4}".format(i, i ** 2, i ** 3))


print()
print("pi = {0:12}".format(22 / 7))
print("pi = {0:12f}".format(22 / 7))
print("pi = {0:12.50f}".format(22 / 7))
print("pi = {0:52.50f}".format(22 / 7))
print("pi = {0:62.50f}".format(22 / 7))
print("pi = {0:72:50f}".format(22 / 7))
print("pi = {0:<72:54f}".format(22 / 7))
 