age = 24
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))

age = 24
print("age is {0}".format(age))
print(f"age is {age}")

print(f"Pi = {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi = {pi:12.50f}")