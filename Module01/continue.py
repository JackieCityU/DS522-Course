print("For-Continue")
for letter in "Python":
    if letter == 'h':
        continue
    print("Current Letter:", letter)

print("\nWhile-Continue")
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print("Current variable value:", var)

print("Good bye!")

# Challene: I will search for number 7
numbers = [1, 3, 5, 9]

for n in numbers:
    if n == 7:
        print("Found it!")
        break
else:
    print("The number 7 was not in the list.")