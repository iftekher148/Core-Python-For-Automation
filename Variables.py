# counter = 100          # Creates an integer variable
# miles   = 1000.0       # Creates a floating point variable
# name    = "Zara Ali"   # Creates a string variable
# print (counter)
# print (miles)
# print (name)


""" Delete a variable useing 'del' """
# counter = 100
# print (counter)
# del counter
# print (counter)


"""Getting Type of a Variable. You can get the data type of a Python variable using the python built-in function type()"""
# counter = 100          
# miles   = 1000.0       
# name    = "Zara Ali"  
# print (type(counter))
# print (type(miles))
# print (type(name))


"""Casting variable. You can specify the data type of a variable with the help of casting as follows:"""
# counter = str(100)
# counter1 = int(100)
# counter2 = float(100)
# print("counter:",counter)
# print("counter1:",counter1)
# print("counter2",counter2)


"""Case-Sensitivity of Python Variables: Means Age and age are two different variables"""
# age = 20
# Age = 30
# print( "age =", age )
# print( "Age =", Age )


"""Python Variables - Multiple Assignment: Python allows to initialize more than one variables in a single statement"""
# a,b,c=20,30,40
# print(a,b,c)
# print(a)
# print(b)
# print(c)

# a=b=c=500
# print(a,b,c)

"""Python Local Variables: Python Local Variables are defined inside a function. We can not access variable outside the function."""
def sum(x,y):
    sum=x+y
    return sum
sum(20,30)
print(sum())




