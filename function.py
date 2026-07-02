def reverser_array(arr):
    left = 0
    right = len(arr) -1
    
    # swap elements from both end
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr


# exapmple

numbers = [1, 2, 3, 4, 5, 6, 7]

reverse_numbers = reverser_array(numbers)

print("reversed numbers array", reverse_numbers)

# Many Values to Multiple Variables

# Python allows you to assign values to multiple variables in one line:

x, y, z = "Ram", "Shyam", "Sita"

print(x)
print(y)
print(z)
print(x, y, z)