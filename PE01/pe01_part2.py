import random

# Generating a list of 50 random integers
numbers = [random.randint(1, 100) for _ in range(50)]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Original list length: {len(numbers)}")
print(f"Found {len(even_numbers)} even numbers:")
print(even_numbers)