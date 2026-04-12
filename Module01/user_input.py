name = input("Please enter your name: ")
print("\nWelcome to DS522 class, " + name + "!")
print("The data type of the variable name is", type(name))

age = input("\nEnter your age: ")
age = int(age) #converts the string to int type
print("\nYour age is ", age)
print("The data type of the variable age is", type(age))

# Let me try to multiply
user_input = "5"  
multiplier = 3

result = user_input * multiplier

print(f"Result: {result}") 
# Output: 555 (This is quite Unexpected, I wanted 15)