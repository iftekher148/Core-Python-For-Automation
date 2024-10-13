""" Numeric Data Types """
#     1. int
#     2. flot
#     3. complex

""" Python Numeric Data Types:"""
# var1 = 1       # int data type
# var2 = True    # bool data type
# var3 = 10.023  # float data type
# var4 = 10+3j   # complex data type

# print("The type of variable having value", var1, " is ", type(var1))
# print("The type of variable having value", var2, " is ", type(var2))
# print("The type of variable having value", var3, " is ", type(var3))
# print("The type of variable having value", var4, " is ", type(var4))

"""  Python String Data Type  """
"""Python strings are immutable which means when you perform an operation on strings, you always produce a new string object of the same 
    type, rather than mutating an existing string.A string in Python is an object of str class. It can be verified with type() function."""

"""However, operations such as slicing and concatenation can be done. Python's str class defines a number of useful methods for string processing. 
Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their
 way from -1 at the end.
The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator in Python."""

str = 'Hello World!'
# print(str)
# print(str[0])
# print(str[2:5])
# print(str[1:])
# print(str[-1])
#print(str[-1:0:-1])    # str[start:end:step]. -1 (step value):A step of -1 means we are moving backward through the string (right to left). This reverses the slice order.
# print(str * 2)
# print (str + "TEST")


""" 3. Python Sequence Data Types """
"""Sequence is a collection data type. It is an ordered collection of items. Items in the sequence have a positional index starting with 0. 
    It is conceptually similar to an array in C or C++."""
# 1. List Data Type
# 2. Tuple Data Type
# 3. Range Data Type


"""1. List: Python lists are similar to arrays in C. One difference between them is that all the items belonging to a Python list can be of 
different data type where as C array can store elements related to a particular data type."""

# List_data =["Apple",2024,3.67,5+6j]
# print(type(List_data))
# nested_list =  [['One', 'Two', 'Three'], [1,2,3], [1.0, 2.0, 3.0]]
# print(nested_list)
my_list = ["abc",234,3.55,'Orange',4.66]
tiny_list = ['Yellow',400]
# print(my_list)           # Prints complete list
# print(my_list[0])         # Prints first element of the list
#print(my_list[1:3])         # Prints elements starting from 1st till 3rd. list[1:3] slices the list starting from index 1 (inclusive) to index 3 (exclusive), so it returns the elements at indices 1 and 2.Inclusive: The starting index is included in the slice, meaning the element at start will be part of the result.
                            #Exclusive: The ending index is excluded from the slice, meaning the element at end will not be part of the result.
print(my_list[2:])          # Prints elements starting from 3rd element
# print(my_list[-1])        # Print last element of the list
# print(my_list[-1:0:-1])   # Reverse the list element
print (my_list + tiny_list)     # Prints concatenated lists


"""List"""
# data = ["John", "john@gmail.com", "password123"]
# # data.append("123-456-7890")
# # print(data)
# print(data.pop(1))
# print(data)

# alphabets = ['a','e','d','c','b']
# alphabets.sort()
# print(alphabets)

# user_info = ["Alice", "alice@example.com", "password", "123-456-7890"]
# print(user_info[1:3])

# data = ["user", "email", "password"]
# result = data + ["new data"]
# print(result)

# data = ["name", "email"]
# data[1:1] = ["new_email", "phone"]
# print(data)