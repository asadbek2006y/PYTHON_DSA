x = "Hello, World!"

def my_len(x):
    count = 0      # Default 0
    for char in x: # counting chars in x
        count += 1 # Increment count for each char
    return count   # Return the final count
print(my_len(x)) 
mytuple = ("apple", "banana", "cherry")
print(my_len(mytuple))