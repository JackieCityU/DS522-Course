'''This function handles grocery delivery details.
 It accepts:
 - item: the name of the grocery item
 - quantity: how many units of the item ordered
 - *delivery_info: an arbitrary number of additional details
  (such as customer name, address, phone number, delivery time, and etc.)
'''
def deliver_groceries(item, quantity, *delivery_info):
    print("Grocery delivery details: ")
    print("Item: ", item)
    print("Quantity: ", quantity)

    print("Delivery Information: ")
    for info in delivery_info:
        print(info)