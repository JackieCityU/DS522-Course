def print_numbers(limit):
    "This prints a list of numbers starting 0 to the limit-1"
    i = 0  # initialize the value of i to 0
    numbers = []

    # Continue appending values to the numbers list until the limit is reached
    while i < limit:
        numbers.append(i)
        i = i + 1  # increment to 1 at each iteration

    return numbers  # return the final list

# User input to specify the limit
user_limit = int(input("Give a limit: "))  # convert the string default input value to int & assign to a variable
print(print_numbers(user_limit))

# Define a function called printme
def print_text(str):
    "This prints a passed string into this function"
    print(str)
    return

# Call the function
print_text("First call to the user-defined function.")
print_text("Second call to the same user-defined function.")