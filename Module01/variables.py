print("\nMultiple Assignments\n")
x, y, z = 1, 2.0, "Three"
print(x)
print(y)
print(z)

x = y = z = "Python"

print("X: ", x)
print("Y: ", y)
print("Z: ", z)


# 1. Start as an integer
data = 100
print(f"Value: {data}, Type: {type(data)}")

# 2. Change the same variable to a string
data = "Now I am a string"
print(f"Value: {data}, Type: {type(data)}")

# 3. Change again to a list
data = [1, 2, 3]
print(f"Value: {data}, Type: {type(data)}")

#Python is dynamically typed. This means the "type" is attached to the object (the data itself), not the variable name. 
# Think of the variable name as a label or a sticky note. 
# You can peel that "data" label off a box containing a number and stick it onto 
# a box containing a string whenever you want.