# basic Syntax rules in python (this is a single line comment)
 
'''
 this is a multi line comment
 
 welcome to the python learning

 '''
 
#  Case sensititvity => Python is case sensitive.

# Both name and Name are different variables
name = "Vivek"
Name = "Dwivedi"

print(name)
print(Name)

# Indentation => Python uses indentation to defne blocks of code. Consistent use of spaces (commonly 4) or a tab is reauired.

''' Indentation in Python is used to define the structure and hierarchy of the code. Unlike many other programming languages 
tha use braces {} to delimit blocks of code, Python uses indentation to determine the grouping of statments. This means that all the 
statments within a block must be indentent at the same level.
'''

age = 30
print("age", age)

if age > 20:
    print("age in if", age)
    
print(age)

# Line Continuation 
total = 1+2+3+4+5+ \
        6+7+8+9+10
        
print(total)