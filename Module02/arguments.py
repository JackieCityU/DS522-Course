#Function definition is here
def student_info(name, major, gpa):
    "This prints the passed info into this function"
    print(f"Name: {name}")  # Use f-string to print string and assigned value
    print(f"Major: {major}")
    print(f"GPA: {gpa}")
    return

# Call the student_info function to print the values provided
print("----- Positionale Arguments ----- ")
student_info("Ezra Berthalomew Johnson", "Neuroscience; Arts", 3.95)

print("------Keyword Arguments-----")
student_info(name="John Jones", gpa=3.85, major="Physics")

# Function definition
def student_info(name, major, gpa, level=1):
    "This prints the passed info into this function"
    print(f"Name: {name}")  # Use f-string to print string and assigned value
    print(f"Major: {major}")
    print(f"GPA: {gpa}")
    print(f"Year level: {level}")
    return

# Call the student_info function to print the values provided
print("----- Positional Arguments ----- ")
student_info("Ezra Berthalomew Johnson", "Neuroscience; Arts", 3.95, 4)

print("----- Keyword Arguments ----- ")
student_info(name="John Jones", gpa=3.85, major="Physics", level=2)

print("----- Default Argument Value ----- ")
student_info(name="Kento Nanami", gpa=3.58, major="Finance")