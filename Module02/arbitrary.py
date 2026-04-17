def shopping_list(cart, *items):
    for item in items:
        cart.append(item)  # add each item to the cart
    return cart

# initialize an empty cart
cart = []

# function call
cart = shopping_list(cart, "apples")
cart = shopping_list(cart, "bread", "milk", "eggs", "butter")
cart = shopping_list(cart, 'ink', 'backpack', 'pens', 'notebook')

# Print all the items in your cart
print("Items in the cart: ", cart)