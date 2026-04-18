from itertools import product, combinations

# 1 & 2. Define two sets
set1 = {"A", "B", "C"}
set2 = {1, 2, 3}

# Generate all possible combinations between the two sets
all_combinations = list(product(set1, set2))

print("All combinations between set1 and set2:")
for combo in all_combinations:
    print(combo)

#Provide an example real-world use case of generating possible combinations. 
## Example can be password generation. A system may generate
## all possible combos to determine how strong a password is.
