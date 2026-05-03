# What is a function?
# A function is a reusable block of code that performs a specific task. Think of it like a recipe: you write it once, then "call" it whenever you need that task done. Functions help you avoid repeating code, organize your logic, and make your programs easier to read and debug.
# Defining your first function
# In Python, you create a function using the def keyword:

def greet():
    print("Hello, welcome to Python functions!")
greet()  # This will call the function and execute its code

# Parameters and arguments
def greet2(name):   # 'name' is a parameter
    print(f"Hello, {name}!")
greet2("Alice")     # 'Alice' is an argument

def add(a, b):
    return a + b
result = add(5, 3)  # This will return 8
print(result)


def add_all(*numbers):   # *args allows for variable number of arguments
    total = 0
    for num in numbers:
        total += num
    return total
print(add_all(1, 2, 3, 4))  # This will print 10
print(add_all(1, 2, 3, 4,5,6))  # This will print 21


def user_info_scratch(**kwargs):
    # kwargs  bu {'name': 'Asadbek', 'role': 'Developer', 'level': 'B2'}
    for key in kwargs:
        value = kwargs[key]  # Kalit orqali qiymatni qo'lda olish
        print(f"{key}: {value}")

user_info_scratch(name="Asadbek", role="Developer", level="B2")

def describe(**info):
    for name, surname in info.items():
        print(f"{name}: {surname}") 
describe(name="Alice", surname="Smith", age=30)

square = lambda x: x * x
print(square(5))    # 25

def square(x):
    return x * x