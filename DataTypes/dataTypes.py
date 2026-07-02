# Python has the following data types built-in by default, in these categories:

# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	NoneType



# Setting the Data Type

# In Python, the data type is set when you assign a value to a variable:
x = 5
print(type(x))


# Setting the Specific Data Type

# If you want to specify the data type, you can use the following constructor functions:

y = str("Hello World")
x = int(20)
x = float(20.1)
x = complex(1j)
x = list(("apple", "banana", "Mango"))
x = tuple(("Apple", "Banana", "Mango", "Pine apple"))
x = range(6)
x = {name: "John", age: 39}
x = dict(name="John", age=39)

x = {"apple", "banana", "cherry"}
x = set(("apple", "banana", "cherry"))

x = True
x = b"Hello"
x = bytearray(5)

x = memoryview(bytes(5))



