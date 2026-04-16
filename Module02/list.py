#create an empty list
empty_list = []
print(empty_list)

#creating a list with strings
str_list = ["alpha", "bravo", "charlie"]

#creating a list with integers
int_list = [0, 1, 2, 3, 4, 5]

#Access elements
print(str_list[2]) #access the 3rd element by using index 2
print(int_list[0:2]) # access elements from 0 to 1.note: this excludes element in index 2
print(str_list[-1]) # access the last element
print(int_list[::-1]) #access elements in reverse

#updating values in a list
print(f"Original value at index 1: {str_list[1]}")
str_list[1] = 'beta'
print(f"Updated value at index 1:{str_list[1]}")

#Adding elements

#The append() method
str_list.append('delta') #appending a single element
print(str_list)

str_list.append(['echo', 'foxtrot']) #appending a list as a single element
print(str_list)

#insert method
str_list.insert(1, 'bravo') #insert the value to index 1
print(str_list)

#extend method
#extending the str_list by adding items in a tuple
str_list.extend(('golf', 'hotel', 'india'))
print(str_list)

#extending the str_list by adding items int the previously created int_list
str_list.extend(int_list)
print(str_list)

#join Lists
#Using the Concatenation Operator(+)
str_list_1 = ['Juliett', 'Kilo', 'Lima']
str_list_2 = list(('Mike', 'November')) #conerting tuple to a list
joined_str_list = str_list + str_list_1 + str_list_2
print(f"joined list: {joined_str_list}")

#Using list comprehension
joined_list = [item for sublist in [str_list_1, str_list_2] for item in sublist]
print(f"another joined list: {joined_list}")

#1. Challenge answers
#The "+" operator creates a brand-new list in memory that contains elements from both operands.
#it leaves the original list untouched and requires both to be lists

#2. The extend() method modifies the existing list by adding elements
     #to the end of it, it updates the original list and returns None.

# pop method
last_1 = str_list.pop()  # no argument
print(f"After popping without arguments: {str_list}")
print(f"Popped item: {last_1}")

# This will not return or print the popped item since we did not store it in a variable
str_list.pop(-1)  # with argument - index of the last item.
print(f"After popping of item in last index : {str_list}")

zero = str_list.pop(8)  # with argument - index of the int 0
print(f"After popping 0 : {str_list}")
print(f"Popped item: {zero}")

#Remove elements
# remove method
str_list.remove('beta')
print(f"After removing beta: {str_list}")

int_list.clear()
print(f"After clearing the int_list: {int_list}")

#delete method
#del int_list
#print(f"After deleting int_list: {int_list}")  # this will cause a NameError: name 'int_list' is not defined

# del keyword
# using to remove an item of the given index
del str_list[4]
print(f"After deleting item in index 4: {str_list}")

[print(i) for i in str_list]

#sort method
print("List after sorting: ", int_list)

# Sorted Function
int_list_1 = [10, 1, 8, 20, 15, 6, 47]

print("Unsorted list: ", int_list_1)

sorted_list = sorted(int_list_1)

print("Sorted list: ", sorted_list)

#Reverse method
sorted_list.reverse()
print("Reversed list: ", sorted_list)