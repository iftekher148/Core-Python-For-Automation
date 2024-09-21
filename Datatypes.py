""" Python Numeric Data Types:"""
# var1 = 1       # int data type
# var2 = True    # bool data type
# var3 = 10.023  # float data type
# var4 = 10+3j   # complex data type

# print("The type of variable having value", var1, " is ", type(var1))
# print("The type of variable having value", var2, " is ", type(var2))
# print("The type of variable having value", var3, " is ", type(var3))
# print("The type of variable having value", var4, " is ", type(var4))

"""Python String Data Type"""
"""However, operations such as slicing and concatenation can be done. Python's str class defines a number of useful methods for string processing. 
Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their
 way from -1 at the end.
The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator in Python."""

str = 'Hello World!'
print(str)
print(str[0])
print(str[2:5])
print(str[1:])
print(str[-1])
print(str[-1:0:-1])    # str[start:end:step]. -1 (step value):A step of -1 means we are moving backward through the string (right to left). This reverses the slice order.
print(str * 2)
print (str + "TEST")