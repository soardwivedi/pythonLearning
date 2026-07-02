x = "awesome"

def myfun():
    print("Python is " + x)
    
myfun()


y = "awesome"

def myfun2():
    x = "fentastic"
    print("python is " + x)
    
myfun2()

print("Python is " + y)

# To create a global variable inside a function, you can use the global keyword.

def myfun3():
    global p
    p = "king of Ayodhya"
    print("Ram was " + p)
   
myfun3() 
print(p)