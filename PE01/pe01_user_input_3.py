# Part 3: User Input finfing Odd Number

# 1. Get input from the user
user_input = input("Enter numbers separated by spaces: ")

# 2. Split the string into a list of individual strings
string_list = user_input.split()

# 3. Creating an empty list to store the odd numbers
odd_numbers = []

# 4. Loop through each item in our list
for item in string_list:
    # Convert the string into an integer
    number = int(item)
    
    # Check if the number is odd using the modulo operator (%)
    # If a number divided by 2 has a remainder of 1, it is odd
    if number % 2 != 0:
        odd_numbers.append(number)

# 5. Print the final result
print("Here are the odd numbers you entered:")
print(odd_numbers)